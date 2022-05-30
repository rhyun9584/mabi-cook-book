from celery import states
from celery.exceptions import Ignore
from flask_mail import Message

from app import celery, db, mail
from app.models import ResetPw


@celery.task
def mail_send(receive, uuid):
    msg = Message()
    msg.subject = 'password reset link'
    msg.body = f'http://127.0.0.1:5000/auth/reset_pw/{uuid}/'
    msg.recipients = [receive, ]
    msg.sender = 'rhyun95@gmail.com'

    mail.send(msg)

    # 30분 뒤 링크 expired (테스트는 120초로..)
    delete_reset_pw_page.apply_async((uuid,), countdown=120)

@celery.task(bind=True)
def delete_reset_pw_page(self, uuid):
    page = ResetPw.query.filter_by(addr=uuid).first()
    if page is None:
        self.update_state(
            state=states.FAILURE,
            meta=f"Cannot find page about addr(uuid): {uuid}",
        )
        raise Ignore

    page.is_expired = True
    db.session.commit()
