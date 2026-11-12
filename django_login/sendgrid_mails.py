# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
load_dotenv()

def send_email(from_mail, to_email, mail_subject, mail_content):
    api_key = os.environ.get('SENDGRID_API_KEY')
    if not api_key:
        # Sin API key (p. ej. entorno local) no se envía correo, pero el flujo continúa.
        print('SENDGRID_API_KEY no configurada: se omite el envío de correo.')
        return
    message = Mail(
        from_email=from_mail,
        to_emails=to_email,
        subject=mail_subject,
        html_content=mail_content
    )
    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
    except Exception as e:
        print(e)