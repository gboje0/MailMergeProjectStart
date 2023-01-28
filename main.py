PLACEHOLDER = "[name]"

with open("./input/names/invited_names.txt") as name_file:
    guest_names = name_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in guest_names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt",mode="w") as complete_letter:
            complete_letter.write(new_letter)

with open("./Output/ReadyToSend/letter_for_Sokka.txt") as letter:
    view = letter.read()
    print(view)