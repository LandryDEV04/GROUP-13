from datetime import datetime
import calendar

class Person:
    def __init__(
        self, last_name, first_name, birth_place, nationality,
        birth_year, birth_month, birth_day, height_cm, gender,
        address, profession, phone, emergency_contact, emergency_phone
    ):
        self.last_name = last_name
        self.first_name = first_name
        self.full_name = f"{last_name} {first_name}"
        self.birth_place = birth_place
        self.nationality = nationality
        self.birth_year = birth_year
        self.birth_month = birth_month
        self.birth_day = birth_day
        self.height_cm = height_cm
        self.gender = gender
        self.address = address
        self.profession = profession
        self.phone = phone
        self.emergency_contact = emergency_contact
        self.emergency_phone = emergency_phone

    def get_age(self, reference_year=None):
        year = reference_year or datetime.now().year
        return year - self.birth_year

    def is_adult(self):
        return self.get_age() >= 18


class IDCard:
    def __init__(self, person: Person):
        self.person = person
        self.issue_date = datetime.now()
        self.expire_date = self._calculate_expiration()
        self.id_number = self.generate_id()

    def generate_id(self):
        return (
            f"{self.person.full_name[:3].upper()}"
            f"{self.person.birth_year}"
            f"{self.person.birth_month:02d}"
            f"{self.person.birth_day:02d}"
        )

    def _calculate_expiration(self):
        target_year = self.issue_date.year + 10
        try:
            return self.issue_date.replace(year=target_year)
        except ValueError:
            # Handle Feb 29 in non-leap target years.
            return self.issue_date.replace(month=2, day=28, year=target_year)

    def display(self):
        p = self.person
        age = p.get_age()
        status = "ADULT" if p.is_adult() else "MINOR"

        issue = self.issue_date.strftime("%d/%m/%Y")
        expiration = self.expire_date.strftime("%d/%m/%Y")

        width = 60  # inner frame width

        def line(label, value):
            content = f"{label}: {value}"
            return f"│ {content:<{width-2}} │"

        print("\n" + "┌" + "─" * width + "┐")
        print("│{:^{w}}│".format("NATIONAL IDENTITY CARD", w=width))
        print("├" + "─" * width + "┤")

        print(line("LAST NAME", p.last_name))
        print(line("FIRST NAME", p.first_name))
        print(line("DATE OF BIRTH", f"{p.birth_day:02d}/{p.birth_month:02d}/{p.birth_year}"))
        print(line("BIRTH PLACE", p.birth_place))
        print(line("NATIONALITY", p.nationality))
        print(line("AGE / STATUS", f"{age} years - {status}"))
        print(line("HEIGHT", f"{p.height_cm} cm"))
        print(line("GENDER", p.gender))
        print(line("PROFESSION", p.profession))
        print(line("PHONE", p.phone))
        print(line("ADDRESS", p.address))
        print(line("EMERGENCY CONTACT", p.emergency_contact))
        print(line("EMERGENCY PHONE", p.emergency_phone))

        print("├" + "─" * width + "┤")
        print(line("ID NUMBER", self.id_number))
        print(line("ISSUED ON", issue))
        print(line("EXPIRATION", expiration))

        print("└" + "─" * width + "┘")


class IDCardGenerator:
    def __init__(self):
        self.cards = []

    def collect_person_data(self):
        def prompt_text(label):
            while True:
                val = input(f"Enter your {label}: ").strip()
                if val:
                    return val
                print(f"Error: {label.title()} is required")

        def prompt_birth_year():
            while True:
                val = input("Enter your birth year: ").strip()
                try:
                    year = int(val)
                    current_year = datetime.now().year
                    if 1900 <= year <= current_year:
                        return year
                except ValueError:
                    pass
                print("Error: Invalid year")

        def prompt_birth_month():
            month_names = {name.lower(): idx for idx, name in enumerate(calendar.month_name) if name}
            month_abbr = {abbr.lower(): idx for idx, abbr in enumerate(calendar.month_abbr) if abbr}

            while True:
                raw = input("Enter your birth month (number or name): ").strip().lower()

                if not raw:
                    print("Error: Invalid month")
                    continue

                if raw.isdigit():
                    month = int(raw)
                    if 1 <= month <= 12:
                        return month
                else:
                    if raw in month_names:
                        return month_names[raw]
                    if raw in month_abbr:
                        return month_abbr[raw]

                print("Error: Invalid month")

        def prompt_birth_day(year, month):
            while True:
                val = input("Enter your birth day: ").strip()
                try:
                    day = int(val)
                    _, max_day = calendar.monthrange(year, month)
                    if 1 <= day <= max_day:
                        return day
                    print(f"Error: {calendar.month_name[month]} only has {max_day} days.")
                except ValueError:
                    print("Error: Invalid day")

        def prompt_height():
            while True:
                val = input("Enter your height in cm: ").strip()
                try:
                    height = float(val)
                    if height > 0:
                        return height
                except ValueError:
                    pass
                print("Error: Height must be a positive number")

        def prompt_gender():
            while True:
                val = input("Enter your gender (M/F): ").strip().upper()
                if val in ["M", "F"]:
                    return val
                print("Error: Invalid gender")

        while True:
            last_name_raw = " ".join(input("Enter your last name: ").split())
            first_name_raw = " ".join(input("Enter your first name: ").split())

            if not last_name_raw or not first_name_raw:
                print("Error: Both last and first name are required.\n")
                continue

            last_name = last_name_raw.title()
            first_name = first_name_raw.title()

            birth_place = prompt_text("birth place")
            nationality = prompt_text("nationality")

            while True:
                birth_year = prompt_birth_year()
                birth_month = prompt_birth_month()
                birth_day = prompt_birth_day(birth_year, birth_month)

                try:
                    datetime(birth_year, birth_month, birth_day)
                    break
                except ValueError:
                    print("Error: Invalid calendar date. Please re-enter your birth date.\n")

            height_cm = prompt_height()
            gender = prompt_gender()
            address = prompt_text("address")
            profession = prompt_text("profession")
            phone = prompt_text("phone number")
            emergency_contact = prompt_text("emergency contact")
            emergency_phone = prompt_text("emergency contact phone")

            return Person(
                last_name, first_name, birth_place, nationality,
                birth_year, birth_month, birth_day,
                height_cm, gender, address, profession,
                phone, emergency_contact, emergency_phone
            )

    def generate_cards(self):
        while True:
            raw = input("How many cards to create?: ").strip()
            try:
                n = int(raw)
                if n <= 0:
                    raise ValueError
            except ValueError:
                print("Error: enter a positive integer.")
                continue
            break

        for i in range(n):
            print(f"\n=== Creating card {i+1}/{n} ===")
            person = self.collect_person_data()
            card = IDCard(person)
            self.cards.append(card)
            card.display()

    def show_all(self):
        if not self.cards:
            print("No generated cards.")
            return

        for i, card in enumerate(self.cards, 1):
            print(f"\n----- CARD {i} -----")
            card.display()


def main():
    gen = IDCardGenerator()

    while True:
        print("\n=== MENU ===")
        print("1 • Create cards")
        print("2 • Show all cards")
        print("3 • Quit")

        c = input("Choice: ")

        if c == "1":
            gen.generate_cards()
        elif c == "2":
            gen.show_all()
        elif c == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
