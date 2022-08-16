import flask
from datetime import datetime

# MESSENGER
all_messages = []  # list of all messages


# Print message
def print_message(message):
    print(f"[{message['time']} {message['sender']}]: {message['text']}")


# Add new message
def add_message(sender, text):
    # dictionary
    # key : value
    new_message = {
        "sender": sender,
        "text": text,
        "time": datetime.now().strftime('%H:%M')
    }
    all_messages.append(new_message)


add_message("Andrey", "Всё хорошо")
add_message("Artur", "Погромче")
add_message("Поляр", "Много пользователей")


for message in all_messages:
    print_message(message)
