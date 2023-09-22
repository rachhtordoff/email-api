# this code must use environment variables for original config as we will be changing the application config

import os
from src import app
from flask_mail import Mail
from flask import current_app
from flask_mail import Message

def get_smtp_config():
	mail = Mail()
	app.config.update(dict(
		MAIL_SERVER = os.environ['MAIL_SERVER'],
		MAIL_PORT = os.environ['MAIL_PORT'],
		MAIL_USE_TLS = True,
		MAIL_USE_SSL = False,
		MAIL_USERNAME = os.environ['MAIL_USERNAME'],
		MAIL_PASSWORD = os.environ['MAIL_PASSWORD'],
	))
	mail.init_app(app)
	return mail

def send_mail(title, recipient, body):
	mail = get_smtp_config()
	msg = Message(
            title,
            sender=app.config['MAIL_USERNAME'],
            recipients=recipient
            )

	msg.html = body

	try:
		mail.send(msg)
	except Exception as e:
		print(e)
		current_app.logger.error('Unhandled Exception: %s', repr(e))
		return 'error'
	else:
		current_app.logger.info('email sent')
		return 'sent'

