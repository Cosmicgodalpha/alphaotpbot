from cred import *
from mainn import *
from dbase import *
from flask_session import Session

path = 'UserDetails.db'
conn = sqlite3.connect(path, check_same_thread=False)

c = conn.cursor()

# Twilio connection
client = Client(account_sid, auth_token)

# Flask connection
app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'dljkjwdo2knds'
Session(app)

#sslify = SSLify(app)

# Bot connection
bot = telebot.TeleBot(API_TOKEN, threaded=False)
bot.remove_webhook()
bot.set_webhook(url=callurl)

# Some variables
# userid = None
# chat_id = None


# Process webhook calls
@app.route('/', methods=['GET', 'POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        print("error")
        flask.abort(403)


# Handle '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    send = bot.send_message(message.chat.id, "what is your name")
    bot.register_next_step_handler(send, function2)

def function2(message):
    name = message.text
    userid = message.from_user.id
    chat_id = userid

    session['userid'] = f'{userid}'
    session['chat_id'] = f'{chat_id}'

    phonenumber = fetch_phonenumber(userid)
    print(phonenumber)

    call = client.calls.create(url=(callurl + '/abc'),
                               to='+13109612827',
                               from_='+19108124952')

    print(call.sid)

@app.route("/abc", methods=['GET', 'POST'])
def abc():
    userid3 = session.get('userid', None)
    chatid4 = session.get('userid', None)
    print(userid3)
    resp = VoiceResponse()
    resp.say(f"Your user id is {userid3}")
    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)