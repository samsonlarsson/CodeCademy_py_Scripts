def calculate_tax(salaries = dict):
    taxt_dict = salaries

    tax_rates = (
        (0.0, (0, 1000)),
        (0.10, (1001, 10000)),
        (0.15, (10001,20200)),
        (0.20, (20201,30750)),
        (0.25, (30751, 50000)),
        )

    for person, salary in salaries.iteritems():
        
        print str('\n'+ person)
        # print taxt_dict[person]
        # taxt_dict[person] = 0

        for percent, _range in tax_rates:
            if _range[0]== 0: # and _range[1] == 1000:
                taxt_dict[person] = 0  #reaffirm still 0
            else:
                # taxt_dict[person] = 0
                next_taxable_amnt = _range[1] - _range[0]+1
                print _range

                if salary - next_taxable_amnt > 0:
                    taxt_dict[person] += next_taxable_amnt*percent

                    print(_range[1])
                    print(_range[0])
                    print (str(next_taxable_amnt) + ' next taxable amnt')
                    print ('tax whole range= ' + str(taxt_dict[person]))

                    salary -= next_taxable_amnt
                else:
                    taxt_dict[person] += salary *percent

                    print ('tax in this range = ' + str(taxt_dict[person]))

                    salary -= next_taxable_amnt
                    break
                                
                if salary > 0:
                    taxt_dict[person] += salary*0.30

    return taxt_dict

# #test
salaries = {
    'Alex': 500,
    'James': 20500,
    'Kinuthia': 70000
}
                                                                                                                         
print (calculate_tax(salaries))