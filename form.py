from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, IntegerField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp, Required


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=50)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    houseno = StringField('House_no', validators=[DataRequired(), Length(min=1, max=50)])
    sector= StringField('Sector', validators=[DataRequired(), Length(min=3, max=20)])
    city = StringField('City', validators=[DataRequired(), Length(min=3, max=50)])
    state = StringField('State', validators=[DataRequired(), Length(min=3, max=20)])
    pin = StringField('PinCode', validators=[DataRequired(), Length(min=6, max=6)])
    age = StringField('Age', validators=[DataRequired(), Regexp(regex=r'^[2-9][0-9]$|^1[0-9][0-9]$',message="Person above 19 age is allowed")])
    gender = StringField('Gender', validators=[DataRequired(), Regexp(regex=r'^[MFO]$',message="Valid inputs are 'M' for male 'F' for female or 'O' for others")])
    dob = StringField('Date Of Birth', validators=[DataRequired(), Required()])
    father = StringField('Fathers Name', validators=[DataRequired(), Length(min=3, max=20)])
    mother = StringField('Mothers Name', validators=[DataRequired(), Length(min=3, max=20)])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class Bank_LoginForm(FlaskForm):
    universal_id = StringField('Universal ID', validators=[DataRequired(), Length(min=3, max=5)])
    bank_id = StringField('BANK ID',validators=[DataRequired(), Regexp(regex=r'^BANK\d{6}$',message="Bank ID should be in the form of BANK100001")])
    branch_id = StringField('Branch ID',validators=[DataRequired(), Length(min=6,max=6)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=3,max=45)])
    remember = BooleanField('Remember Me', default="unchecked")
    submit = SubmitField('Login')

class Company_LoginForm(FlaskForm):
    company_id = StringField('Company ID',validators=[DataRequired(), Regexp(regex=r'^COMP\d{6}$',message="Company ID should be in the form of COMP100001")])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=3,max=45)])
    remember = BooleanField('Remember Me', default="unchecked")
    submit = SubmitField('Login')

class DebitForm(FlaskForm):
    Account_number = StringField('Account Number', validators=[Regexp(regex=r'^ACC-\d{3}$',message="Example Account number ACC-101")])
    Pin = StringField('Pin Number', validators=[Length(min=4, max=4)])
    Amount = StringField('Amount', validators=[Length(min=0, max=15)])
    submit = SubmitField('Transfer')

class Loan_enquiryForm(FlaskForm):
    principal = IntegerField('Loan Amount')
    max_period = IntegerField('Period (Enter in months)')
    loan_type = SelectField('Type', choices=[('Car','Car'),('Home','Home'),('Business','Business'),('Personal','Personal'),('Extra','Extra')])
    submit = SubmitField('Enquire')

class Search_customer(FlaskForm):
    query = StringField('',validators=[Length(min=3)])
    query_type = SelectField('Type', choices=[('customer_id','ID'),('name','Name'),('email','Email'),('account_no','Account Number')])
    submit = SubmitField('Search')

class ADD_loan(FlaskForm):
    loan_type = SelectField('Type', choices=[('Car','Car'),('Home','Home'),('Business','Business'),('Personal','Personal'),('Extra','Extra')])
    interest = IntegerField('Interest in percentage')
    max_period = IntegerField('Period (Enter in months)')
    submit = SubmitField('Add Loan')

class submitbutton(FlaskForm):
    submit = SubmitField('Submit')

class BankPrefForm(FlaskForm):
    radio = RadioField('Parameters', choices=[('Most Trusted','Most Trusted'),('Loan Friendly','Loan Friendly'),('Best for Savings','Best for Savings'),('Least Minimum Account Balance','Least Minimum Account Balance'),('graph','Show Graphical Analysis')])
    submit = SubmitField('Search')

class StockForm(FlaskForm):
    radio = RadioField('Sort using:', choices = [('pe_ratio','Profit'),('market_value','Price'),('company_name','Name'),('graph1','Show PE Analysis'),('graph2','Show EPS Analysis')])
    submit = SubmitField('Search')

