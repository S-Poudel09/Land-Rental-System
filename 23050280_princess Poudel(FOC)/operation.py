from datetime import datetime
from write import write_rent_bill, write_return_bill

def get_valid_name(prompt):
    while True:
        name = input(prompt)
        if name.isalpha():
            return name
        print("PLEASE PROVIDE VALID NAME")

def get_valid_contact(prompt):
    while True:
        try:
            contact_no = int(input(prompt))
            if len(str(contact_no)) == 10:
                return contact_no
            print("PLEASE ENTER VALID CONTACT NO")
        except ValueError:
            print("PLEASE ENTER VALID CONTACT NO")

def get_land_id(prompt, available_ids):
    while True:
        land_id = input(prompt)
        if land_id in available_ids:
            return land_id
        print("Invalid LandId")

def get_valid_anna(prompt, correct_anna):
    while True:
        try:
            anna = int(input(prompt))
            if anna == correct_anna:
                return anna
            print("Invalid Anna request")
        except ValueError:
            print("Invalid Anna request")

def get_valid_duration(prompt, max_duration):
    while True:
        try:
            duration = int(input(prompt))
            if 0 < duration <= max_duration:
                return duration
            print("PLEASE PROVIDE VALID MONTH")
        except ValueError:
            print("PLEASE PROVIDE VALID MONTH")

def read_land_data(file_path):
    with open(file_path, "r") as file:
        return [line.strip().replace(",", "\t\t\t") for line in file]

def update_land_data(file_path, data):
    with open(file_path, "w") as file:
        for key, value in data.items():
            file.write(",".join(value) + "\n")

def generate_bill(bills, name, contact_no, current_datetime, renting_duration):
    grand_total = sum(item[5] for item in bills)
    print("\n")
    print("\t\t\t\tTecho Property Nepal ")
    print("\n")
    print("\t\t\t\t kamalpokhari,ktm")
    print("\n")
    print("\t\t\t\tPhone no: 01-384783, 9876542534")
    print("_____________________________________________________________________________________________________________________________")
    print("Tenant details:")
    print("_____________________________________________________________________________________________________________________________")
    print("Tenant name : " + str(name))
    print("Contact no :" + str(contact_no))
    print("Date : " + str(current_datetime))
    print("Lease Duration : " + str(renting_duration))
    print("\n")
    print("_____________________________________________________________________________________________________________________________")
    print("Land_Id \t\t City \t\t Direction \t\t Anna \t\t Price \t\t Rental_Duration Price")
    for each in bills:
        print(f"{each[0]}\t\t{each[1]}\t\t{each[2]}\t\t\t{each[3]}\t\t{each[4]}\t\t\t{each[5]}")
        print("\n")
    print("______________________________________________________________________________________________________________________________")
    print("\n")
    print("Grand Total :" + str(grand_total))
    print("\n")

def rent_land(d):
    rented_items = []
    bills = []
    file_path = "Land.txt"

    while True:
        l = list(d.keys())
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        name = get_valid_name("ENTER YOUR NAME: ")
        contact_no = get_valid_contact("ENTER YOUR PHONE NUMBER: ")
        
        print("Kitta \t\t\t Location \t\t\t Direction \t\t Anna \t\t\t Price \t\t\t Availability")
        print("\n".join(read_land_data(file_path)))
        print("\n")

        land_id = get_land_id("ENTER THE LAND ID: ", l)
        selected_item = d[land_id]
        selected_item[4] = "not available"
        rented_items.append(selected_item)

        anna = get_valid_anna("ENTER THE DESIRED ANNA FOR RENTING: ", int(selected_item[2]))
        renting_duration = get_valid_duration("ENTER THE MONTH: ", 24)

        items = [land_id, selected_item[0], selected_item[1], selected_item[2], selected_item[3],
                int(selected_item[3]) * renting_duration]
        bills.append(items)
        selected_item[4] = " Not available"

        update_land_data(file_path, d)
        generate_bill(bills, name, contact_no, current_datetime, renting_duration)

        write_rent_bill(name, contact_no, renting_duration, bills)

        if input("DO YOU WANT TO RENT ANOTHER LAND? (yes/no): ").lower() != 'yes':
            break

def return_land(d):
    returned_items = []
    bills = []
    file_path = "Land.txt"

    while True:
        l = list(d.keys())
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        name = get_valid_name("ENTER YOUR NAME: ")
        contact_no = get_valid_contact("ENTER YOUR PHONE NUMBER: ")
        
        print("Kitta \t\t\t Location \t\t\t Direction \t\t Anna \t\t\t Price \t\t\t Availability")
        print("\n".join(read_land_data(file_path)))
        print("\n")

        land_id = get_land_id("ENTER THE LAND ID TO RETURN: ", l)
        selected_item = d[land_id]

        anna = get_valid_anna("ENTER THE DESIRED ANNA FOR RENTING: ", int(selected_item[2]))
        renting_duration = get_valid_duration("ENTER THE MONTH: ", 24)
        rented_duration = get_valid_duration("ENTER THE RENTED MONTH: ", float('inf'))

        items = [land_id, selected_item[0], selected_item[1], selected_item[2], selected_item[3],
                int(selected_item[3]) * renting_duration]
        bills.append(items)

        selected_item[4] = " available"
        update_land_data(file_path, d)

        fine = (rented_duration - renting_duration) * int(selected_item[3]) * 0.10 if renting_duration < rented_duration else 0
        grand_total = sum(item[5] for item in bills) + fine

        print("\n")
        print("\t\t\t\tTecho Property Nepal ")
        print("\n")
        print("\t\t\t\t kamalpokhari,ktm")
        print("\n")
        print("\t\t\t\tPhone no: 01-384783, 9876542534")
        print("\n")
        print("\t\t\t\t RETURN BILL")
        print("_________________________________________________________________________________________________________________________________________________________________________________________")
        print("Tenant details:")
        print("_________________________________________________________________________________________________________________________________________________________________________________________")
        print("Tenant name : " + str(name))
        print("Contact no :" + str(contact_no))
        print("Date : " + str(current_datetime))
        print("Lease Duration : " + str(renting_duration))
        print("Rented Duration : " + str(rented_duration))
        print("\n")
        print("_________________________________________________________________________________________________________________________________________________________________________________________")
        print("Land_Id \t\t City \t\t Direction \t\t Anna \t\t Price \t\t Rental_Duration Price")
        for each in bills:
            print(f"{each[0]}\t{each[1]}\t\t\t{each[2]}\t\t\t{each[3]}\t\t{each[4]}\t\t\t{each[5]}")
            print("\n")
        print("__________________________________________________________________________________________________________________________________________________________________________________________")
        print("\n")
        if fine > 0:
            print("fine : " + str(fine))
        print("\n")
        print("Grand Total :" + str(grand_total))
        print("\n")

        write_return_bill(name, contact_no, renting_duration, rented_duration, fine, bills)

        if input("DO YOU WANT TO RETURN ANOTHER LAND? (yes/no): ").lower() != 'yes':
            break
