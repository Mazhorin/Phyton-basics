user_num = int(input("введите числовой ряд для нахождения бОльшего числа в этом ряду"))
ost_num = user_num
max_num = 0
while ost_num >= 1:
    number = int(ost_num % 10)
    ost_num = ost_num // 10
    if max_num < number:
        max_num = number
print("Максимальное число в ряду ", user_num, "- ", max_num)