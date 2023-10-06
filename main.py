#напишите программу для бинарного поиска загаданного числа

def binary_search():
    min_num = 0
    max_num = 100
    center = (min_num+max_num)//2

    while True:
    print(f"это число {center}?")
        check = input("Если число больше, то поставьте >." "если число <. Если равно =")
    if check == "=":
        print("Я угадал")
        breakpoint
    elif chek == ">":
        min_num = center
        center = (min_num + max_num) // 2
        elif check == ">":
            max_num = center
            center = (min_num + max_num)//2
    else:
        print("я не знаю это число")