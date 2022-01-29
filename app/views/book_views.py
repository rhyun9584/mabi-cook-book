from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    g,
    flash,
    request,
    Response,
)

from app import db
from app.models import Cook, User, Collect

bp = Blueprint('book', __name__, url_prefix='/book')


@bp.route('/', methods=('GET',))
def main():
    if g.user == None:
        # 로그인 해야지만 도감 페이지에 접근 가능
        flash("도감 페이지를 이용하기 위해서는 로그인이 필요합니다.")
        return redirect(url_for('auth.signin'))

    cook_list = Cook.query.all()
    collect_list = Collect.query.filter_by(user=g.user.id).all()

    return render_template('book/book.html', cook_list=cook_list, collect_list=collect_list)


@bp.route('/change_state/', methods=('POST',))
def change_state():
    user_id = User.query.get_or_404(g.user.id).id
    data = request.get_json()

    collect = Collect.query.get_or_404({"user": user_id, "cook": data['cook_id']})
    collect.state = data['new_state']
    db.session.commit()

    return Response('', status=200)
