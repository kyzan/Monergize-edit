

# a = ['name','type','bank_partner','bank_branch','acc_no','ifsc_code','nature_of_biz','contact_no','tax_bracket','doe','type_of_acc','loan_amount','loan_period','fd','int_rate','branches_in_india','importers_id','raw_material','finished_product','custom_duty','relaxation_limit','gst','pe_ratio','quick_ratio','acc_payable','acc_receivable','eps','market_value','book_value','total_assets','total_liabilities','inventories','external_fundings','retained_earnings','product_id ','product_name','email','password','submit']
# b = {}

# for c in a:
#     b[c] = form.'+c+'.data

# print(b)


# a = {'name': form.name.data, 'type': form.type.data, 'bank_partner': form.bank_partner.data, 'bank_branch': form.bank_branch.data, 'acc_no': form.acc_no.data, 'ifsc_code': form.ifsc_code.data, 'nature_of_biz': form.nature_of_biz.data, 'contact_no': form.contact_no.data, 'tax_bracket': form.tax_bracket.data, 'doe': form.doe.data, 'type_of_acc': form.type_of_acc.data, 'loan_amount': form.loan_amount.data, 'loan_period': form.loan_period.data, 'fd': form.fd.data, 'int_rate': form.int_rate.data, 'branches_in_india': form.branches_in_india.data, 'importers_id': form.importers_id.data, 'raw_material': form.raw_material.data, 'finished_product': form.finished_product.data, 'custom_duty': form.custom_duty.data, 'relaxation_limit': form.relaxation_limit.data, 'gst': form.gst.data, 'pe_ratio': form.pe_ratio.data, 'quick_ratio': form.quick_ratio.data, 'acc_payable': form.acc_payable.data, 'acc_receivable': form.acc_receivable.data, 'eps': form.eps.data, 'market_value': form.market_value.data, 'book_value': form.book_value.data, 'total_assets': form.total_assets.data, 'total_liabilities': form.total_liabilities.data, 'inventories': form.inventories.data, 'external_fundings': form.external_fundings.data, 'retained_earnings': form.retained_earnings.data, 'product_id ': form.product_id .data, 'product_name': form.product_name.data, 'email': form.email.data, 'password': form.password.data, 'submit': form.submit.data}

# a = 'COMP100001'
# a = 'COMP' + str(int(a[4:])+1)
# print(a)

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23,17,35,29,12]
ax.bar(langs,students)
plt.show()