from config import AccountSMTP, logging


class Msg:
    subject = None
    text = None
    id_template = None
    variables = None
    recipients = None

    def __init__(self, subject,  id_template, variables, recipients, text=None):
        self.subject, self.text, self.id_template, self.variables, self.recipients = \
            subject, text, id_template, variables, recipients


class Email:
    account_smtp = None

    def __init__(self, account_smtp):
        self.account_smtp = account_smtp

    def send(self, recipients: list, subject: str, text: str = None, html: str = None):
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        import smtplib

        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['To'] = ', '.join(recipients)
        msg['From'] = f'{self.account_smtp.SENDER} <{self.account_smtp.USER}>'
        msg['Reply-To'] = self.account_smtp.USER
        if text:
            msg.attach(MIMEText(text, 'plain'))
        if html:
            msg.attach(MIMEText(html, 'html'))
        try:
            mail = smtplib.SMTP_SSL(self.account_smtp.SERVER)
            mail.login(self.account_smtp.USER, self.account_smtp.PASSWORD)
            mail.sendmail(self.account_smtp.USER, recipients, msg.as_string())
            mail.quit()
        except Exception as e:
            logging.critical(
                f'error: {str(e)}, recipients: {recipients}, subject: {subject}, text: {text}, html: {html}'
            )
            return str(e)
        return None


class EmailHandler:

    @staticmethod
    def send_msg(msg: Msg):
        from message.models import Message, Recipient, Templates, Error
        from datetime import datetime
        template = Templates.objects.get(id=msg.id_template)
        msg_db = Message(subject=msg.subject, text=msg.text, id_template=template)
        msg_db.save()
        email = Email(AccountSMTP)
        for recipient in msg.recipients:
            recipient_db = Recipient(email=recipient, id_message=msg_db)
            recipient_db.save()
            error = email.send([recipient], msg.subject, html=template.html.format(**msg.variables))
            if error:
                Error(id_message=msg_db, description=error).save()
            else:
                recipient_db.send = datetime.now()
                recipient_db.save()
