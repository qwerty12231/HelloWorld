seasons = {"Winter": (1, 2, 12),
           "Sping": (3, 4, 5),
           "Summer": (6, 7, 8),
           "Autumn": (9, 10, 11)}

month = int(input('Enter please number mounth: '))
for key in seasons.keys():
    if month in seasons[key]:
        print(key)


