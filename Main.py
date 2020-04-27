from flask import Flask,render_template,url_for,flash,redirect,request
from flask_mysqldb import MySQL
from flask_login import LoginManager,login_user,current_user,logout_user,login_required
from form import LoginForm, DebitForm, RegisterForm, StockForm, RegComForm, RegBankForm, RegEmpForm, RegSupForm, MNCPayForm, PaymentForm, EKartForm, PerformanceForm, BankPrefForm
from load_data import *
import load_data


app = Flask(__name__ ,template_folder='templates' , static_folder='static')
app.config['SECRET_KEY'] = '5791628bpowerb0b13ce0c676dfde280ba245'

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='password'
app.config['MYSQL_DB']='bank'

mysql = MySQL(app)

login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route("/")
def hello():
    return render_template('Main_home.html',title="Home page")

@app.route("/home")
def home():
    return render_template('home.html',title="Home page 2")

@app.route("/about")
def about():
    return render_template('about.html',title="About")

@app.route("/register", methods=['GET', 'POST'])
def register():
    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))

    # form = RegisterForm()
    # if form.validate_on_submit():
    #     user_info = [form.name.data, form.email.data, form.houseno.data, form.sector.data, form.city.data, form.state.data, form.pin.data, form.age.data, form.gender.data, form.dob.data, form.father.data, form.mother.data]
    #     load_data.insert_user(user_info)
    #     flash('Your account has been created! You are now able to log in', 'success')
    return render_template('regdesk.html', title='Register')

@app.route("/stock", methods=['GET', 'POST'])
def stock():
    data = load_data.load_market_data('pe_ratio')
    form = StockForm()
    if form.validate_on_submit():
        data =load_data.load_market_data(form.type.data)

    return render_template('stock_market.html', form=form, data=data)

@app.route("/login", methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()

    if form.validate_on_submit():
        if form.email.data in load_data.dbemails and load_data.dbpasswords[load_data.dbemails.index(form.email.data)]==form.password.data:
            login_user(User(load_data.dbcustomer_id[load_data.dbemails.index(form.email.data)]), remember=True)
            next_page = request.args.get('next')
            flash('Logged in successfully', 'success')
            return redirect(next_page) if(next_page) else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template('sign_up.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    user_data,bank_detail,employee_detail=load_data.request_User_detail(current_user.id)
    return render_template('account.html', title="Account",user_data=user_data,bank_detail=bank_detail,employee_detail=employee_detail)

@app.route("/debit", methods=['GET', 'POST'])
@login_required
def debit():
    form = DebitForm()
    curr_user_bank_detail=request_User_bank_detail(current_user.id)

    if form.validate_on_submit():
        if form.Account_number.data!=curr_user_bank_detail[2] and Does_user_exist(form.Account_number.data):
            print("Transaction successful")
            return redirect(url_for('home'))
        else :
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('debit.html', title='Debit', form=form, bank_detail=curr_user_bank_detail)

@app.route("/summary")
@login_required
def summary():
    summary = load_data.request_User_summary(current_user.id)
    return render_template('summary.html', 
                            title='Summary',
                            user_id=current_user.id,
                            user_name=current_user.name,
                            bank_detail=load_data.request_User_bank_detail(current_user.id), 
                            summary=summary)

@app.route('/reg_wsu', methods=['GET', 'POST'])
def reg_wsu():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegisterForm()
    if form.validate_on_submit():
        user_info = {'name': form.name.data, 'email': form.email.data,'houseno': form.houseno.data,'sector': form.sector.data,'city': form.city.data,'state': form.state.data,'pin': form.pin.data,'age': form.age.data,'gender': form.gender.data,'dob': form.dob.data,'father': form.father.data,'mother': form.mother.data, 'password': form.password.data}
        load_data.insert_user(user_info)
        flash('Your account has been created! You are now able to log in', 'success')
    return render_template('register.html', title="Web Service User", form=form)

@app.route('/reg_com', methods=['GET', 'POST'])
def reg_com():
    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))

    form = RegComForm()
    if form.validate_on_submit():
        user_data = {'name': form.name.data, 'type': form.type.data, 'bank_partner': form.bank_partner.data, 'bank_branch': form.bank_branch.data, 'acc_no': form.acc_no.data, 'ifsc_code': form.ifsc_code.data, 'nature_of_biz': form.nature_of_biz.data, 'contact_no': form.contact_no.data, 'tax_bracket': form.tax_bracket.data, 'doe': form.doe.data, 'type_of_acc': form.type_of_acc.data, 'loan_amount': form.loan_amount.data, 'loan_period': form.loan_period.data, 'fd': form.fd.data, 'int_rate': form.int_rate.data, 'branches_in_india': form.branches_in_india.data, 'importers_id': form.importers_id.data, 'raw_material': form.raw_material.data, 'finished_product': form.finished_product.data, 'custom_duty': form.custom_duty.data, 'relaxation_limit': form.relaxation_limit.data, 'gst': form.gst.data, 'pe_ratio': form.pe_ratio.data, 'quick_ratio': form.quick_ratio.data, 'acc_payable': form.acc_payable.data, 'acc_receivable': form.acc_receivable.data, 'eps': form.eps.data, 'market_value': form.market_value.data, 'book_value': form.book_value.data, 'total_assets': form.total_assets.data, 'total_liabilities': form.total_liabilities.data, 'inventories': form.inventories.data, 'external_fundings': form.external_fundings.data, 'retained_earnings': form.retained_earnings.data, 'product_id ': form.product_id .data, 'product_name': form.product_name.data, 'email': form.email.data, 'password': form.password.data}
        print(user_data)
        # load_data.insert_company(user_info)
        flash('Your account has been created! You are now able to log in', 'success')
    return render_template('regcom.html', title="Company", form=form)

