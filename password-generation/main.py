import random as rnd
import time
import datetime as dttm
import matplotlib.pyplot as plt
import string
from collections import Counter

# русские строчные и прописные буквы вариант 4

def create_russian_vocabulary():
    return "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

alphabet = create_russian_vocabulary()
alphabet_length = len(alphabet)
cpu_speed = 4_200_000_000 * 8

def visualization(password: string):
    password = sorted(password)
    x = Counter(password).keys()
    y = Counter(password).values()
    plt.plot(x, y)
    plt.show()
    
def time_convert(sec: int):
    return str(dttm.timedelta(sec))
  
def generate_password(length: int):
    password = ''
    for _ in range(length):
        password = password + rnd.choice(alphabet)

    return password

def generate_password_time_decorator(length: int):
    start_time = time.time()
    password = generate_password(length)
    end_time = time.time()
    time_lapsed = (end_time - start_time)
    print(time_lapsed)
    print(f'Elapsed time to generate password \'{password}\' is {time_lapsed} seconds')
    visualization(password)
    return password

def calculate_bruteforce_time(password: string):
    power = pow(len(alphabet), len(password))
    print(f'Average time to crack password of current length(in seconds): {time_convert(power / cpu_speed)}')

def plot_password_length():
    x = [i for i in range(1, 15)]
    y = []

    for i in x:
        y.append(pow(alphabet_length, i) / cpu_speed)
    
    plt.plot(x, y)
    plt.show()


print('input password length:')
length = int(input())
password = generate_password_time_decorator(length)
calculate_bruteforce_time(password)
plot_password_length()