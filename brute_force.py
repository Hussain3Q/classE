
import os, sys, time
import requests



print()
print('============================================')
print("=     Brute force attack for web pages     =")
print('=                Class E                   =')
print('=           By Basil & Hussain             =')
print('============================================')


print()
print()
print()
url= input("Enter your target website: ")
print()
print()
print()

wordlist = open('./wordlist.txt', 'r')
for word in wordlist:
    r = requests.get(url+ word.strip())
    if r.status_code == 200:
        print(r.url)
