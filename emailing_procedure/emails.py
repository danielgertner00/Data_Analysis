import email
from email.mime.multipart import MIMEMultipart
import smtplib

emls = {
    1: 'files/Dzień 1 - Trening uważności.eml',
    2: 'files/Dzień 2 - Trening uważności.eml',
    3: 'files/Dzień 3 - Trening uważności.eml',
    4: 'files/Dzień 4 - Trening uważności.eml',
    5: 'files/Dzień 5 - Trening uważności.eml',
    6: 'files/Dzień 6 - Trening uważności.eml',
    7: 'files/Dzień 7 - Trening uważności.eml',
    8: 'files/Dzień 8 - Trening uważności.eml',
    9: 'files/Dzień 9 - Trening uważności.eml',
    10: 'files/Dzień 10 - Trening uważności.eml',
    11: 'files/Dzień 11 - Trening uważności.eml',
    12: 'files/Dzień 12 - Trening uważności.eml',
    13: 'files/Dzień 13 - Trening uważności.eml',
    14: 'files/Dzień 14 - Trening uważności.eml',
    15: 'files/Dzień 15 - Trening uważności.eml',
    16: 'files/Dzień 16 - Trening uważności.eml',
    17: 'files/Dzień 17 - Trening uważności.eml',
    18: 'files/Dzień 18 - Trening uważności.eml',
    19: 'files/Dzień 19 - Trening uważności.eml',
    20: 'files/Dzień 20 - Trening uważności.eml',
    21: 'files/Dzień 21 - Trening uważności.eml',
    22: 'files/Dzień 22 - Trening uważności.eml',
    23: 'files/Dzień 23 - Trening uważności.eml',
    24: 'files/Dzień 24 - Trening uważności.eml',
    25: 'files/Dzień 25 - Trening uważności.eml',
    26: 'files/Dzień 26 - Trening uważności.eml',
    27: 'files/Dzień 27 - Trening uważności.eml',
    28: 'files/Dzień 28 - Trening uważności.eml',
    29: 'files/Dzień 29 - Trening uważności.eml',
    30: 'files/Dzień 30 - Trening uważności.eml',
    31: 'files/Dzień 31 - Trening uważności.eml'
}

def eml_reader(eml_path):
    with open(eml_path, 'rb') as f:
        msg = email.message_from_bytes(f.read())
    return msg

def msg_creator(eml_path, sender, recipient):
    msg = eml_reader(eml_path)
    if sender:
        msg.replace_header('From', sender)
    if recipient:
        msg.replace_header('To', recipient)
    # raw_msg = base64.urlsafe_b64encode(msg.as_bytes()).decode('utf-8')
    return msg

def send_email(recipient_email, day):
    msg = msg_creator(emls.get(day), 'treninguwaznosciswps@gmail.com',
               recipient_email)
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'treninguwaznosciswps@gmail.com'
    smtp_password = 'slhf wgnt snsx qhil'

    m_msg = MIMEMultipart()
    m_msg['From'] = msg.get('From')
    m_msg['To'] = msg.get('To')
    m_msg['Subject'] = msg.get('Subject')
    m_msg.attach(msg)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as smtp:
            smtp.starttls()
            smtp.login(smtp_username, smtp_password)
            smtp.send_message(m_msg)
        print("Email sent successfully!")

    except smtplib.SMTPException as e:
        print(f"SMTP error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")