def raindropss(number):
    if number %3 ==0 and number %5 ==0:
        return "pling plang"
    elif number %5 ==0 and number %7==0:
        return "plang plong"
    elif number %7==0 and number %3==0:
        return "plong pling"
    elif number %3 ==0:
        return "pling"
    elif number %5 ==0:
        return "plang"
    elif number %7==0:
        return "plong"
    else:
        return "{}".format(number)

print(raindropss(75))