@app.route('/reg_emp', methods=['GET', 'POST'])
def reg_emp():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegEmpForm()
    # if form.validate_on_submit():
    #     user_info = {'name': form.name.data, 'email': form.email.data,'houseno': form.houseno.data,'sector': form.sector.data,'city': form.city.data,'state': form.state.data,'pin': form.pin.data,'age': form.age.data,'gender': form.gender.data,'dob': form.dob.data,'father': form.father.data,'mother': form.mother.data, 'password': form.password.data}
    #     load_data.insert_user(user_info)
    #     flash('Your account has been created! You are now able to log in', 'success')
    return render_template('regemp.html', title="Web Service User", form=form)

@app.route('/reg_bank', methods=['GET', 'POST'])
def reg_bank():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegBankForm()
    # if form.validate_on_submit():
    #     user_info = {'name': form.name.data, 'email': form.email.data,'houseno': form.houseno.data,'sector': form.sector.data,'city': form.city.data,'state': form.state.data,'pin': form.pin.data,'age': form.age.data,'gender': form.gender.data,'dob': form.dob.data,'father': form.father.data,'mother': form.mother.data, 'password': form.password.data}
    #     load_data.insert_user(user_info)
    #     flash('Your account has been created! You are now able to log in', 'success')
    return render_template('regbank.html', title="Web Service User", form=form)

@app.route('/reg_sup', methods=['GET', 'POST'])
def reg_sup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegSupForm()
    # if form.validate_on_submit():
    #     user_info = {'name': form.name.data, 'email': form.email.data,'houseno': form.houseno.data,'sector': form.sector.data,'city': form.city.data,'state': form.state.data,'pin': form.pin.data,'age': form.age.data,'gender': form.gender.data,'dob': form.dob.data,'father': form.father.data,'mother': form.mother.data, 'password': form.password.data}
    #     load_data.insert_user(user_info)
    #     flash('Your account has been created! You are now able to log in', 'success')
    return render_template('regsup.html', title="Web Service User", form=form)

@app.route("/mnc_pay", methods=['GET', 'POST'])
def mnc_pay():
    data = (('NA','NA','NA','NA','NA','NA','NA'),)
    data1 = (('NA','NA','NA','NA','NA','NA','NA','NA'),)
    data2 = (('NA',),)
    form = MNCPayForm()
    if form.validate_on_submit():
        data =load_data.load_employee_data(form.id.data)
        data1 = load_data.load_su_data()
        data2 = load_data.custom_duty(form.id.data)
    return render_template('mnc_pay.html', form=form, data=data, data1=data1, data2 = data2)

@app.route("/payment", methods=['GET', 'POST'])
def payment():
    form = PaymentForm()
    if form.validate_on_submit():
        id = form.id.data
        amount = form.amount.data
        radio = form.radio.data
        load_data.add_amount(id,amount,radio)
        flash("amount: "+amount+" transferred to "+radio+" "+id+" successfully "+' Transaction ID: 123456789')
    return render_template('payment.html', form=form)

@app.route("/ekart", methods=['GET', 'POST'])
def ekart():
    data = load_data.load_products(0)
    form = EKartForm()
    if form.validate_on_submit():
        data =load_data.load_products(form.radio.data)

    return render_template('ekart.html', form=form, data=data)

@app.route("/perform", methods=['GET', 'POST'])
def perform():
    data0 = (('NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA'),)
    data = (('NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA'),)
    data1 = (('NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA'),)
    data2 = (('NA','NA'),)
    form = PerformanceForm()
    if form.validate_on_submit():
        data0 = load_data.own_market_data(form.id.data)
        data =load_data.best_company()
        data1 = load_data.better_company(form.id.data)
        data2 = load_data.rev_by_category()
    return render_template('perform.html', form=form, data=data, data1=data1, data2 = data2, data0=data0)

@app.route("/banks", methods=['GET', 'POST'])
def banks():
    data = load_data.bank_recc(0)

    form = BankPrefForm()
    if form.validate_on_submit():
        data = bank_recc(form.radio.data)
    return render_template('bank_recc.html', form=form, data=data)

if __name__ == '__main__':
    app.run(debug=True)

