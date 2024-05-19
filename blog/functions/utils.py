import smtplib
from email.header import Header
from email.mime.text import MIMEText
import environ


def send_email(blog):
    env = environ.Env()
    environ.Env.read_env()

    login = env("LOGIN")
    password = env("PASSWORD_EMAIL")
    print(login)
    print(password)

    msg = MIMEText(
        f"Поздравляю, ваша статья {blog.title} "
        f"набрала {blog.views_count} просмотров",
        "plain", "utf-8"
    )
    msg["Subject"] = Header("Поздравляю !!!", "utf-8")
    msg["From"] = login + "@yandex.ru"
    msg["To"] = ",".join(env("EMAIL_TO").split(","))

    s = smtplib.SMTP("smtp.yandex.ru", 587, timeout=10)

    s.starttls()
    s.login(login, password)
    s.sendmail(msg["From"], msg["To"], msg.as_string())

    s.quit()
