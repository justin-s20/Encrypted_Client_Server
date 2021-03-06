"""
    add_user.py - Stores a new username along with salt/password

    CSCI 3403
    Authors: Matt Niemiec and Abigail Fernandes
    The solution contains the same number of lines (plus imports)
    Group Memebers:
    Gunther Wallach, Andrew Hack, Justin Sperry
"""

import hashlib
import os
import string
from random import randint
import random

#print(hashlib.algorithms_available)
#print(hashlib.algorithms_guaranteed)

user = input("Enter a username: ")
password = input("Enter a password: ")

# TODO: Create a salt and hash the password DONE
salt = hashlib.sha512(os.urandom(90)).hexdigest().encode('ascii')
hashed_password = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
salt = salt.decode()
hashed_password = hashed_password.decode()

try:
    reading = open("passfile.txt", 'r')
    for line in reading.read().split('\n'):
        if line.split('\t')[0] == user:
            print("User already exists!")
            exit(1)
    reading.close()
except FileNotFoundError:
    pass

with open("passfile.txt", 'a+') as writer:
    writer.write("{0}\t{1}\t{2}\n".format(user, salt, hashed_password))
    print("User successfully added!")
