from datetime import datetime

def write_rent_bill(name, contact_no, renting_duration, bills, file_path="bill.txt"):
    """
    Write a rent bill to the specified file.

    Args:
        name (str): Tenant's name.
        contact_no (str): Tenant's contact number.
        renting_duration (int): Duration of the rental in months.
        bills (list): List of bill details for each rented land.
        file_path (str): Path to the file where the bill will be written. Defaults to "bill.txt".
    """
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    grand_total = sum(item[5] for item in bills)

    with open(file_path, "w") as file:
        file.write(f"\n\t\t\t\tTecho Property Nepal\n")
        file.write(f"\t\t\t\tkamalpokhari,ktm\n")
        file.write(f"\t\t\t\tPhone no: 01-384783, 9876542534\n")
        file.write(f"__________________________________________________________________________________________________________\n")
        file.write(f"Tenant details:\n")
        file.write(f"___________________________________________________________________________________________________________\n")
        file.write(f"Tenant name : {name}\n")
        file.write(f"Contact no : {contact_no}\n")
        file.write(f"Date : {current_datetime}\n")
        file.write(f"Lease Duration : {renting_duration} months\n")
        file.write(f"_____________________________________________________________________________________________________________\n")
        file.write(f"Land_Id \t City \t\t Direction \t Anna \t\t Price \t\t Rental_Duration Price\n")
        for each in bills:
            file.write(f"{each[0]}\t\t{each[1]}\t{each[2]}\t\t{each[3]}\t\t{each[4]}\t\t\t{each[5]}\n")
        file.write(f"_______________________________________________________________________________________________________________\n")
        file.write(f"Grand Total : {grand_total}\n")

def write_return_bill(name, contact_no, renting_duration, rented_duration, fine, bills, file_path="returnbill.txt"):
    """
    Write a return bill to the specified file.

    Args:
        name (str): Tenant's name.
        contact_no (str): Tenant's contact number.
        renting_duration (int): Duration of the rental in months.
        rented_duration (int): Actual duration the land was rented.
        fine (float): Fine amount for extra rental duration.
        bills (list): List of bill details for each returned land.
        file_path (str): Path to the file where the return bill will be written. Defaults to "returnbill.txt".
    """
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    grand_total = sum(item[5] for item in bills) + fine

    with open(file_path, "w") as file:
        file.write(f"\n\t\t\t\tTecho Property Nepal\n")
        file.write(f"\t\t\t\tkamalpokhari,ktm\n")
        file.write(f"\t\t\t\tPhone no: 01-384783, 9876542534\n")
        file.write(f"_______________________________________________________________________________________________________________\n")
        file.write(f"Tenant details:\n")
        file.write(f"_______________________________________________________________________________________________________________\n")
        file.write(f"Tenant name : {name}\n")
        file.write(f"Contact no : {contact_no}\n")
        file.write(f"Date : {current_datetime}\n")
        file.write(f"Lease Duration : {renting_duration} months\n")
        file.write(f"Rented Duration : {rented_duration} months\n")
        file.write(f"_______________________________________________________________________________________________________________\n")
        file.write(f"Land_Id \t City \t\t Direction \tAnna \t\t Price \t\t Rental_Duration Price\n")
        for each in bills:
            file.write(f"{each[0]}\t\t{each[1]}\t{each[2]}\t\t{each[3]}\t\t{each[4]}\t\t\t{each[5]}\n")
        file.write(f"________________________________________________________________________________________________________________\n")
        file.write(f"Fine : {fine}\n")
        file.write(f"Grand Total : {grand_total}\n")