class PerformanceForm(FlaskForm):
    id = StringField('Company ID')
    radio = RadioField('',choices=[('graph','Show Graphical Analysis')])
    submit = SubmitField('Submit')

class MNCPayForm(FlaskForm):
    id = StringField('Company ID')
    submit = SubmitField('Submit')

class PaymentForm(FlaskForm):
    id = StringField('Recipients ID')
    amount = StringField('Amount')
    radio = RadioField('Choose', choices=[('Employee','Employee'),('Start Ups','Start Ups')])
    cid = StringField('Your ID')
    pin = PasswordField('PIN')
    submit = SubmitField('CONFIRM')

class EKartForm(FlaskForm):
    radio = RadioField('Filters', choices=[('Health','Health'),('Fashion','Fashion'),('Books','Books'),('Electronics','Electronics'),('Best Sellers','Best Sellers'),('Lowest Prices','Lowest Prices'),('graph','Show Graphical Analysis')])
    submit = SubmitField('Find the right item!')

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=50)])
    email = StringField('Email',validators=[DataRequired(), Email()])
    houseno = StringField('House_no', validators=[DataRequired(), Length(min=1, max=50)])
    sector= StringField('Sector', validators=[DataRequired(), Length(min=3, max=20)])
    city = StringField('City', validators=[DataRequired(), Length(min=3, max=50)])
    state = StringField('State', validators=[DataRequired(), Length(min=3, max=20)])
    pin = StringField('PinCode', validators=[DataRequired(), Length(min=6, max=6)])
    age = StringField('Age', validators=[DataRequired(), Regexp(regex=r'^[2-9][0-9]$|^1[0-9][0-9]$',message="Person above 19 age is allowed")])
    gender = StringField('Gender', validators=[DataRequired(), Regexp(regex=r'^[MFO]$',message="Valid inputs are 'M' for male 'F' for female or 'O' for others")])
    dob = StringField('Date Of Birth', validators=[DataRequired(), Required()])
    father = StringField('Fathers Name', validators=[DataRequired(), Length(min=3, max=20)])
    mother = StringField('Mothers Name', validators=[DataRequired(), Length(min=3, max=20)])

    account_no = StringField('Account Number')
    bank_id = StringField('Bank ID', validators=[DataRequired(), Length(min=3, max=20)])
    account_balance = StringField('First Deposit', validators=[DataRequired(), Length(min=3, max=20)])
    account_type = StringField('Account type', validators=[DataRequired(), Length(min=3, max=20)])
    set_pin = PasswordField('Set Pin', validators=[DataRequired(), Length(min=3, max=20)])

    govt_id = StringField('Aadhar Number', validators=[DataRequired(), Length(min=3, max=20)])
    profession = StringField('Profession', validators=[DataRequired(), Length(min=3, max=20)])
    contact_no = StringField('Contact', validators=[DataRequired(), Length(min=3, max=20)])
    branch_id = StringField('Branch ID', validators=[DataRequired(), Length(min=3, max=20)])
    fixed_deposit = StringField('FD Amount', validators=[DataRequired(), Length(min=3, max=20)])
    salary = StringField('Salary', validators=[DataRequired(), Length(min=3, max=20)])
    username = StringField('username', validators=[DataRequired(), Length(min=3, max=20)])
    tax_bracket = StringField('Tax Bracket', validators=[DataRequired(), Length(min=3, max=20)])
    loan_emi = StringField('Loan', validators=[DataRequired(), Length(min=3, max=20)])
    aco = StringField('Account Opening Date', validators=[DataRequired(), Length(min=3, max=20)])

    password = PasswordField('Password', validators=[DataRequired(), Length(min=3, max=20)])
    submit = SubmitField('Register')

class RegComForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=20)])
    type = StringField('Company Type', validators=[DataRequired(), Length(min=3, max=20)])
    bank_partner = StringField('Bank Partner', validators=[DataRequired(), Length(min=3, max=20)])
    bank_branch = StringField('Bank Branch', validators=[DataRequired(), Length(min=3, max=20)])
    acc_no = StringField('Account Number', validators=[DataRequired(), Length(min=3, max=20)])
    ifsc_code = StringField('IFSC', validators=[DataRequired(), Length(min=3, max=20)])
    nature_of_biz = StringField('Nature of Business', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    contact_no =  StringField('Contact Number', validators=[DataRequired(), Length(min=3, max=20)])
    tax_bracket = StringField('Tax Bracket', validators=[DataRequired(), Length(min=3, max=20)])
    doe = StringField('Date of Establishment', validators=[DataRequired(), Length(min=3, max=20)])
    type_of_acc = StringField('Type Of Account', validators=[DataRequired(), Length(min=3, max=20)])
    loan_amount = StringField('Loan Amount', validators=[DataRequired(), Length(min=3, max=20)])
    loan_period = StringField('Loan Period', validators=[DataRequired(), Length(min=3, max=20)])
    fd = StringField('FD', validators=[DataRequired(), Length(min=3, max=20)])
    int_rate = StringField('Interest Rate', validators=[DataRequired(), Length(min=3, max=20)])

    branches_in_india = StringField('Branches In India', validators=[DataRequired(), Length(min=3, max=20)])
    importers_id = StringField('Importer', validators=[DataRequired(), Length(min=3, max=20)])
    raw_material = StringField('Raw Material', validators=[DataRequired(), Length(min=3, max=20)])
    finished_product = StringField('Finished Product', validators=[DataRequired(), Length(min=3, max=20)])
    custom_duty = StringField('Custom Duty', validators=[DataRequired(), Length(min=3, max=20)])
    relaxation_limit = StringField('Relaxation Limit', validators=[DataRequired(), Length(min=3, max=20)])
    gst = StringField('GST', validators=[DataRequired(), Length(min=3, max=20)])

    pe_ratio = StringField('PE Ratio', validators=[DataRequired(), Length(min=3, max=20)])
    quick_ratio = StringField('Quick Ratio', validators=[DataRequired(), Length(min=3, max=20)])
    acc_payable = StringField('Account Payable', validators=[DataRequired(), Length(min=3, max=20)])
    acc_receivable = StringField('Account Receivable', validators=[DataRequired(), Length(min=3, max=20)])
    eps = StringField('Earning Per Share', validators=[DataRequired(), Length(min=3, max=20)])
    market_value = StringField('Market Value', validators=[DataRequired(), Length(min=3, max=20)])
    book_value = StringField('Book Value', validators=[DataRequired(), Length(min=3, max=20)])
    total_assets  = StringField('total_assets', validators=[DataRequired(), Length(min=3, max=20)])
    total_liabilities = StringField('total_liabilities', validators=[DataRequired(), Length(min=3, max=20)])
    inventories = StringField('Inventories', validators=[DataRequired(), Length(min=3, max=20)])
    external_fundings = StringField('External Fundings', validators=[DataRequired(), Length(min=3, max=20)])
    retained_earnings = StringField('Retained Earnings', validators=[DataRequired(), Length(min=3, max=20)])

    product_id = StringField('Product ID', validators=[DataRequired(), Length(min=3, max=20)])
    product_name = StringField('Product Name', validators=[DataRequired(), Length(min=3, max=20)])
    category = StringField('Category')
    price = StringField('Price')
    sold = StringField('Items Sold')

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=3, max=20)])
    submit = SubmitField('Register')


class RegEmpForm(FlaskForm):
    cust_id = StringField('Customer ID', validators=[DataRequired(), Length(min=3, max=20)])
    comp_id = StringField('Company ID', validators=[DataRequired(), Length(min=3, max=20)])
    sector = StringField('Sector', validators=[DataRequired(), Length(min=3, max=20)])
    product_type = StringField('Product Type', validators=[DataRequired(), Length(min=3, max=20)])
    company_name = StringField('Company Name', validators=[DataRequired(), Length(min=3, max=20)])
    working_from = StringField('Working From', validators=[DataRequired(), Length(min=3, max=20)])
    working_till = StringField('Working Till', validators=[DataRequired(), Length(min=3, max=20)])

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=3, max=20)])
    submit = SubmitField('Register')


