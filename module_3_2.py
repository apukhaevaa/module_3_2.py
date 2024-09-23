# Пухаева Алина Александровна
# Homework for the lesson "Ways to call a function"
# 22.09.2024
# Notes: ctrl+alt+L
def send_email(message, recipient, *, sender):
    standard_senders = ['university.help@gmail.com', 'urban.teacher@mail.ru']
    if sender == recipient:
        print(f'Нельзя отправить письмо самому себе!')
        return
    if sender not in standard_senders:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
send_email('Напоминание', 'vasyok1337@gmail.com', sender='university.help@gmail.com')
send_email('Новое письмо', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Не отправляется', 'urban.student@mail.ru', sender='urban.teacher@mail.ru')
