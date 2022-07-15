import smtplib
from config import RULES


def send_email(rates):
    """
FINDING RIGHT preferred
    """
    send_preferred = dict()
    for exc in RULES["email"]["preferred"]:
        send_preferred[exc] = rates[exc]

    using_email_service(send_preferred)


def using_email_service(text):
    """
    sending through mailtrap
    """

    sender = "babakft082@gmail.com"
    receiver = RULES["email"]["receiver"]
    message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}
{text}."""
    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.login("261f765550ac77", "669f7100c11602")
        server.sendmail(sender, receiver, message)
