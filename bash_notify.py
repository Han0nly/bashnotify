#!/usr/bin/python
# -*- encoding:utf-8 -*-
import sys
import subprocess
from email.mime.text import MIMEText
import smtplib

class sendMail():

    def txtMail(self,content):
        msg = MIMEText(content,_subtype='plain',_charset='gb2312')
        msg['to'] = 'dest@email.com' # change this to the reciever email address
        msg['from'] = 'Your_email_address' # change this to you email address
        msg['subject'] = 'exec result'
        try:
            server = smtplib.SMTP_SSL('smtp.ym.163.com',994) # change this to your SMTP server
            # server.connect()
            server.login('Your_email_address','Your_Password') # change the email address and password to your address and password
            server.sendmail(msg['from'], msg['to'],msg.as_string())
            server.quit()
            print("Send Email Successfully!")
        except Exception as e:
            print(str(e))

if __name__=='__main__':
    comm= ' '.join( [ str(x) for x in sys.argv[1:]])
    (status, output) = subprocess.getstatusoutput(comm)
    sendMail().txtMail("comm:%s;status:%s;output:%s" % (comm,status,output))

