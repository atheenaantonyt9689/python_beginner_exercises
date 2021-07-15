def nand_gate(A,B):   
    
    if A==0 and B==0:
        return "NAND(A, B): {}".format(True)
    elif  A==0 and B==1:
        return "NAND(A, B): {}".format(True)
    elif A==1 and B==0:
        return "NAND(A, B): {}".format(True) 
    else:
        return "NAND(A, B): {}".format(False) 
print(nand_gate(1,0))