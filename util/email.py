import smtplib as mail
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


def compose_and_send(fromaddr, frompass, toaddr, name, data, imgfile='plot.png'):
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "DDO Expense reminder"
    body = '%s<br><img src="cid:%s" style = "width:900px;"><br>' % (data.format(name=name), imgfile)

    fp = open(imgfile, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    msgImage.add_header('Content-ID', '<{}>'.format(imgfile))
    msg.attach(MIMEText(body, 'html'))
    msg.attach(msgImage)
    send(msg, fromaddr, frompass, toaddr)


def send(msg, fromaddr, frompass, toaddr):
    text = msg.as_string()
    s = mail.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, frompass)
    s.sendmail(fromaddr, toaddr, text)
    print("email has been sent")
