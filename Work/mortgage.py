# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment = 1000
months_extra_payment = 12
payments = 0

while principal > 0:
    if months_extra_payment > 0:
        principal = principal * (1+rate/12) - (payment + extra_payment)
        total_paid = total_paid + (payment + extra_payment)
        months_extra_payment -= 1
    else: 
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    payments += 1

print('Total paid', round(total_paid, 2), payments)