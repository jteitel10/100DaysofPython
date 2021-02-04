import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# create a csv that has a small table of fur color, count
fur_color = data['Primary Fur Color']

grey_squirrel_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrel_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrel_count = len(data[data['Primary Fur Color'] == 'Black'])

data_dict = {
    'Fur Color' : ['Gray', 'Red', 'Black'],
    'Count' : [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}
squirrel_data = pandas.DataFrame(data_dict)
squirrel_data.to_csv('squirrel_count.csv')
