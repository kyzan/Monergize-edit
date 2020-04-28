from flask import Flask,render_template,url_for,flash,redirect,request
from flask_mysqldb import MySQL
from flask_login import LoginManager,login_user,current_user,logout_user,login_required
#from form import LoginForm, DebitForm, RegisterForm, Loan_enquiryForm, Bank_LoginForm, Search_customer, ADD_loan, submitbutton, Company_LoginForm, BankPrefForm, StockForm, PerformanceForm, MNCPayForm
from form import *
from load_data import *
#import load_data
import pygal


app = Flask(__name__ ,template_folder='templates' , static_folder='static')
app.config['SECRET_KEY'] = '5791628bpowerb0b13ce0c676dfde280ba245'

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='password'
app.config['MYSQL_DB']='bank'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'


@login_manager.user_loader
def load_user(id):
    if 'COMP' in id:return Company(id)
    if 'B' in id:return Bank(id)
    if len(id)==10:return User(id)
    return None

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegisterForm()
    if form.validate_on_submit():
        user_info = [form.name.data, form.email.data, form.houseno.data, form.sector.data, form.city.data, form.state.data, form.pin.data, form.age.data, form.gender.data, form.dob.data, form.father.data, form.mother.data]
        insert_user(user_info)
        flash('Your account has been created! You are now able to log in', 'success')
    return render_template('register.html', title='Register', form=form)

