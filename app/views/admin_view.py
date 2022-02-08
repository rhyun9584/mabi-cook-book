from flask import (
    g,
    abort,
)
from flask_admin.contrib.sqla import ModelView

from app import db
from app.models import User, Collect


class NewModelView(ModelView):
    def is_accessible(self):
        if g.user and g.user.is_admin:
            return True
        return False

    def inaccessible_callback(self, name, **kwargs):
        return abort(404)


class UserModelView(NewModelView):
    can_delete = False
    can_create = False

    column_exclude_list = ('password', )
    column_editable_list = ('is_admin', )


class CookModelView(NewModelView):
    column_searchable_list = ('name', 'ingredients',)
    column_filters = ('method',)

    def after_model_change(self, form, model, is_created):
        # row가 생성되면 모든 user에 대해 collect row 생성
        if is_created:
            user_list = User.query.all()
            for user in user_list:
                collect = Collect(user=user.id, cook=model.id)
                db.session.add(collect)
            db.session.commit()

    # row를 삭제하면 관련 collect row 전부 삭제
    def on_model_delete(self, model):
        Collect.query.filter_by(cook=model.id).delete()
        db.session.commit()


class CollectModelView(NewModelView):
    # Collect db 테이블 확인용
    can_delete = False
    can_create = False
    can_edit = False

    column_list = ('user', 'cook', 'state')
    column_sortable_list = ('user', 'cook')
    column_filters = ('user', 'cook')
