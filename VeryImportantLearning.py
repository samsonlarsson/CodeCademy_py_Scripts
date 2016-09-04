test = {
    'Alex': 500,
    'James': 20500,
    'Kinuthia': 70000,
    'Sam': 800,
    'Jane': 20500,
}

def calculate_tax(income = dict):
  tax_rates = (
    (0.0, (0, 1000)),
    (0.10, (1000, 10000)),
    (0.15, (10000, 20200)),
    (0.20, (20200, 30750)),
    (0.25, (30750, 50000)),
    )
    
  if type (income) == dict:
    result = {}
    for name, salary in income.items():
      if type (salary) == str:
        raise ValueError("Allow only numeric input")
      if type (salary) == int:
        result[name] = 0
        for percent, _range in tax_rates:
          next_taxable_amount = _range[1] - _range[0]
          if salary - next_taxable_amount > 0:
            result[name] += next_taxable_amount * percent
            salary -= next_taxable_amount
          else:
            result[name] += salary * percent
            salary -= next_taxable_amount
            break
        
        if salary > 0:
          result[name] += salary * 0.3
    return result
  else:
     raise ValueError("Input of type int not allowed") 
  
  
print (calculate_tax(test))

