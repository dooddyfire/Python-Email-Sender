import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 


def send_email(sender_email,sender_password,recipient_email,subject,message): 

    # บอกให้ปลายทาง เมลผู้รับ รู้ว่าเราจะส่งเมลรูปแบบไหนไป text , image 
    msg = MIMEMultipart()

    msg.attach(MIMEText(message,'plain'))

    msg['From'] = sender_email 
    msg['To'] = recipient_email 
    msg['Subject'] = subject 

    # เริ่มส่งเมล 
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    
    server.login(sender_email,sender_password)

    server.sendmail(sender_email,recipient_email,msg.as_string())

    server.quit()


if __name__ == '__main__': 
    
    sender_email = "sender@gmail.com"

    # App Password คนละตัวกับ Password ปกติที่เราใช้เข้าเมล

    # https://myaccount.google.com/apppasswords
    sender_password = "gvwwytbgwzqednzh"

    recipient_email = "recipient@gmail.com"
    message = "ทดสอบการส่ง Email ด้วย Python"
    subject ="Python Email EP 1"

    send_email(sender_email,sender_password,recipient_email,subject,message) 
