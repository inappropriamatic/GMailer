#!/usr/bin/python

import smtplib
import os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import Encoders

class GMailer():
    """A Class for emailing text and attachments"""
    def __init__(self):
        self.gmail_user = "inappropriamatic@gmail.com"
        self.gmail_pwd = "hunter2"
    
    
    def set_credentials(user, password):
        self.gmail_user = user
        self.gmail_pwd = password
    
    
    def mail(self, to, subject, text, attachments=[]):
       msg = MIMEMultipart()
    
       msg['From'] = self.gmail_user
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
       mailServer.login(self.gmail_user, self.gmail_pwd)
       mailServer.sendmail(self.gmail_user, to, msg.as_string())
       mailServer.close()

