from flask import Flask
from flask_mail import Mail, Message
from app import fileread


app = Flask(__name__)
def send_mail():
  EMAIL_USER=""#type your email
  EMAIL_PASSWORD=""#type your password

  mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME":EMAIL_USER,
    "MAIL_PASSWORD":EMAIL_PASSWORD
  }

  app.config.update(mail_settings)
  mail = Mail(app)
  with app.app_context():
        msg = Message(subject="Hello",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=[Recipeint_mail], 
                      body="This is a test email I sent with Gmail and Python!")
        mail.send(msg)
        
#To send an automated mail
def send_mail():
  EMAIL_USER="painitehelp@gmail.com"
  EMAIL_PASSWORD="coventryj4"
  e=getmessage()
  filewrite("get_email.txt",e)
  r=fileread("get_email.txt")


  mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME":EMAIL_USER,
    "MAIL_PASSWORD":EMAIL_PASSWORD
  }

  app.config.update(mail_settings)
  mail = Mail(app)
  with app.app_context():
        msg = Message(subject="Hello",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=[r],
                      body=("Thanks for using Painite. The information you asked for is written below:"+str(details2())+"\nBest Regards, \nPainite"))
        if type(msg.recipients) is list: 
          msg.recipients = msg.recipients 
        else: 
          msg.recipients = (msg.recipients).split()
  if '@uni.coventry.ac.uk' in r:      
        mail.send(msg)
        return(True)  
  else:
    return False

  if '@' in r:
      a=send_mail()
      if a==True:
        return("Email has been sent. Please check your inbox.")
      else:
        return("Please enter a valid email")
