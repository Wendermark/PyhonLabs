
def isPrime(x):
    if x <= 1:
        return False
    
    elif x <= 3:
        return True
    
    elif x % 2 == 0 or x % 3 == 0:
        return False
    
    i = 5

    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6

    return True

def typeDependentCalc(x):

    t = type(x)

    if(t is list):
        print(f"Длина всех слов в списке: {sum([len(i) for i in x])}")

    elif(t is int):
        print(f"Число наоборот: {str(x)[::-1]}")

    elif(t is tuple):
        print(f"Кол-во букв: {sum([len(i) for i in x if type(i) is str])}\t Кол-во чисел: {len([i for i in x if type(i) is int])}")

    elif(t is str):
        print(f"Сумма цифр в строке: {sum([int(i) for i in x if i.isdigit()])}")

    else:
        print("Передан неподдерживаемый тип данных!")

def isSymmetric(matrix):

    n = len(matrix)

    if n != len(matrix[0]):
        return False

    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != matrix[j][i]:
                return False

    return True

def tryExceptShowcase(i):

    x = 0

    try:
        print(x / i)

    except ZeroDivisionError:
        print("Ошибка деления на 0!")

    finally:
        print("Отработал finally")


print(isPrime(13))
print()
print(isPrime(2))
print()
print(isPrime(22))

input()

typeDependencyCalc(["as", "asd", "asdf"])
print()
typeDependencyCalc(456123)
print()
typeDependencyCalc((1, 2, 3, "ff", "f"))
print()
typeDependencyCalc("1239")

input()

tryExceptShowcase(1)
print()
tryExceptShowcase(0)
print()
