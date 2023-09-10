#coding=UTF-8

def task1():
    print("\n\nЗадание 1")

    num_str = input("Введите натуральное число: ")
    
    isIncreasing = True

    length = len(num_str)
    
    for i in range(length - 1, 0, -1):

        if int(num_str[i]) > int(num_str[i - 1]):
            isIncreasing = False

    if isIncreasing:
        print("Последовательность цифр упорядочена по возрастанию.")
        
    else:
        print("Последовательность цифр не упорядочена по возрастанию.")
        
def task2():
    print("\n\nЗадание 2")

    vowels = "УуЕеЫыАаОоЭэЯяИи"
    consonants = "ЙЦКНГШЩЗХФВПРЛДЖЧСМТБйцкнгшщзхфвпрлджчсмтб"
    
    text = input("Введите текст: ")

    vowelCount = 0
    consonantCount = 0
    wordCount = 0

    words = text.split(' ')

    for word in words:
        
        wordCount += 1
        
        for letter in word:
            
            if letter in vowels:
                vowelCount += 1
                
            elif letter in consonants:
                consonantCount += 1


    print(f"Количество гласных букв: {vowelCount}")
    print(f"Количество согласных букв: {consonantCount}")
    print(f"Количество слов в тексте: {wordCount}")

    if vowels == consonants:
        consonant_set = set()
        for char in text:
            if char.isalpha() and char.lower() not in vowels:
                consonant_set.add(char.lower())
                
        print(f"Согласные буквы в тексте: {' '.join(consonant_set)}")
        
def task3():

    print("\n\nЗадание 3")

    inputStr = input("Введите набор чисел через пробел: ")

    lst = inputStr.split()
    
    pairCounter = 0

    elementDict = {}

    for item in lst:
        
        if item in elementDict:
            pairCounter += 1
            elementDict[item] += 1
            
        else:
            elementDict[item] = 1

    print(f"Количество пар элементов, равных друг другу: {pairCounter}")
    
def task4():
    print("\n\nЗадание 4")

    inputString = input("Введите числовую строку: ")

    digitCountDict = {}
    
    for char in inputString:

        if char.isdigit():
            digit = int(char)

            digitCountDict[digit] = digitCountDict.get(digit, 0) + 1

    print(digitCountDict)

def task5():

    store = {
        "продукт1": [100, 10],
        "продукт2": [200, 5],
        "продукт3": [50, 20],
        "продукт4": [300, 8],
        "продукт5": [150, 15]
    }

    def viewPrice(product_name):
        if product_name in store:
            price = store[product_name][0]
            print(f"{product_name} - Цена: {price} руб.")

    def viewQuantity(product_name):
        if product_name in store:
            quantity = store[product_name][1]
            print(f"{product_name} - Количество: {quantity} шт.")

    def viewAll():
        print("Информация о товарах в магазине:")
        for product_name, [price, quantity] in store.items():
            print(f"{product_name} - Цена: {price} руб., Количество: {quantity} шт.")

    def buyProduct(product_name, amount):

        if product_name in store:

            price = store[product_name][0]

            quantity = store[product_name][1]

            if amount <= quantity:

                total_price = price * amount

                store[product_name][1] -= amount

                print(f"Покупка успешно совершена. Вы купили {amount} шт. {product_name} за {total_price} руб.")
            
            else:
                print(f"Извините, в магазине нет столько {product_name}.")

        else:
            print("Извините, товар не найден.")

    # Основной цикл программы
    while True:

        print("""\nМеню:
        1. Просмотр цены товара
        2. Просмотр количества товара
        3. Вся информация о товарах
        4. Покупка товара
        0. Выход""")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            product_name = input("Введите название товара: ")

            viewPrice(product_name)

        elif choice == "2":
            product_name = input("Введите название товара: ")

            viewQuantity(product_name)

        elif choice == "3":
            viewAll()

        elif choice == "4":
            product_name = input("Введите название товара для покупки: ")

            amount = int(input("Введите количество: "))

            buyProduct(product_name, amount)

        elif choice == "0":
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите пункт меню снова.")

def task6():

    numbers = input("Введите список целых чисел через пробел: ").split(' ')

    numbers.reverse()#или nembers = numbers[::-1]

    uniqueNumbers = set(numbers)

    print("Список уникальных чисел в обратном порядке", uniqueNumbers)

def showMenu():
    while(True):
        print("""\nМеню:
        1. Задание 1
        2. Задание 2
        3. Задание 3
        4. Задание 4
        5. Задание 5
        6. Задание 6
        0. Выход""")

        choice = input("Выберите пункт меню: ")

        if(choice == "1"):
            task1()

        elif(choice == "2"):
            task2()

        elif(choice == "3"):
            task3()

        elif(choice == "4"):
            task4()

        elif(choice == "5"):
            task5()

        elif(choice == "6"):
            task6()

        elif(choice == "0"):
            print("До свидания!")
            break

if __name__ == "__main__":
    showMenu()