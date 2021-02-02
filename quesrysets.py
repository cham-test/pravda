## 1 ##
customers = Customer.objects.all()
payments = Payment.objects.all()

result = []

for customer in customers:
    if payments.objects.filter(customer=customer).count() >= 4:
        result.append(customer)

## 2 ##
