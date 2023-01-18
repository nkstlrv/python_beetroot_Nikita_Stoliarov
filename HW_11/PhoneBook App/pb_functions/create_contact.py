import json


def create_contact():
    # Phone number
    while True:

        phone_num = input("\n Firstly, lets add your contact's PHONE NUMBER"
                          "\n Acceptable formats: [0772074849] and [+490772074748]"
                          "\n ENTER your answer: ")
        if len(phone_num) in range(8, 15):
            print(f"\n Your new contact's number is --> {phone_num}")

            try:
                next_step = int(input("\n Do you want to continue?"
                                      "\n Yes --> [1] No --> [2] Quit --> [1101]: "))
            except ValueError:
                print("\n Input Error"
                      "\n Use only given numbers to choose")
                continue
            except Exception as error:
                print(f"\n Unexpected error --> {error}"
                      "\n Try again")
                continue

            if next_step == 1:
                break
            elif next_step == 2:
                continue
            elif next_step == 1101:
                quit()

    # Name and Surname
    while True:
        name = input("\n Now, add contact's NAME"
                     "\n ENTER your answer: ").title()
        surname = input("\n And SURNAME"
                        "\n ENTER your answer: ").title()
        print(f"\n Your contact's full name is {name} {surname}")

        try:
            next_step = int(input("\n Do you want to continue?"
                                  "\n Yes --> [1] No --> [2] Quit --> [1101]: "))
        except ValueError:
            print("\n Input Error"
                  "\n Use only given numbers to choose")
            continue
        except Exception as error:
            print(f"\n Unexpected error --> {error}"
                  "\n Try again")
            continue

        if next_step == 1:
            break
        elif next_step == 2:
            continue
        elif next_step == 1101:
            quit()

    # Address
    while True:
        city = input("\n Finally let's add contact's ADDRESS"
                     "\n ENTER contact's CITY: ").title()
        state = input("\n Now ENTER contact's STATE: ").title()
        country = input("\n And finally ENTER contact's COUNTRY: ").title()
        print(f"\n Your contact's address is --> {city}, {country}, {state}")

        try:
            next_step = int(input("\n Do you want to continue?"
                                  "\n Yes --> [1] No --> [2] Quit --> [1101]: "))
        except ValueError:
            print("\n Input Error"
                  "\n Use only given numbers to choose")
            continue
        except Exception as error:
            print(f"\n Unexpected error --> {error}"
                  "\n Try again")
            continue

        if next_step == 1:
            break
        elif next_step == 2:
            continue
        elif next_step == 1101:
            quit()

    new_cont = {
        "Number": phone_num,
        "Name": name,
        "Surname": surname,
        "City": city,
        "State": state,
        "Country": country
    }

    while True:
        val_lst = []
        key_lst = []
        for key, val in new_cont.items():
            if len(val_lst) == len(new_cont):
                break
            val_lst.append(val)
            key_lst.append(key)
        print("\n Here is contact's info:\n")
        i = 0
        while i < len(val_lst):
            print("", f"{key_lst[i]} -- {val_lst[i]}")
            i += 1
        break

    while True:
        try:
            next_step = int(input("\n Do you want to SAVE this contact?"
                                  "\n Yes --> [1] No --> [2]: "))
        except ValueError:
            print("\n Input Error"
                  "\n Use only given numbers to choose")
            continue
        except Exception as error:
            print(f"\n Unexpected error --> {error}"
                  "\n Try again")
            continue

        if next_step == 1:

            with open("contacts_copy.json", "r") as pb:
                old_book = json.load(pb)

            old_book.append(new_cont)

            with open("demo_dict.txt", "w") as wpb:
                json.dump(old_book, wpb)
            quit()
        elif next_step == 2:
            quit()


# ----------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    create_contact()
