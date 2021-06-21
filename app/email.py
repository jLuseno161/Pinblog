from flask_mail import Message
from flask import render_template
from app import mail
from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
mail = Mail(app)

sender_email = 'projectsmoringa@gmail.com'
subject_pref = 'PinBlog'

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'projectsmoringa@gmail.com'
app.config['MAIL_PASSWORD'] = 'Moringa20'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


def mail_message(subject, template, to, **kwargs):
    email = Message(subject_pref + " " + subject,
                    sender=sender_email,
                    recipients=[to])
    email.body = render_template(template + ".txt", **kwargs)
    mail.send(email)
    # print(email)

def sub_message(subject, template, to, **kwargs):
    email = Message(subject_pref + " " + subject,
                    sender=sender_email,
                    recipients=[to])
    email.body = render_template(template + ".txt", **kwargs)
    mail.send(email)
    # print(email)


if __name__ == '__main__':
    app.run()
