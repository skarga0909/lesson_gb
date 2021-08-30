weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(weather)
weather_new = []
for word in weather:
    if word.isdigit():
        weather_new.append('"')
        word = int(word)
        word = f'{word:02d}'
    weather_new.append(word)
    if word.isdigit():
        weather_new.append('"')
print(weather_new)

weather_str = ' '.join(weather_new)
print(weather_str)
