import smtplib
import pandas as pd
from supersecret import uname, pwd

# my email settings
SUBJECT = "[python-workshop] Thank you for participating"
FROM = "Ivana <...@uwaterloo.ca>"

# load contact data and email text
file_names = ['contacts_data.csv']
email_texts = ['email_text.txt']

# connect to server
server = smtplib.SMTP(host='mxer.uwaterloo.ca', port=25)
server.set_debuglevel(True)
server.ehlo()
server.starttls()
server.ehlo()
server.login(uname, pwd)

for file_name, email_text_path in zip(file_names, email_texts):

    data = pd.read_csv(file_name, delimiter=',')

    # load e-mail text
    with open(email_text_path, 'r') as f:
        text_rows = f.readlines()
        text_template = "".join(text_rows)

    # send a personalized email to each contact
    for _, name, email in data.itertuples():
        firstname = name[:name.find(' ')]
        to = email.strip()
        text = text_template.format(firstname)

        BODY = "From: {}\r\nTo: {}\r\nSubject: {}\r\n\r\n{}\r\n".format(
            FROM, email, SUBJECT, text)

        server.sendmail(FROM, [to], BODY)

server.quit()
