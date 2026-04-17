# User inputs
print("===================================================");
print(  "        ID CARD GENERATOR");
print("===================================================\n");
full_name = input("Enter your full name: ")
birth_place = input("Place of birth: ")
nationality = input("Nationality: ")
birth_year = int(input("Year of birth: "))
birth_month = int(input("Month of birth (1-12): "))
birth_day = int(input("Day of birth: "))
height_cm = float(input("Height in cm: "))
gender = input("Gender (M/F): ")
address = input("Address: ")
profession = input("Profession: ")

# Calculations
age = 2025 - birth_year
expiration_year = 2025 + 10

# ID number generation
id_number = f"{full_name[:3].upper()}{birth_year}{birth_month:02d}"

# Summary display with f-strings
print("===================================================");
print(  "        ID CARD GENERATED SUCCESSFULLY");
print("===================================================\n");

print(f"Name: {full_name}")
print(f"Born in: {birth_day}/{birth_month:02d}/{birth_year}")
print(f"Place: {birth_place}")
print(f"Nationality: {nationality}")
print(f"Card valid until: {expiration_year}")
print(f"ID Number: {id_number}")