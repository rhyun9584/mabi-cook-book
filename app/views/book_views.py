from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    g,
    flash,
    request,
    Response,
    make_response,
)
from sqlalchemy import or_

from app import db
from app.models import Cook, User, Collect
from app.enums import Method

bp = Blueprint('book', __name__, url_prefix='/book')


@bp.route('/', methods=('GET',))
def main():
    if g.user == None:
        # 로그인 해야지만 도감 페이지에 접근 가능
        flash("도감 페이지를 이용하기 위해서는 로그인이 필요합니다.")
        return redirect(url_for('auth.signin'))

    query = request.args.get('q', type=str, default='')
    range = request.args.get('r', type=str, default='all')
    method = request.args.get('m', type=str, default='')
    collected = request.args.get('c', type=str, default='')

    # Cook 모델과 Collect join 및 user 필터링
    join_query = db.session.query(Cook, Collect).join(Collect, Collect.cook == Cook.id)\
        .filter(Collect.user == g.user.id)

    # Cook 모델 필터링
    if query:
        if range == 'name':
            join_query = join_query.filter(Cook.name.like(f'%{query}%'))
        elif range == 'ingredients':
            join_query = join_query.filter(Cook.ingredients.like(f'%{query}%'))
        else:
            join_query = join_query.filter(or_(Cook.name.like(f'%{query}%'), Cook.ingredients.like(f'%{query}%')))

    if method:
        method_list = method.rstrip().split(" ")
        join_query = join_query.filter(Cook.method.in_(method_list))

    # Collect 모델 필터링
    if collected:
        collected_list = collected.rstrip().split(" ")
        join_query = join_query.filter(Collect.state.in_(collected_list))

    join_list = join_query.all()
    method_list = list(Method)

    resp = make_response(render_template('book/book.html', join_list=join_list,
                                         method_list=method_list, query=query, range=range))
    resp.set_cookie('range', range)
    # resp.set_cookie('method', method)
    # resp.set_cookie('collected', collected)

    return resp


@bp.route('/change_state/', methods=('POST',))
def change_state():
    user_id = User.query.get_or_404(g.user.id).id
    data = request.get_json()

    collect = Collect.query.get_or_404({"user": user_id, "cook": data['cook_id']})
    collect.state = data['new_state']
    db.session.commit()

    return Response('', status=200)
