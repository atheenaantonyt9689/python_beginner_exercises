def moose_body_mass(latitude):
    mass = 0
    a=2.757
    b=16.793
    mass=a*latitude+b
    

    return " body mass of a moose living at the input latitude: {:.4f}".format(mass)
print(moose_body_mass(60.5))