import csv
# because we are going to use the csv file
import datetime
# we will need the date of the Item
import random
# we need a random serial number

"""we need a list for field names:"""

fieldnames = ["product", "date", "serial_no", "price", "tax", "total"]
date = datetime.date.today()
serail__no = random.randint(1, 59999)
"""we are done with lists and variables"""

# ask the user if they want to add the product or see a product
Ask_user = input("Add Product Or Access Product?\n")

# check what they typed

if Ask_user.upper() == "APRO" or Ask_user.upper() == "ADD PRODUCT":

    # ask for the name of the product
    name = input("Name Of The Product:\n")

    # ask for the price
    price = input("\nPrice:\n")

    # ask for the tax in money, not in percent (%)
    tax = input("\nTax On The Product:\n")

    # declare the total variable
    total = int(price) + int(tax)

    print(f"total is going to be: {total}")

    with open("data.csv", "a", newline='') as data:
        # we opened the file
        # now use Dictwriter function to write to the
        # csv file

        format = csv.DictWriter(data, fieldnames=fieldnames)

        # not going to use the header() if you want to know what
        # it does visit this link :-
        # or got to my login-system-with-csv-files repository

        format.writerow({"product": name, "date": date, "serial_no": serail__no, "price": price, "tax": tax, "total": total})
        print("\n\nProduct was added!")
        print(f"\nyour product: {name} and its serial number is: {serail__no}")

elif Ask_user.upper() == "ACCP" or Ask_user.upper() == "ACCESS PRODUCT":
    # not going to go over this again

    serail__no2 = input("enter the serial Number of the product:\n")
    Name = input("\nenter the name of the product:\n")

    with open("data.csv", "r") as data2:
        format2 = csv.DictReader(data2)



        for line in format2:
            if line["serial_no"] == serail__no2 and line["product"] == Name:
                print(f"Product Found!")
            else:
                print("")
