import smtplib
import os

# Constants
my_email = os.environ.get("KMAIL")
password = os.environ.get("KPASS")
to_email = os.environ.get("RMAIL")

# Functions


def mail_sender(message):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email,
                            msg="Subject:Você tem uma nova resposta para o seu Formulário!!\n\n"
                                f"{message}".encode("utf8"))

