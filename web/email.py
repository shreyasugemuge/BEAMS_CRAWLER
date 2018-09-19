import smtplib as mail
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config as C


def compose_and_send(fromaddr, frompass, toaddr, data, ddo):
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = C.EMAIL_SUBJECT.format(DDO=str(ddo))
    body = data
    imgfile = C.LOGO_FILENAME
    fp = open(imgfile, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', '<{}>'.format(imgfile))
    msg.attach(MIMEText(body, 'html'))
    msg.attach(msgImage)
    print("Assembled Email")
    send(msg, fromaddr, frompass, toaddr)


def send(msg, fromaddr, frompass, toaddr):
    text = msg.as_string()
    s = mail.SMTP('smtp.gmail.com', 587)
    print("Making TLS Connection")
    s.starttls()
    print("Authenticating SMTP client")
    s.login(fromaddr, frompass)
    print("Sending email")
    s.sendmail(fromaddr, toaddr, text)
    print("Email has been sent")


def gen_section(thres, df):
    print("Generating Section {f}".format(f=str(thres-1)))
    if (df.shape[0] == 0):
        return ""
    final = C.SECTION_HEADER.format(color=C.COLOR[thres], thres=C.THRES[thres])
    count = 1
    for ind, data in df.iterrows():
        final += '<h4>' + str(count) + ". " + data['Scheme & Detail Head'] + ': ' + str(
            data['Spending']) + ' %' + '<h4>'
        count += 1
    return final
