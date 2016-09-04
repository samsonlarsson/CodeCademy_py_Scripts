def calculate_tax(salaries = dict): #salaries is a dictionary

	tax_dict = salaries       #tax dictionary initialised as acopy of the salaries
	tax_rates_for_income = (
        (0.0, (0, 1000)),
        (0.10, (1001, 10000)),
        (0.15, (10001, 20200)),
        (0.20, (20201, 30750)),
        (0.25, (30751, 50000)),
    )                         #tax rates specified.    

	for person, salary  in salaries.iteritems():
		tax_dict[person] = 0  #set tax amount for each person to zero here 
		for percent, _range in tax_rates_for_income:
            next_taxable_amount = _range[1] - _range[0] + 1
            if salary - next_taxable_amount > 0:
                tax_dict[person] += next_taxable_amount * percent  #increment the tax charge accordingly
                salary -= next_taxable_amount
            else:
                tax_dict[person] += salary * percent
                salary -= next_taxable_amount
                break

            if salary > 0:
	            tax_dict[person] += salary * 0.30

		# print tax_dict[person]
	return tax_dict


	# return salaries  

salaries = {
    'Alex': 500,
    'James': 20500,
    'Kinuthia': 70000
}
                                                                                                                         
print (calculate_tax(salaries))