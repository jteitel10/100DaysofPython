import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}

user_input = input("Enter a word:\n").upper()
phonetic_list = [nato_dict[letter] for letter in user_input]
print(phonetic_list)
