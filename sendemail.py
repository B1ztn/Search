import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
sender = "zhangtn0227@hotmail.com"
receiver = "tzhang@msqventures.com" 
subject = "say hi from tiannan's python"
smtpserver = "smtp.exmail.hotmail.com"
 
user = 'zhangtn0227@hotmail.com'
password = 'B1b13221'
 
msg = MIMEText('hello this is tiannan')
msg['Subject'] = Header(subject)
msg['From'] = 'zhangtn0227@hotmail.com'
msg['To'] = 'tzhang@msqventures.com'
smtp = smtplib.SMTP()
smtp.connect('smtp-mail.outlook.com')
smtp.ehlo()
smtp.starttls()
smtp.login(user,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()