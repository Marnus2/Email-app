import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "marnusl365@gmail.com"
    password = "hohner123#"

    receiver = "marnusl365@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

# test function
if __name__ == "__main__":
    message = "HELLO THERE"
    send_email(message)