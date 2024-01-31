# -*- coding: utf-8 -*-
"""
Created on Mon Dec 4 16:09:54 2023
@author: Mheab
"""

# Function Declarations
def error_check(prompt, options):
    response = input(prompt)
    while response not in options:
        print("Invalid response. Please try again.")
        response = input(prompt)
    return response

def get_room_name(room_choice):
    room_names = ["Interior", "Ocean View", "Balcony", "Royal Suite Class"]
    return room_names[room_choice - 1]

def print_receipt(fName, lName, customer_address, city, state, zip_code, credit_card_type, credit_card_num, order_details, room_choice, num_guests, room_cost, dinner_costs, excursion_name, excursion_cost, disc_amt, selected_excursions):
    room_name = get_room_name(room_choice)
    print("\n************************************************************")
    print("               Monroe Caribbean Cruise Line")
    print("                 Reservation Receipt")
    print("************************************************************")
    print(f"Dear {fName} {lName},")
    print("Thank you for choosing Monroe Caribbean Cruise Line.")
    print(f"Num of Guests: {num_guests}  | Room Type: {room_name} | Room Cost: ${room_cost:.2f}")
    print(f"{selected_package_type}: ${dinner_costs:.2f}")
    print(f"Excursion - {excursion_name}: ${excursion_cost:.2f} ")

    if selected_excursions:
        print("Selected Excursions:")
        for excursion in selected_excursions:
            print(f"- {excursion[0]}: ${excursion[1]:.2f}")

    print(f"Payment Option: {credit_card_type} | Last 4 Digits: {last_four_digits}")
    print(f"Billing Address: {customer_address}, {city}, {state} {zip_code}")

    subtotal = room_cost + dinner_costs + excursion_cost
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Monroe College Student Discount: ${disc_amt:.2f}")

    state_tax = 0.0625
    tax = subtotal * state_tax
    total_due = subtotal + tax

    print("Additional Charges:")
    print(f"Tax (6.25%): ${tax:.2f}")
    print(f"Total Due: ${total_due:.2f}")
    print("************************************************************\n")


# Main Program
all_reservations = []  # List to store all reservations
room_price = [["Interior", 599], ["Ocean View", 699], ["Balcony", 799], ["Royal Suite Class", 1999]]
room_names = ["Interior", "Ocean View", "Balcony", "Royal Suite Class"]
excursions = ["Cultural Sightseeing", "Snorkeling", "Scuba Diving"]
excursions_price = [["Cultural Sightseeing", 150], ["Snorkeling", 100], ["Scuba Diving", 599]]
dinner_package_price = [["Alcoholic Dinner Package", 150], ["Non-Alcoholic Dinner Package", 75]]
dinner_package = ["Alcoholic Dinner Package", "Non-Alcoholic Dinner Package"]

print("Welcome to Monroe Caribbean Cruise Line Reservation System")

cruise_program = input("Press any key to continue (or type '-1' to end): ")

