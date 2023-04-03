from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    flash,
    session,
    g,
    abort,
)
from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from sqlalchemy import func

from app import db
from app.forms import (
    UserCreateForm,
    UserSigninForm,
    ChangePwForm,
    SearchPwForm,
    ResetPwForm,
    LeaveForm,
)
from app.models import User, Cook, Collect, ResetPw

from tasks import mail_send


bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    if g.user:
        # 이미 로그인된 경우 404 return
        abort(404)

    form = UserCreateForm()

    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            user = User(email=form.email.data,
                        password=generate_password_hash(form.password1.data),
                        name=form.server.data + '@' + form.name.data,
                        )
            db.session.add(user)
            db.session.commit()

            # 유저의 collect 정보 init
            cook_list = Cook.query.all()
            for cook in cook_list:
                collect = Collect(user=user.id, cook=cook.id)
                db.session.add(collect)
                db.session.commit()

            # 회원가입이 완료되면 로그인 페이지로 redirect
            return redirect(url_for('auth.signin'))
        else:
            flash('이미 존재하는 email ID입니다.')

    return render_template('auth/signup.html', form=form)

@bp.route('/signin/', methods=('GET', 'POST'))
def signin():
    if g.user:
        # 이미 로그인 된 경우 404 return
        abort(404)

    form = UserSigninForm()

    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user or not check_password_hash(user.password, form.password.data):
            error = "아이디 혹은 비밀번호가 올바르지 않습니다."
            flash(error)
        else:
            session.clear()
            session['user_id'] = user.id

            next = request.form.get("next")
            if next:
                return redirect(next)
            return redirect(url_for('main.main'))

    return render_template('auth/signin.html', form=form)

@bp.route('/signout/', methods=('GET',))
def signout():
    session.clear()

    return redirect(url_for('main.main'))

@bp.route('/change_pw/', methods=('GET', 'POST'))
def change_pw():
    if g.user == None:
        # 로그인되지 않은 상태에는 비밀번호 변경 불가능
        # abort(404)
        return redirect(url_for('auth.signin'))

    form = ChangePwForm()

    if request.method == 'POST' and form.validate_on_submit():
        user = g.user

        if check_password_hash(user.password, form.old_pw.data) is False:
            error = "현재 비밀번호가 올바르지 않습니다."
            flash(error)
        else:
            user.password = generate_password_hash(form.new_pw1.data)
            db.session.commit()
            return redirect(url_for('main.main'))

    return render_template('auth/changepw.html', form=form)

@bp.route('/search_pw/', methods=('GET', 'POST'))
def search_pw():
    if g.user:
        return abort(404)

    form = SearchPwForm()

    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        uuid = str(uuid4())

        duplicate = ResetPw.query.filter_by(addr=uuid).first()
        while duplicate is not None:
            uuid = str(uuid4())
            duplicate = ResetPw.query.filter_by(addr=uuid).first()

        page = ResetPw(
            user=user.id,
            addr=uuid,
        )
        db.session.add(page)
        db.session.commit()

        origin_url = request.url_root

        mail_send.delay(user.email, origin_url, uuid)

        return render_template('auth/sending_email.html')

    return render_template('auth/searchpw.html', form=form)

@bp.route('/reset_pw/<uuid>/', methods=('GET', 'POST'))
def reset_pw(uuid):
    # 비밀번호 찾기 로직을 통해 받은 이메일 링크를 통해 비밀번호 변경
    page = ResetPw.query.filter_by(addr=uuid).first()
    if page is None or page.is_expired == True:
        return abort(404)

    form = ResetPwForm()

    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.get(page.user)
        user.password = generate_password_hash(form.new_pw1.data)

        # 한 번 비밀번호 변경에 사용된 페이지는 바로 expired
        page.is_expired = True

        db.session.commit()
        return render_template('auth/complete_resetpw.html')

    return render_template('auth/resetpw.html', form=form)

@bp.route('/leave/', methods=('GET', 'POST'))
def leave():
    if g.user == None:
        # 로그인하지 않은 채로 회원탈퇴 불가능
        abort(404)

    form = LeaveForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = g.user

        if not check_password_hash(user.password, form.password.data):
            error = "비밀번호가 올바르지 않습니다."
            flash(error)
        else:
            db.session.delete(user)
            db.session.commit()

            session.clear()

            return render_template('auth/after_leave.html')

    return render_template('auth/leave.html', form=form)

@bp.route('/info/', methods=('GET',))
def info():
    if g.user == None:
        abort(404)

    collects = Collect.query.with_entities(Collect.state, func.count(Collect.state)).group_by(Collect.state).all()

    state_count = {0: 0, 1: 0, 2: 0}
    for co in collects:
        state_count[co[0]] = co[1]

    return render_template('auth/info.html', count=state_count)

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)
