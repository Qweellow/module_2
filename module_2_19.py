def find_password(n):
    result = ""

    for i in range(1, 21):
        for j in range(i + 1, 21):
            if i + j == n:
                if n % (i + j) == 0:
                    result += str(i) + str(j)
    return result

# Пример использования:
n = int(input('Введите число от 3 до 20: '))
password = find_password(n)
print('Нужный пароль:', password)
