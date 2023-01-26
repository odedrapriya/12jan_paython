print("-----------Welcome to kalyan jwellers----------")

name = input("Enter your name : ")
gender = input("Enter your Gender :")
age = int(input("Enter age :"))
product_nm = input("Enter product :")
product_grm =int(input("Enter product gram :"))
gold_price =int(input("Enter gold price :"))
mk_charge =int(input("Enter making charges :"))

print(" Name :",name)
print(" Gender :",gender)
print("Age :",age)
print("Product Name :",product_nm)
print("product gram :",product_grm)
print("gold price:",gold_price)

total_rate = product_grm * gold_price
print("Total gold rate : ",total_rate)


total_mkcharge = total_rate + (mk_charge*product_grm)
print("Total making charge :",total_mkcharge)

total_amt = total_rate + total_mkcharge
print("Total amount :",total_amt)

Discount = ""
if gender=="male":

    if age>65:
        if total_amt>=200000 and total_amt<300000:
            print("Discount 20%")
            Discount=total_amt*0.2
        
        elif total_amt>=300000 and total_amt<500000:
            print("Discount 30%")
            Discount=total_amt*0.3

        elif total_amt>500000:
            print("Discount 35 %")
            Discount=total_amt*0.35

        else:
            print("No Discount")

    else:
        if total_amt>=200000 and total_amt<300000:
            print("Discount 10%")
            Discount=total_amt*0.1

        elif total_amt>=300000 and total_amt<500000:
            print("Discount 20%")
            Discount=total_amt*0.2

        elif total_amt>500000:
            print("Discount 25%")
            Discount=total_amt*0.25

        else:
            print("No discount")

if gender=="female":
    if age>65:
        if total_amt>=200000 and total_amt<300000:
            print("Discount 25%")
            Discount=total_amt*0.25
        
        elif total_amt>=300000 and total_amt<500000:
            print("Discount 35%")
            Discount=total_amt*0.35

        elif total_amt>500000:
            print("Discount 40 %")
            Discount=total_amt*0.4

        else:
            print("No Discount")

    else:
        if total_amt>=200000 and total_amt<300000:
            print("Discount 15%")
            Discount=total_amt*0.15

        elif total_amt>=300000 and total_amt<500000:
            print("Discount 25%")
            Discount=total_amt*0.25

        elif total_amt>500000:
            print("Discount 30%")
            Discount=total_amt*0.3

        else:
            print("No discount")


dis_amt = (total_amt-total_mkcharge)-Discount
print("Discount amount :",dis_amt)

totalnet_amt = total_amt - dis_amt
print("Total net amount :",totalnet_amt)

