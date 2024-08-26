salary=int(input())
age=int(input())
if salary>=20000 or age<=25:
    loanamount=int(input("loan :"))
    if loanamount<=50000:
        print("loan is eligible")
    else:
        print("max loan is 50000")
else:
    print("you are not eligible for loan")