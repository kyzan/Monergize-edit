from Main import mysql,app
from flask_login import UserMixin
import itertools

with app.app_context():
    ###### User details
    cur = mysql.connection.cursor()

    cur.execute("SELECT Customer_id FROM bank.customer_login_detail;")
    dbcustomer_id = list(map(lambda x: x[0], (cur.fetchall())))

    cur.execute("SELECT email FROM bank.customer_login_detail;")
    dbemails = list(map(lambda x: x[0], (cur.fetchall())))

    cur.execute("SELECT password FROM bank.customer_login_detail;")
    dbpasswords = list(map(lambda x: x[0], (cur.fetchall())))

    cur.close()
    #######

#This is for user class
class User(UserMixin):

    def __repr__(self):
        return f"User('{self.id}', '{self.email}', '{self.password}', '{self.name}')"

    def __init__(self, id):
        self.id = id
        self.email = dbemails[dbcustomer_id.index(int(id))]
        all_user_data = request_User_detail_small(id)
        self.name = all_user_data[1]

def request_User_detail(id):
    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM bank.customer_personal_detail WHERE Customer_id = %s;",[int(id),])
    user_info = ((cur.fetchall()))

    cur.execute("SELECT * FROM bank.customer_bank_details WHERE customer_id = %s;",[int(id)])
    bank_detail = (cur.fetchall())

    cur.execute("SELECT * FROM bank.customer_employment_details WHERE Customer_id = %s;",[int(id)])
    employee_detail = (cur.fetchall())

    cur.close()

    user_info=list(itertools.chain(*user_info))
    bank_detail=list(itertools.chain(*bank_detail))
    employee_detail=list(itertools.chain(*employee_detail))

    return user_info,bank_detail,employee_detail

def request_User_detail_small(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM bank.customer_personal_detail WHERE Customer_id = %s;",[int(id),])
    user_info = ((cur.fetchall()))
    user_info=list(itertools.chain(*user_info))
    return user_info

def request_User_bank_detail(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT bank_id,bank_name,account_no,account_balance,account_pin FROM bank.customer_bank_details WHERE Customer_id = %s;",[int(id)])
    bank_detail = (cur.fetchall())
    bank_detail=list(itertools.chain(*bank_detail))
    return bank_detail

def Does_user_exist(acc_no):
    cur = mysql.connection.cursor()
    cur.execute("SELECT bank_id,account_no,account_balance,account_pin FROM bank.customer_bank_details WHERE Customer_id = %s;",[(acc_no)])
    bank_detail = (cur.fetchall())
    if (len(bank_detail)>0):return True
    else: return False
    

def request_User_summary(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM bank.customer_account_summary WHERE Customer_id = %s;",[int(id)])
    user_summary = list(map(list,cur.fetchall()))
    return user_summary


def insert_user(user_detail):
    cur = mysql.connection.cursor()
    cur.execute("SELECT MAX(CUSTOMER_ID) FROM bank.customer_personal_detail")
    id_val = map(lambda x: x[0], (cur.fetchall()))
    id_val = str(list(id_val)[0]+1)
    cur.execute("INSERT INTO bank.customer_personal_detail VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", [id_val, user_detail[0], user_detail[1], user_detail[2], user_detail[3], user_detail[4], user_detail[5], user_detail[6], user_detail[7], user_detail[8], user_detail[9], user_detail[10], user_detail[11]])
    mysql.connection.commit()
    cur.close()

def load_market_data(para):
    if para =="pe_ratio":
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM bank.company_market_detail ORDER BY pe_ratio")
        data = cur.fetchall()
        mysql.connection.commit()
        cur.close()
    if para =="market_value":
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM bank.company_market_detail ORDER BY market_value")
        data = cur.fetchall()
        mysql.connection.commit()
        cur.close()
    if para =="company_name":
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM bank.company_market_detail ORDER BY company_name")
        data = cur.fetchall()
        mysql.connection.commit()
        cur.close()

    return data