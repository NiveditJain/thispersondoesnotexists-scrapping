import requests
import string
import random
import os

base = string.ascii_letters + string.digits


def main():
    response = requests.request('GET', 'https://thispersondoesnotexist.com/image')

    file_name = ''.join(random.choice(base) for _ in range(32)) + '.jpeg'

    with open(file_name, 'wb') as file:
        file.write(response.content)

    print(f'Saved file {file_name}')


for j in range(1, 100000):
    os.mkdir(str(j))
    os.chdir(str(j))

    for i in range(1, 100):
        main()

    os.chdir('..')
