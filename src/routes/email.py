from flask import request, Blueprint, Response, jsonify, current_app, render_template
from flask import current_app
import json
from src import config, app

from src.dependencies.smtp_config import send_mail
from datetime import date

# This is the blueprint object that gets registered into the app in blueprints.py.
email = Blueprint('email', __name__,
                    template_folder='templates')



@email.route("/send_email", methods=['POST'])
def send_email():
    json_data = request.json
    msg_body = render_template('/pages/{}.html'.format(json_data['template']),
                                json_data=json_data
                                )

    return send_mail(
        json_data['title'],
        [json_data['email']],
        msg_body)    
