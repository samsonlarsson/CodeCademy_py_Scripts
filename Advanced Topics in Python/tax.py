my_list = {"Joe": 80000}


  
def calculate_tax(my_list):
  for key in my_list:
    t_tax = 0
    if my_list[key] in range(0, 1000):
      t_tax = 0
      key = key - 1000
      return t_tax
  
    elif my_list[key] in range(1000, 10000):
      t_tax = t_tax + salary * 0.1
      key = key - 10000
      return t_tax

    elif my_list[key] in range(10000, 20200):
      t_tax = t_tax + salary * 0.15
      key = key - 30750
      return t_tax
      
    elif my_list[key] in range(20201, 30750):
      t_tax = t_tax + key * 0.2
      key = key - 30750
      return t_tax
      
    elif my_list[key] in range(307501, 50000):
      t_tax = t_tax + key * 0.25
      key = key - 50000
      return t_tax
    
    elif my_list[key] > 50000:
      t_tax = t_tax + key * 0.3
      return t_tax
    
    else:
      t_tax = t_tax
    return t_tax

    print my_list[value], t_tax
