

def calculateSubTotal(quantity, price):
    subTotal = quantity * price
    return subTotal

def calculateValueWithTax(value, tax):
    taxPercentage = tax / 100
    result = value * (1 + taxPercentage)
    return result


