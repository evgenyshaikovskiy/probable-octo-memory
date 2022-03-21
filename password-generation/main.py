import random as rnd
import datetime as dttm
import matplotlib.pyplot as plt
from collections import Counter


def create_russian_vocabulary():
    return "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


alphabet = create_russian_vocabulary()
alphabet_length = len(alphabet)
cpu_speed = 4_200_000_000 * 8


def visualization(password):
    password = sorted(password)
    x = Counter(password).keys()
    y = Counter(password).values()
    plt.plot(x, y)
    plt.show()


def generate_password(length):
    password = ''
    for _ in range(length):
        password += (rnd.choice(alphabet))

    return password


def generate_multiple_passwords(length, count):
    passwordConcat = ""
    start_time = dttm.datetime.now()
    for _ in range(count):
        passwordConcat += generate_password(length)

    end_time = dttm.datetime.now()

    print(f'Time taken to generate {count} passwords: {end_time - start_time}')
    visualization(passwordConcat)

    # pass random password of given length
    return generate_password(length)


def calculate_bruteforce_time(password):
    power = pow(len(alphabet), len(password))
    seconds = power / cpu_speed
    print(f'''Average time to crack password
          of current length: {seconds} seconds''')


def plot_password_length():
    x = [i for i in range(1, 10)]
    y = []

    for i in x:
        y.append(pow(alphabet_length, i) / cpu_speed)

    plt.plot(x, y)
    plt.show()


print('input password length:')
length = int(input())

print('input count of passwords to generate:')
count = int(input())

password = generate_multiple_passwords(length, count)
calculate_bruteforce_time(password)
plot_password_length()
