from commands import add_contact, change_contact, show_phone, show_all, delete_contact
from parser import parse_input

def main():
    contacts = {
        "Andrii": "48788083792"
    }
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))   
        elif command == "delete":
            print(delete_contact(args,contacts)) 
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
