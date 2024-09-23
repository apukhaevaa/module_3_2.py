# Пухаева Алина Александровна
# Homework for the lesson "Ways to call a function"
# 22.09.2024
# Notes: ctrl+alt+L
def send_email(message, recipient, *, sender="university.help@gmail.com"):
    valid_domains = ['.com', '.ru', '.net']  # Проверяю наличие "@" и доменов

    def is_valid_email(email):
        return "@" in email and any(email.endswith(domain) for domain in valid_domains)

    if not is_valid_email(recipient) or not is_valid_email(sender):    # Проверяю корректность email-адресов
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    if sender == recipient:   # Проверяю на отправку самому себе
        print("Нельзя отправить письмо самому себе!")
        return

    if sender == "university.help@gmail.com": # Проверяю на отправителя по умолчанию
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
