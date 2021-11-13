#  You can experiment here, it won’t be checked
income = int(input())
if 0 <= income <= 15527:
    percent = 0
    calculated_tax = int(round(income * (percent / 100)))
    print("The tax for {} is {}%. That is {} dollars!".format(income, percent, calculated_tax))
elif 15528 <= income <= 42707:
    percent = 15
    calculated_tax = int(round(income * (percent / 100)))
    print("The tax for {} is {}%. That is {} dollars!".format(income, percent, calculated_tax))
elif 42708 <= income <= 132406:
    percent = 25
    calculated_tax = int(round(income * (percent / 100)))
    print("The tax for {} is {}%. That is {} dollars!".format(income, percent, calculated_tax))
else:
    percent = 28
    calculated_tax = int(round(income * (percent / 100)))
    print("The tax for {} is {}%. That is {} dollars!".format(income, percent, calculated_tax))
