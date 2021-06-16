orig_time = int(input('введите секунды для перевода в формат "чч:мм:сс"'))
all_sec = orig_time
sec = all_sec % 60
ostatok = all_sec // 60
print("Вот столько секунд, не входящих в минуты: ", sec)
min = ostatok % 60
ostatok = ostatok / 60
print("Вот столько минут, не входящих в часы", min)
hours = int(ostatok)
print("вот столько часов: ", hours)
print(f"переводим в привычный формат: {hours:02}:{min:02}:{sec:02}")