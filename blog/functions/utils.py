import smtplib
from email.header import Header
from email.mime.text import MIMEText
import environ
from django.core.mail import send_mail


def get_db_login(keys):
    env = environ.Env()
    environ.Env.read_env()
    return env(keys)


send_mail(
    subject='Поздравляю!!!',
    message='Поздравляю ваш пост набрал 100 просмотров, Ура ...',
    from_email=get_db_login('LOGIN') + '@yandex.ru',
    recipient_list=[f'{get_db_login('LOGIN')} + @yandex.ru'],
    fail_silently=False
)

# def send_email(blog):
#     env = environ.Env()
#     environ.Env.read_env()
#
#     login = env("LOGIN")
#     password = env("PASSWORD_EMAIL")
#     print(login)
#     print(password)
#
#     msg = MIMEText(
#         f"Поздравляю, ваша статья {blog.title} "
#         f"набрала {blog.views_count} просмотров",
#         "plain", "utf-8"
#     )
#     msg["Subject"] = Header("Поздравляю !!!", "utf-8")
#     msg["From"] = login + "@yandex.ru"
#     msg["To"] = ",".join(env("EMAIL_TO").split(","))
#
#     s = smtplib.SMTP("smtp.yandex.ru", 587, timeout=10)
#
#     s.starttls()
#     s.login(login, password)
#     s.sendmail(msg["From"], msg["To"], msg.as_string())
#
#     s.quit()
