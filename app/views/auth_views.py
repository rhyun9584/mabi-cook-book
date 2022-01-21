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
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from app import db
from app.forms import UserCreateForm, UserSigninForm
from app.models import User


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
                        name=form.name.data,
                        )
            db.session.add(user)
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
        error = None
        user = User.query.filter_by(email=form.email.data).first()
        if not user or not check_password_hash(user.password, form.password.data):
            error = "아이디 혹은 비밀번호가 올바르지 않습니다."
            flash(error)
        else:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('main.main'))

    return render_template('auth/signin.html', form=form)

@bp.route('/signout/', methods=('GET',))
def signout():
    session.clear()

    return redirect(url_for('main.main'))


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)