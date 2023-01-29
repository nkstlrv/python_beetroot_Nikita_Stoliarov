class InvalidCountry(Exception):

    available_countries = ["Ukraine", "USA", "UK", "Sweeden", "New Zeland", "Japan"]

    def __init__(self, country, message="Unfortunately, there is no access from your country :("):
        self.country = country
        self.message = message
        super().__init__(self.message)


country = input("Enter country to check access: ")
if country not in InvalidCountry.available_countries:
    error_message = str(InvalidCountry(country))

    with open ("Module 2\HW_16_Inheritance\logs.txt", "a") as f:
        f.write(error_message + "\n\n")

    raise InvalidCountry(country)
else:
    print("Congratulations. You've got access! :)")
