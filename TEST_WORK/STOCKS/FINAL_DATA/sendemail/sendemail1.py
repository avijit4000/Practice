from email.message import EmailMessage
import ssl
import smtplib


email_sender="avijit4000@gmail.com"
email_passward="lwrp hpjd arae czvv"

email_recever="avijitindia01@gmail.com"

subject="Test Mail"
body="This is a test mail."

em=EmailMessage()
em["From"]=email_sender
em["To"]=email_recever
em["subject"]=subject
em.set_content(body)

context=ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_passward)
    smtp.sendmail(email_sender,email_recever, em.as_string())