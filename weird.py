c=    ['cust_id''.''comp_id''.''sector''.''product_type''.''company_name''.''working_from''.''working_till''.''email''.''password']
def cal1(a):
    b={}
    for i in a:
        b[i]='form.'+i+'.data'

    print(b)

# {'cust_id': form.cust_id.data'.'' 'comp_id': form.comp_id.data'.'' 'sector': form.sector.data'.'' 'product_type': form.product_type.data'.'' 'company_name': form.company_name.data'.'' 'working_from': form.working_from.data'.'' 'working_till': form.working_till.data'.'' 'email': form.email.data'.'' 'password': form.password.data}


a=['su_name''.''account_id''.''date_val''.''date_created''.''bank_balance''.''sales_type''.''email''.''registered_photo''.''linked_acc''.''state''.''size''.''tax_owed''.''source_id''.''value''.''interest''.''product_id''.''product_name''.''category''.''price''.''sold''.''email''.''password''.''submit']


b = ['name''.''branch_id''.''branch_name''.''contact''.''no_cust''.''total_assets''.''ROI_for_loans''.''ROI_for_savings''.''ROI_for_current''.''no_fds''.''min_bal''.''ann_govt''.''loan_taken''.''money_lent''.''email''.''password''.''submit']

c= ['cust_id''.''comp_id''.''sector''.''product_type''.''company_name''.''working_from''.''working_till''.''email''.''password']
def cal(a):
    b=[]
    for i in a:
        i = 'user_info['+i+']'
        b.append(i)
    print(b)    





a =['bank_id','account_balance','account_type','set_pin','govt_id','profession','contact_no','branch_id','fixed_deposit','salary','username','tax_bracket','loan_emi','aco','password']

cal1(a)
cal(a)