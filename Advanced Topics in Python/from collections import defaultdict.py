from collections import defaultdict


def calculate_rate(persons_income = dict):
    tax_rates_for_income = (
        (0.0, (0, 1000)),
        (0.10, (1001, 10000)),
        (0.15, (10001, 20200)),
        (0.20, (20201, 30750)),
        (0.25, (30751, 50000)),
    )

    result = defaultdict(float)

    for name, salary in persons_income.items():
        for percent, _range in tax_rates_for_income:
            next_taxable_amount = _range[1] - _range[0] + 1
            if salary - next_taxable_amount > 0:
                result[name] += next_taxable_amount * percent
                salary -= next_taxable_amount
            else:
                result[name] += salary * percent
                salary -= next_taxable_amount
                break

        if salary > 0:
            result[name] += salary * 0.30

    return result


persons2income = {
    'Alex': 500,
    'James': 20500,
    'Kinuthia': 70000,
}

print(dict(calculate_rate(persons2income))
