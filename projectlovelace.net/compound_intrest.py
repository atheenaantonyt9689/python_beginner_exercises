def compound_interest(amount, rate, years):
    
    m=amount
    r=float(rate)
    n=years
    new_amount=m*(1+r)**n

    

    return "Final Amount :{:.2f}".format(new_amount)
print(compound_interest(1000, 0.07, 25))