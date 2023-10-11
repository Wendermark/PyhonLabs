def task1():

    def count_consonants(text):

        consonants = "bcdfghjklmnpqrstvwxyz"

        count = 0

        for char in text:

            if str(char).lower() in consonants:
                count += 1

        return count
    
    with open('F1.txt', 'w') as f1:
        
        while True:

            line = input("Введите строку (пустая строка для завершения ввода): ")
            
            if not line:
                break

            f1.write(line + '\n')

    N = int(input("Введите начальный индекс строки (N): "))
    K = int(input("Введите конечный индекс строки (K): "))

    with open('F1.txt', 'r') as f1, open('F2.txt', 'w') as f2:

        lines = f1.readlines()

        for i in range(N - 1, min(K, len(lines))):
            f2.write(lines[i])

    with open('F2.txt', 'r') as f2:
        print(f"Количество согласных букв в файле F2: {count_consonants(f2.read())}")

def task2():

    with open("task2.txt", 'a'):
        pass

    with open("task2.txt", 'r') as f:
        lines = f.readlines()

    for line in lines:

        marks = line.split()[1:]
        
        avg_mark = sum(int(i) for i in marks) / len(marks)

        line = line.removesuffix('\n')

        print(f"""{line}, ср. балл - {avg_mark}""")
            
def task3():

    subjects = { }

    with open("task3.txt", 'a'):
        pass

    with open("task3.txt", 'r') as f:
        lines = f.readlines()

    for line in lines:

        subject_info = line.split(':')

        subject_name = subject_info[0]

        subjects[subject_name] = [int(subject_info[1]), int(subject_info[2]), int(subject_info[3]), 0]

        subjects[subject_name][3] = sum(subjects[subject_name])

    for k, v in subjects.items():
        print(f"Предмет: {k}, Лекций: {v[0]}, Практических: {v[1]}, Лабораторных: {v[2]}, Всего - {v[3]}")

def task4():

    import json

    with open("task4.txt", 'a'):
        pass

    with open('task4.txt', 'r') as f:
        lines = f.readlines()

    result_list = []

    total_profit = 0

    average_profit = 0

    for line in lines:
        name, revenue, costs = line.split()

        profit = int(revenue) - int(costs)

        if profit > 0:
            total_profit += profit

        result_list.append({'name': name, 'profit': profit})

    companies_count = len(result_list)

    if companies_count > 0:
        average_profit = total_profit / companies_count

    result_list.append({'average_profit': average_profit})

    with open('task4Result.json', 'w') as f:
        json.dump(result_list, f)

def menu():

    while(True):
        print("""\nМеню:
        1. Задание 1
        2. Задание 2
        3. Задание 3
        4. Задание 4
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

        elif(choice == "0"):
            print("До свидания!")
            break

menu()