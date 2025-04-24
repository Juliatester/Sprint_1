world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}
world_champions[2022] = 'Аргентина'
italy_won = False
for key,value in world_champions.items():
    print(f'{key} - {value}')

for key,value in world_champions.items():
    country = 'Италия'
    if value == 'Италия':
        italy_won = True
        if italy_won:
            print('Италия становилась чемпионом мира по футболу в 21 веке!')
        else:
            print('Италия не выигрывала чемпионат мира по футболу в 21 веке.')