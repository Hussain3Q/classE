

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
print('.')
print('.')
print('.')



num_lines = 0
with open('./wordlist.txt', 'r') as f:
    for line in f:
        num_lines += 1

j=0
i=1
wordlist = open('./wordlist.txt', 'r')
for word in wordlist:
    r = requests.get(url+ word.strip())
    j +=1
    if r.status_code == 200:
        print(i,"- ",r.url,"............",'{0:.2f}%'.format(j*100/num_lines))
        i +=1
        
        
