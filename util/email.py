import smtplib as mail
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


def compose_and_send(fromaddr, frompass, toaddr, name, data, ddo, imgfile='plot.png'):
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "DDO Expense reminder"
    body = '%s<br><BR><img src="cid:%s" style = "width:900px;"><br><BR>' % (data.format(name=name,ddo=ddo), imgfile) + '<br><BR>' \
                        'Thank You,<br>GIS Team<BR>' \
                        '<hr><small> Disclaimer: ' \
                        'This is an auto generated email. The data is obtained from the BEAMS portal ' \
                        '(https://beams.mahakosh.gov.in/Beams5/BudgetMVC/MISRPT/DDOFundReport.jsp)' \
                        'and is accurate as of 14 September 2018. ' \
                        'In case of questions contact +911231231231.</small> '
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
