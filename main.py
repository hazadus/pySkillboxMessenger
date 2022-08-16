from flask import Flask, request, render_template
from datetime import datetime
import json

DB_FILE = "./db.json"

all_messages = []
app = Flask(__name__)  # Create new app


def load_messages():
    # json_file = open(DB_FILE, "r")
    # json_data = json.load(json_file)
    with open(DB_FILE, "r") as json_file:
        json_data = json.load(json_file)
    return json_data["messages"]


def save_messages():
    data = {
        "messages": all_messages
    } # TODO: доделать
    # https://colab.research.google.com/drive/110dro_DjbcoxzLvt6KLbQSJxzeanlhs3?usp=sharing



@app.route("/")
def index_page():
    return "Hello from <b>index page</b>!"


# Get list of all messages
# Flask кодирует в JSON если функция возвращает словарь
@app.route("/get_messages")
def get_messages():
    return {"messages": all_messages}  # json-valid format


# Print message
def print_message(message):
    print(f"[{message['time']} {message['sender']}]: {message['text']}")


@app.route("/chat")
def display_chat():
    return render_template("form.html")


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


@app.route("/send_message")
def send_message():
    # get sender name and message text
    sender = request.args["name"]
    text = request.args["text"]
    add_message(sender, text)
    save_messages()

    return "OK"


all_messages = load_messages()  # list of all messages

# TODO: remove after first run
add_message("Andrey", "Всё хорошо")
add_message("Artur", "Погромче")
add_message("Поляр", "Много пользователей")


app.run()
