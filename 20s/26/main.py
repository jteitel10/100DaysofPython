import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}

def phonetic_generate():
    user_input = input("Enter a word:\n").upper()
    try:
        phonetic_list = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        phonetic_generate()
    else:
        print(phonetic_list)


phonetic_generate()
