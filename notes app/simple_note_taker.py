
with open("notes.txt", 'r') as file:
    notes = file.readlines()


while True:
    choice = int(input("Menu:\n"
                       "1. Add a note\n"
                       "2. View all notes\n"
                       "3. Exit\n"
                       "Chose an option (1,2, or 3):  "))

    match choice:
        case 1:
            new_note = input("Enter your note: ")
            notes.append(new_note + "\n")
            with open("notes.txt", 'w') as file:
                file.writelines(notes)
        case 2:
            if len(notes) < 1:
                print("No Notes to view.")
            else:
                print("Note List:")
                for note in notes:
                    note.strip('\n')
                    print(f"-{note}")
        case 3:
            break
