contacts = {}
with open("contacts.txt") as file:
    for line in file:
        (key, val) = line.split(":")
        contacts[key] = val

while True:
    name = input("Enter a contact name or type 'done' to finish: \n")
    if name != "done":
        phone = input(f"Enter a phone number for {name}: ")
        contacts[name + ":"] = phone + '\n'
        with open("contacts.txt", 'w') as file:
            for key, value in contacts.items():
                file.write(f"{str(key)} {str(value)}")
    else:
        break
