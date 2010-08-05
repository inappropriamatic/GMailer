#!/usr/bin/python

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import Encoders

class GMailer():
    """A Class for emailing text and attachments"""
    self.gmail_user = "inappropriamatic@gmail.com"
    self.gmail_pwd = "hunter2"
    
    
    def set_credientials(user, password):
        self.gmail_user = user
        self.gmail_pwd = password
    
    
    def mail(self, to, subject, text, attachments=[]):
       msg = MIMEMultipart()
    
       msg['From'] = gmail_user
       msg['To'] = to
       msg['Subject'] = subject
    
       msg.attach(MIMEText(text))
    
       
       for attach in attachments:
          part = MIMEBase('application', 'octet-stream')
          part.set_payload(open(attach, 'rb').read())
          Encoders.encode_base64(part) 
          part.add_header('Content-Disposition',
                   'attachment; filename="%s"' % os.path.basename(attach))
          msg.attach(part)
    
       mailServer = smtplib.SMTP("smtp.gmail.com", 587)
       mailServer.ehlo()
       mailServer.starttls()
       mailServer.ehlo()
       mailServer.login(gmail_user, gmail_pwd)
       mailServer.sendmail(gmail_user, to, msg.as_string())
       mailServer.close()

