PLACEHOLDER = "[name]"

# create letter object
with open ('./Input/Letters/starting_letter.txt') as letter:
    letter = letter.read()

# create list of names
with open('./Input/Names/invited_names.txt') as names_file:
    name_list = names_file.readlines()

# create ready to send Letters
for name in name_list:
    new_name = name.strip()
    ready_to_send = letter.replace(PLACEHOLDER, f'{new_name}' )
    with open(f'./Output/ReadyToSend/letter_to_{new_name}.txt', 'w') as ready_letter:
        ready_letter.write(ready_to_send)
