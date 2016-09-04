def calculate_tax(persons_income = dict):

    result = {}
    for name, salary in persons_income.items():
    	next_taxable_amount = 0
    	if salary >= 0:
    		next_taxable_amount = 1000
    		result[name] = 0
    		salary -= 1000
    		next_taxable_amount = 9000
        
        if salary - next_taxable_amount > 0:
        	result[name] += next_taxable_amount * 0.10
        	salary -= next_taxable_amount
        	next_taxable_amount = 10200

    	if salary - next_taxable_amount > 0:
    		result[name] += next_taxable_amount * 0.15
    		salary -= next_taxable_amount
    		next_taxable_amount = 10550 

    	if salary - next_taxable_amount > 0:
    		result[name] += next_taxable_amount * 0.20
    		salary -= next_taxable_amount
    		next_taxable_amount = 19250 

    	if salary - next_taxable_amount > 0:
    		result[name] += next_taxable_amount * 0.25
    		salary -= next_taxable_amount
    		next_taxable_amount = salary - next_taxable_amount
    	else:
    		result[name] += salary * 0.2
    		salary -= next_taxable_amount
    		break

		if salary > 0:
			result[name] = salary * 0.30

    return result


persons2income = {
    'Alex': 500,
    'James': 20500,
    'Kinuthia': 70000,
}

print(calculate_tax(persons2income))