class RegSupForm(FlaskForm):
    su_name = StringField('StartUp Name', validators=[DataRequired(), Length(min=3, max=20)])
    account_id = StringField('Account ID', validators=[DataRequired(), Length(min=3, max=20)])
    date_val = StringField('Date Till Account Valid', validators=[DataRequired(), Length(min=3, max=20)])
    date_val = StringField('Date Till Account Valid', validators=[DataRequired(), Length(min=3, max=20)])
    date_created = StringField('Date Created', validators=[DataRequired(), Length(min=3, max=20)])
    bank_balance = StringField('Bank Balance', validators=[DataRequired(), Length(min=3, max=20)])
    sales_type = StringField('Sales Type', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    registered_photo = StringField('Type Confirm', validators=[DataRequired(), Length(min=3, max=20)])
    linked_acc = StringField('Account Number', validators=[DataRequired(), Length(min=3, max=20)])
    state = StringField('Location(State)', validators=[DataRequired(), Length(min=3, max=20)])
    size = StringField('Size', validators=[DataRequired(), Length(min=3, max=20)])
    tax_owed = StringField('Tax', validators=[DataRequired(), Length(min=3, max=20)]) 

    source_id = StringField('Funding Company ID', validators=[DataRequired(), Length(min=3, max=20)])
    value = StringField('Fund Value', validators=[DataRequired(), Length(min=3, max=20)])
    interest = StringField('Interest', validators=[DataRequired(), Length(min=3, max=20)])

    product_id = StringField('Product ID', validators=[DataRequired(), Length(min=3, max=20)])
    product_name = StringField('Product Name', validators=[DataRequired(), Length(min=3, max=20)])
    category = StringField('Category')
    price = StringField('Price')
    sold = StringField('Items Sold')

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=3, max=20)])
    submit = SubmitField('Register')

class RegBankForm(FlaskForm):
    name = StringField('Bank Name', validators=[DataRequired(), Length(min=3, max=20)])
    branch_id = StringField('Branch ID', validators=[DataRequired(), Length(min=3, max=20)])
    branch_name = StringField('Branch Name', validators=[DataRequired(), Length(min=3, max=20)])
    contact = StringField('Contact', validators=[DataRequired(), Length(min=3, max=20)])
    no_cust = StringField('Number of Customer', validators=[DataRequired(), Length(min=1, max=20)])
    total_assets = StringField('Number of Assets', validators=[DataRequired(), Length(min=3, max=20)])
    ROI_for_loans = StringField('ROI Loans', validators=[DataRequired(), Length(min=1, max=20)])
    ROI_for_savings = StringField('ROI Savings', validators=[DataRequired(), Length(min=1, max=20)])
    ROI_for_current = StringField('ROI Current', validators=[DataRequired(), Length(min=1, max=20)])
    no_fds = StringField('Number of FDs', validators=[DataRequired(), Length(min=1, max=20)])
    min_bal = StringField('Minimum Account Balance', validators=[DataRequired(), Length(min=1, max=20)])
    ann_govt = StringField('Annual Share Govt', validators=[DataRequired(), Length(min=1, max=20)])
    loan_taken = StringField('Loan Taken', validators=[DataRequired(), Length(min=1, max=20)])
    money_lent = StringField('Money LENT', validators=[DataRequired(), Length(min=1, max=20)])

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=3, max=20)])
    submit = SubmitField('Register')

class InvestForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    profession = StringField('Occupation', validators=[])
    profit = RadioField('How much return do you want?',choices=[('H','High'),('M','Medium'),('L','Low')])
    risk = RadioField('How risk can you take?',choices=[('H','High'),('M','Medium'),('L','Low')])
    time = RadioField('How much time can you invest?',choices=[('H','>5 Years'),('M','3-5 Years'),('L','0-3 Years')])
    capital = RadioField('How much capital can you invest?',choices=[('H','>10 Lakhs'),('M','1-10 Lakhs'),('L','<1 Lakhs')])
    submit = SubmitField('Find!')

