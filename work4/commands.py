def add_contact(args, contacts):
    if len(args) != 2:
        return "Error: You must provide a name and a phone number."
    name, phone = args
    contacts[name] = phone
    return f"Contact '{name}' has been added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Error: You must provide a name and a new phone number."
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Contact '{name}' has been updated with the new phone number."
    else:
        return f"Error: Contact '{name}' not found."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Error: You must provide a valid name."
    name = args[0]
    if name in contacts:
        return f"The phone number for '{name}' is: {contacts[name]}"
    else:
        return f"Error: Contact '{name}' not found."


def show_all(contacts):
    if not contacts:
        return "You have no saved contacts."
    else:
        result = "Saved contacts:\n"
        for name, phone in contacts.items():
            result += f"- {name}: {phone}\n"
        return result.strip()


def delete_contact(args, contacts):
    if len(args) != 2:
        return "Error: You must provide a name and a phone number to delete."
    name, phone = args
    if name in contacts and contacts[name] == phone:
        del contacts[name]
        return f"Contact '{name}' has been deleted."
    elif name in contacts:
        return f"Error: The phone number provided for '{name}' does not match."
    else:
        return f"Error: Contact '{name}' not found."
