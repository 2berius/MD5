import string
from itertools import product
import hashlib
from colorama import Fore


def main(message, start, min, max):
    letters = string.ascii_letters + string.digits + "!@#$%&*"

    while min <= max:
        for word in map(''.join, product(letters, repeat=min)):
            new = start + word
            md5 = hashlib.md5(new.encode('utf-8')).hexdigest()

            if md5 == message:
                print(Fore.GREEN +
                      f'\nMD5 Hash:   {Fore.GREEN + md5}   {Fore.GREEN + new}')
                quit()
            print(Fore.RED + f'MD5 Hash:   {md5}   {new}')
        min += 1


if __name__ == "__main__":
    start = input("Enter what you know: ")
    message = input("Hash Message: ").lower()
    msg_min = int(input("Min # of chars in message after what you entered:"))
    msg_max = int(input("Max # of chars in message after what you entered:"))
    main(message, start, msg_min, msg_max)