@app.route("/login/User", methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()

    if form.validate_on_submit():
        verify_user=Verify_user(form.email.data,form.password.data)
        if verify_user!=-1:
            if form.remember.data:login_user(User(verify_user), remember=True)
            else:login_user(User(verify_user),remember=False)
            next_page = request.args.get('next')
            flash('Logged in successfully', 'success')
            return redirect(next_page) if(next_page) else redirect(url_for('home'))
        else:flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template('sign_in.html', title='Login', form=form)

@app.route("/login/bank", methods=['GET', 'POST'])
def bank_login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = Bank_LoginForm()

    if form.validate_on_submit():
        verify_banker=Verify_banker(form.universal_id.data,form.bank_id.data,int(form.branch_id.data),form.password.data)
        if verify_banker!=-1:
            if form.remember.data:login_user(Bank(form.universal_id.data), remember=True)
            else:login_user(Bank(form.universal_id.data), remember=False)
            flash('Logged in successfully', 'success')
            return redirect(url_for('bank_home'))
        else:flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template('bank_sign_in.html', title='Login', form=form)
    
@app.route("/login/company", methods=['GET', 'POST'])
def company_login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = Company_LoginForm()

    if form.validate_on_submit():
        verify_comp=Verify_company(form.company_id.data,form.password.data)
        if verify_comp!=-1:
            if form.remember.data:login_user(Company(form.company_id.data), remember=True)
            else:login_user(Company(form.company_id.data), remember=False)
            flash('Logged in successfully', 'success')
            return redirect(url_for('company_home'))
        else:flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template('company_sign_in.html', title=' Corporate Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    user_data,bank_detail,employee_detail= request_User_detail(current_user.id)
    user_data=list(user_data.values())
    bank_detail=list(bank_detail.values())
    employee_detail=list(employee_detail.values())
    return render_template('account.html', title="Account",user_data=user_data,bank_detail=bank_detail,employee_detail=employee_detail)

@app.route("/debit", methods=['GET', 'POST'])
@login_required
def debit():
    form = DebitForm()
    curr_user_bank_detail=request_User_bank_detail(current_user.id)

    if form.validate_on_submit():
        if form.Account_number.data!=current_user.account_no and int(form.Pin.data)==current_user.PIN:
            if int(form.Amount.data)<current_user.balance:
                if Does_user_exist(form.Account_number.data):
                    amount=float(form.Amount.data)
                    make_transaction(current_user.account_no,form.Account_number.data,amount)
                    flash('Trasaction successful', 'success')
                    return redirect(url_for('home'))
                else:
                    flash('Please enter valid Account number','danger')
            else:
                flash('Amount Cannot be more than balance','danger')
        else :
            flash('Please check your account number and PIN code', 'danger')
    return render_template('debit.html', title='Debit', form=form, bank_detail=list(curr_user_bank_detail.values()))

@app.route("/summary")
@login_required
def summary():
    summary =  request_User_summary(current_user.id)

    data = []
    for entry in summary:
        data.append(list(entry.values()))

    return render_template('summary.html', 
                            title='Summary',
                            user_id=current_user.id,
                            user_name=current_user.name,
                            bank_detail=list(request_User_bank_detail(current_user.id).values()), 
                            summary=data)

@app.route("/loan_enquire", methods=['GET', 'POST'])
@login_required
def loan_enquire():
    form = Loan_enquiryForm()
    if form.validate_on_submit():
        loan_data,emi_data=enquire_loan(form.loan_type.data,form.principal.data,form.max_period.data)
        if loan_data!=False:
            return render_template('loan_enquire_result.html', title='Loan Enquiry', loan_data=loan_data, emi_data=emi_data,loop=range(len(loan_data)) , loan_type=form.loan_type.data, principal=int(form.principal.data))
        else:
            flash('No Loan available for your requirement','success')
    return render_template('loan_enquire.html', title='Loan Enquiry', form=form) 

@app.route("/bank/home")
@login_required
def bank_home():
    return render_template('bank_home.html', title='Bank_home', total_customer=len(request_customerlist(current_user.bank_id,0,'customer_id')), pending_loan=len(search_loan_application('PENDING',current_user.bank_id)))

@app.route("/bank/customer", methods=['GET', 'POST'])
@login_required
def print_customer_list():
    form = Search_customer()
    if form.validate_on_submit():
        column=form.query_type.data
        term=form.query.data
        data=request_customerlist(current_user.bank_id,term,column)
        if data==None or len(data)==0:
            return render_template('customer_list.html', title='Customer list', customer_list=[], record=False, many_recored=False, form=form)
        else:
            if len(data)==1:
                summary =  request_User_summary(data[0]['customer_id'])
                statements = []
                for entry in summary:
                    statements.append(list(entry.values()))
                return render_template('customer_list.html', title='Customer list', customer_list=data[0], record=True, many_recored=False, summary=statements,form=form)
            else:return render_template('customer_list.html', title='Customer list', customer_list=data, record=True, many_recored=True, form=form)
    customer_list=request_customerlist(current_user.bank_id,0,'customer_id')
    return render_template('customer_list.html', title='Customer list', customer_list=customer_list, record=True, many_recored=True, form=form)

@app.route("/bank/add_loan", methods=['GET', 'POST'])
@login_required
def add_loan():  
    current_loan=current_loan_in_database(current_user.bank_id,'0')
    form=ADD_loan()
    if form.validate_on_submit():
        insert_loan_in_database(current_user.bank_id,form.loan_type.data,form.interest.data,form.max_period.data)
        flash('New loan added into list','success')
        return redirect(url_for('bank_home'))
    return render_template('bank_add_loan.html',form=form, current_loan=current_loan)

@app.route("/bank/clear_loan", methods=['GET', 'POST'])
@login_required
def clear_loan():   
    applications = search_loan_application('PENDING',current_user.bank_id)
    if request.method=='POST':
        customer_list=request_customer_detail((request.form['submit']))
        print(customer_list)
        summary =  request_User_summary(customer_list['customer_id'])
        statements = []
        for entry in summary:
            statements.append(list(entry.values()))
        return render_template('customer_detail.html', customer_list=customer_list, summary=statements) 
    else:
        if type(applications)==int:
            return render_template('bank_loan_applications.html', hasdata=False)
        else:
            return render_template('bank_loan_applications.html', hasdata=True, current_loan=applications)

@app.route("/corporate/home", methods=['GET', 'POST'])
def company_home():
    return render_template('company_home.html',title='Home')

@app.route("/corporate/banks", methods=['GET', 'POST'])
def banks_performance():
    data =  bank_recc(0)
    form = BankPrefForm()
    if form.validate_on_submit():
        data = bank_recc(form.radio.data)
    statements = []
    for entry in data:
        statements.append(list(entry.values()))
    data=statements
    return render_template('Bank_performance.html', form=form, data=data)

@app.route("/corporate/stock", methods=['GET', 'POST'])
def stock_comparision():
    data = load_market_data('company_name')
    form = StockForm()
    if form.validate_on_submit():
        data = load_market_data('company_name')
        if(form.radio.data=='graph1'):
            return redirect(url_for('pe_bar'))
        elif(form.radio.data=='graph2'):
            return redirect(url_for('eps_bar'))

        else:
            data = load_market_data(form.radio.data)
            statements = []
            for entry in data:
                statements.append(list(entry.values()))
                data=statements
            return render_template('stock_performance.html', form=form, data=data)

    return render_template('stock_performance.html', form=form, data=data)

@app.route('/pe_bar', methods=['GET', 'POST'])
def pe_bar():
    data=load_market_data('company_name')
    #print(data)
    bar_labels=[]
    bar_values=[]
    for j in data:
        bar_labels.append(j['company_name'])
        bar_values.append(j['pe_ratio'])
    

    chart = pygal.Bar(width=1200, height=700,spacing=100,explicit_size=True)
    chart.title='Price-to-Earnings Ratio Comparison'
    
    for i in range(len(bar_labels)):
        chart.add(bar_labels[i],(bar_values[i]))
    chart.render_in_browser()
    #chart_data = chart.render_data_uri()
    return redirect(url_for('stock_comparision'))

@app.route('/eps_bar', methods=['GET', 'POST'])
def eps_bar():
    data=load_market_data('company_name')
    #print(data)
    bar_labels=[]
    bar_values=[]
    for j in data:
        bar_labels.append(j['company_name'])
        bar_values.append(j['eps'])
    chart = pygal.Bar(width=1200, height=700,spacing=100,explicit_size=True)
    chart.title='Earnings-per-Share Ratio Comparison'
    for i in range(len(bar_labels)):
        chart.add(bar_labels[i],(bar_values[i]))
    chart.render_in_browser()
    return redirect(url_for('stock_comparision'))

@app.route("/corporate/perform", methods=['GET', 'POST'])
def company_performance():
    data0 = (('NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA'),)
    data = (('NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA'),)
    data1 = (('NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA','NA'),)
    data2 = (('NA','NA'),)
    form = PerformanceForm()
    if form.validate_on_submit():
        data0 =  own_market_data(form.id.data)
        data = best_company()
        data1 =  better_company(form.id.data)
        data2 =  rev_by_category()
    return render_template('corporate_performance.html', form=form, data=data, data1=data1, data2 = data2, data0=data0)

@app.route("/coporate/mnc/pay", methods=['GET', 'POST'])
def mnc_pay():
    data = (('NA','NA','NA','NA','NA','NA','NA'),)
    data1 = (('NA','NA','NA','NA','NA','NA','NA','NA'),)
    data2 = (('NA',),)
    form = MNCPayForm()
    if form.validate_on_submit():
        data = load_employee_data(form.id.data)
        data1 =  load_su_data()
        data2 =  custom_duty(form.id.data)
    return render_template('mnc_payment.html', form=form, data=data, data1=data1, data2 = data2, title='MNC Payment')

@app.route("/coporate/payment", methods=['GET', 'POST'])
def corporate_payment():
    form = PaymentForm()
    if form.validate_on_submit():
        id = form.id.data
        amount = form.amount.data
        radio = form.radio.data
        add_amount(id,amount,radio)
        flash("amount: "+amount+" transferred to "+radio+" "+id+" successfully "+' Transaction ID: 123456789')
    return render_template('corporate_payment.html', form=form, title='Corporate payments')

@app.route("/corporate/ekart", methods=['GET', 'POST'])
def ekart():
    data = load_products(0)
    form = EKartForm()
    if form.validate_on_submit():
        data =load_products(form.radio.data)
    return render_template('corporate_ekart.html', form=form, data=data)

@app.route('/reg_wsu', methods=['GET', 'POST'])
def reg_wsu():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegisterForm()
    if form.validate_on_submit():
        user_info = {'name': form.name.data, 'email': form.email.data,'houseno': form.houseno.data,'sector': form.sector.data,'city': form.city.data,'state': form.state.data,'pin': form.pin.data,'age': form.age.data,'gender': form.gender.data,'dob': form.dob.data,'father': form.father.data,'mother': form.mother.data, 'password': form.password.data, 'account_no':form.account_no.data,'bank_id': form.bank_id.data, 'account_balance': form.account_balance.data, 'set_pin': form.set_pin.data, 'govt_id': form.govt_id.data, 'profession': form.profession.data, 'contact_no': form.contact_no.data, 'branch_id': form.branch_id.data, 'fixed_deposit': form.fixed_deposit.data, 'salary': form.salary.data, 'username': form.username.data, 'tax_bracket': form.tax_bracket.data, 'loan_emi': form.loan_emi.data, 'aco': form.aco.data}
        print(user_info)
        insert_user(user_info)
        flash('Your account has been created! You are now able to log in', 'success')
    print(form.errors)
    return render_template('register.html', title="Web Service User", form=form)

@app.route('/reg_com', methods=['GET', 'POST'])
def reg_com():
    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))

    form = RegComForm()
    if form.validate_on_submit():
        print(hello)
        user_info = {'name': form.name.data, 'type': form.type.data, 'bank_partner': form.bank_partner.data, 'bank_branch': form.bank_branch.data, 'acc_no': form.acc_no.data, 'ifsc_code': form.ifsc_code.data, 'nature_of_biz': form.nature_of_biz.data, 'contact_no': form.contact_no.data, 'tax_bracket': form.tax_bracket.data, 'doe': form.doe.data, 'type_of_acc': form.type_of_acc.data, 'loan_amount': form.loan_amount.data, 'loan_period': form.loan_period.data, 'fd': form.fd.data, 'int_rate': form.int_rate.data, 'branches_in_india': form.branches_in_india.data, 'importers_id': form.importers_id.data, 'raw_material': form.raw_material.data, 'finished_product': form.finished_product.data, 'custom_duty': form.custom_duty.data, 'relaxation_limit': form.relaxation_limit.data, 'gst': form.gst.data, 'pe_ratio': form.pe_ratio.data, 'quick_ratio': form.quick_ratio.data, 'acc_payable': form.acc_payable.data, 'acc_receivable': form.acc_receivable.data, 'eps': form.eps.data, 'market_value': form.market_value.data, 'book_value': form.book_value.data, 'total_assets': form.total_assets.data, 'total_liabilities': form.total_liabilities.data, 'inventories': form.inventories.data, 'external_fundings': form.external_fundings.data, 'retained_earnings': form.retained_earnings.data, 'product_id ': form.product_id .data, 'product_name': form.product_name.data, 'email': form.email.data, 'password': form.password.data}
        print(user_info)
        # load_data.insert_company(user_info)
        flash('Your account has been created! You are now able to log in', 'success')
    print(form.errors)
    return render_template('regcom.html', title="Company", form=form)

