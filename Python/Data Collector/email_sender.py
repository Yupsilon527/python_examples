from email.mime.text import MIMEText
import smtplib

def sendemail(nemail, height):

    message = "Hey there! Your height is %s." % height

    msg = MIMEText(message,'html')
    msg["Subject"] = "Height Survey"
    msg["To"] = nemail
    msg["From"] = "paulsendroiu@gmail.com"

    gmail.smtplib.SMTP("smtp.gmail.com",587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(msg["From"],"password")
    gmail.sendemail(message)