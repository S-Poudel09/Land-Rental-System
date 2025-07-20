from read import read_land_data
from operation import rent_land, return_land

def display_menu():
    """
    Display the menu options to the user.
    """
    print("\nMenu:")
    print("1. Rent the land")
    print("2. Return the land")
    print("3. Exit")

def handle_user_choice(choice, land_data):
    """
    Handle the user's menu choice and call appropriate functions.
    
    Parameters:
    - choice: The user's menu choice.
    - land_data: The land data read from the file.
    """
    if choice == 1:
        rent_land(land_data)
    elif choice == 2:
        return_land(land_data)
    elif choice == 3:
        return False
    else:
        print("Invalid choice")
    return True

def main():
    """
    Main function to drive the program.
    """
    land_data = read_land_data()
    continue_program = True

    while continue_program:
        display_menu()
        try:
            user_input = int(input("Enter your choice: "))
            continue_program = handle_user_choice(user_input, land_data)
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
