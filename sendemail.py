import smtplib
from config import RULES


def send_email(rates):
    send_preferred = dict()
    for exc in RULES["email"]["preferred"]:
        send_preferred[exc] = rates[exc]

    print(send_preferred)
    sender = "babakft082@gmail.com"
    receiver = RULES["email"]["receiver"]

    message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}
{send_preferred}."""
    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.login("261f765550ac77", "669f7100c11602")
        server.sendmail(sender, receiver, message)
