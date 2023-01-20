import json


def delete_contact():
    with open(r"C:\Users\stlrv\OneDrive\Python\GitHub RepClones\python_beetroot_Nikita_Stolyarov\HW_11\PhoneBook "
              r"App\phonebook.json", "r") as pb:
        phone_book = json.load(pb)
    # Searchin contact by number
    key_lst = []
    val_lst = []
    contact_dict = {}
    i = 0
    while True:
        number = input("\n Please, enter contact's number: ")
        for contact in phone_book:
            if number == contact["Number"]:
                contact_dict = contact
                break
            else:
                continue
        if contact_dict == {}:
            print("\n There is NO contact with this number")
            continue
        else:
            for key, val in contact_dict.items():
                if len(val_lst) == len(contact_dict):
                    break
                val_lst.append(val)
                key_lst.append(key)

        print("\n Here is contact's info:\n")
        while i < len(val_lst):
            print("", f"{key_lst[i]} -- {val_lst[i]}")
            i += 1
        break

    while True:
        try:
            next_step = int(input("\n Do you want to DELETE this contact?"
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
            phone_book.remove(contact_dict)
            with open(
                    r"C:\Users\stlrv\OneDrive\Python\GitHub RepClones\python_beetroot_Nikita_Stolyarov\HW_11\PhoneBook "
                    r"App\phonebook.json", "w") as pb:
                json.dump(phone_book, pb)
                quit()
        elif next_step == 2:
            quit()


# Functions test ------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    delete_contact()