@app.route('/reg_emp', methods=['GET', 'POST'])
def reg_emp():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegEmpForm()
    if form.validate_on_submit():
        user_info = {'cust_id': form.cust_id.data, 'comp_id': form.comp_id.data, 'sector': form.sector.data, 'product_type': form.product_type.data, 'company_name': form.company_name.data, 'working_from': form.working_from.data, 'working_till': form.working_till.data, 'email': form.email.data, 'password': form.password.data}
        print(user_info)
        #load_data.insert_user(user_info)
        flash('Your account has been created! You are now able to log in', 'success')
    return render_template('regemp.html', title="Web Service User", form=form)

@app.route('/reg_bank', methods=['GET', 'POST'])
def reg_bank():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegBankForm()
    if form.validate_on_submit():
        user_info = {'name': form.name.data, 'branch_id': form.branch_id.data, 'branch_name': form.branch_name.data, 'contact': form.contact.data, 'no_cust': form.no_cust.data, 'total_assets': form.total_assets.data, 'ROI_for_loans': form.ROI_for_loans.data, 'ROI_for_savings': form.ROI_for_savings.data, 'ROI_for_current': form.ROI_for_current.data, 'no_fds': form.no_fds.data, 'min_bal': form.min_bal.data, 'ann_govt': form.ann_govt.data, 'loan_taken': form.loan_taken.data, 'money_lent': form.money_lent.data, 'email': form.email.data, 'password': form.password.data}
        #load_data.insert_user(user_info)
        flash('Your account has been created! You are now able to log in', 'success')
    return render_template('regbank.html', title="Web Service User", form=form)

@app.route('/reg_sup', methods=['GET', 'POST'])
def reg_sup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegSupForm()
    if form.validate_on_submit():
        user_info = {'su_name': form.su_name.data, 'account_id': form.account_id.data, 'date_val': form.date_val.data, 'date_created': form.date_created.data, 'bank_balance': form.bank_balance.data, 'sales_type': form.sales_type.data, 'email': form.email.data, 'registered_photo': form.registered_photo.data, 'linked_acc': form.linked_acc.data, 'state': form.state.data, 'size': form.size.data, 'tax_owed': form.tax_owed.data, 'source_id': form.source_id.data, 'value': form.value.data, 'interest': form.interest.data, 'product_id': form.product_id.data, 'product_name': form.product_name.data, 'category': form.category.data, 'price': form.price.data, 'sold': form.sold.data, 'password': form.password.data}
        load_data.insert_user(user_info)
        flash('Your account has been created! You are now able to log in', 'success')
    return render_template('regsup.html', title="Web Service User", form=form)

if __name__ == '__main__':
    app.run(debug=True)