while cruise_program != '-1':
    print("\nMonroe Caribbean Cruise Line offers exciting winter voyages to four captivating destinations:")
    print("1. Bahamas\n2. Caribbean\n3. St. Lucia\n4. Panama Canal")

    selected_location = int(error_check("Please select your desired destination (enter the corresponding number): ", ["1", "2", "3", "4"]))

    print("\nSelect from our five magnificent ships setting sail in Winter 2023:")
    print("1. Allure of the Seas\n2. Anthem of the Seas\n3. Harmony of the Seas\n4. Oasis of the Seas\n5. Symphony of the Seas")

    selected_ship = int(error_check("Please choose your preferred cruise ship (enter the corresponding number): ", ["1", "2", "3", "4", "5"]))

    print("\nExplore our variety of luxurious room types:")
    for index, room in enumerate(room_price, start=1):
        print(f"{index}. {room[0]} - ${room[1]} per night")

    room_choice = int(error_check("Please pick your desired room (enter the corresponding number): ", ["1", "2", "3", "4"]))

    if room_choice == 1:
        selected_room_type = room_price[0]
    elif room_choice == 2:
        selected_room_type = room_price[1]
    elif room_choice == 3:
        selected_room_type = room_price[2]
    else:
        selected_room_type = room_price[3]

    filtered_excursions = []
    selected_excursions = []
    excursion_selection = error_check("\nDo you want to add excursions to your trip? (1 for Yes, 2 for No): ", ["1", "2"])

    while excursion_selection == '1':
        if selected_ship == 5:
            filtered_excursions = [trip for trip in excursions_price if trip[0] != "Scuba Diving"]
            print("\nEnhance your experience with our diverse range of excursions:")
            for index, trip in enumerate(filtered_excursions, start=1):
                print(f"{index}. {trip[0]} - ${trip[1]} ")
            selected_excursion = int(error_check("Please select an excursion (enter the corresponding number):", [str(i) for i in range(1, len(filtered_excursions) + 1)]))
            selected_excursions.append(filtered_excursions[selected_excursion - 1])
        else:
            print("\nEnhance your experience with our diverse range of excursions:")
            for index, trip in enumerate(excursions_price, start=1):
                print(f"{index}. {trip[0]} - ${trip[1]} ")
            selected_excursion = int(error_check("Please select an excursion (enter the corresponding number):", [str(i) for i in range(1, len(excursions_price) + 1)]))
            selected_excursions.append(excursions_price[selected_excursion - 1])

        excursion_selection = error_check("\nDo you want to add more excursions to your trip? (1 for Yes, 2 for No): ", ["1", "2"])

    if selected_excursion == 1:
        excursion_cost = excursions_price[0][1]
        excursion_name = excursions[0]
    elif selected_excursion == 2:
        excursion_cost = excursions_price[1][1]
        excursion_name = excursions[1]
    else:
        excursion_cost = excursions_price[2][1]
        excursion_name = excursions[2]

    print("\nIndulge in our exquisite dinner packages:")
    for index, package in enumerate(dinner_package_price, start=1):
        print(f"{index}. {package[0]} - ${package[1]} ")
    selected_dinner = int(error_check("Please choose a dinner package (enter the corresponding number):", ["1", "2"]))

    if selected_dinner == 1:
        selected_package_type = dinner_package[0]
        dinner_costs = dinner_package_price[0][1]
    else:
        selected_package_type = dinner_package[1]
        dinner_costs = dinner_package_price[1][1]

    print("\nPlease provide your information for the reservation:")

    fName = input("First Name: ")
    lName = input("Last Name: ")
    customer_address = input("Street Address: ")
    city = input("City: ")
    state = input("State: ")
    zip_code = input("Zip Code: ")
    credit_card_type = input("Credit Card Type: ")
    credit_card_num = input("Credit Card Number: ")

    if len(credit_card_num) >= 4:
        last_four_digits = credit_card_num[-4:]
    else:
        print("\nInvalid input. The credit card number should be at least four digits long.")

    num_guests_valid = False

    while not num_guests_valid:
        try:
            num_guests = int(input("\nHow many passengers will be joining you? "))
            if num_guests > 0:
                num_guests_valid = True
            else:
                print("Number of guests must be a positive integer. Please try again.")
        except ValueError as e:
            print(f"Invalid input: {e}")

    if room_choice == 1:
        room_cost = num_guests * room_price[0][1]
    elif room_choice == 2:
        room_cost = num_guests * room_price[1][1]
    elif room_choice == 3:
        room_cost = num_guests * room_price[2][1]
    else:
        room_cost = num_guests * room_price[3][1]

    order_details = [f"{num_guests} x {room_choice}"]

    subtotal = room_cost + dinner_costs + excursion_cost

    monroe_disc = 0.0
    disc_amt = 0.0
    stu_disc = error_check("\nAre you a student of Monroe College? (1 for Yes, 2 for No): ", ["1", "2"])
    if stu_disc == "1":
        monroe_disc = 0.10
        disc_amt = monroe_disc * subtotal

    reservations = [fName, lName, customer_address, city, state, zip_code, credit_card_type, credit_card_num, order_details, room_choice, num_guests, room_cost, dinner_costs, excursion_name, excursion_cost, disc_amt, selected_excursions]
    all_reservations.append(reservations)

    print_receipt(*reservations)

    cruise_program = input("Please enter any key to continue (or type '-1' to end): ")

print("Thank you for choosing Monroe Caribbean Cruise Line. We look forward to welcoming you on board!")
pgm_ctrl = input("\nPress any key to exit...")
