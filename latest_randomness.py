import requests
import json

#To get the latest randomness from cloudflare:
r = requests.get('https://drand.cloudflare.com/public/latest', headers={ 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = r.json()
latest_randomness= data["randomness"]

#Digits is a list containing the hex's individual digits:
digits = list(latest_randomness.strip(' '))

num_length = len(digits)

#Pairs is a list containing the pairs of digits that will later be converted:
pairs = [digits[i] + digits[i+1] for i in range(0, num_length-1, 2)]

if (num_length % 2 == 1):
    pairs.append(digits[num_length-1])

#Converts hex pairs to integers modulo 80:
for i in range(len(pairs)):
    pairs[i]= int(pairs[i],16) % 80
    
#To remove any duplicate numbers:
pairs= list(set(pairs))

#To get the last KINO winning numbers from the given link
req=requests.get("https://api.opap.gr/draws/v3.0/1100/last-result-and-active")
data=req.json()
kino_numbers= data["last"]["winningNumbers"]["list"]

count=0 #How many of the pairs' numbers would win in the last KINO drawing

for i in range(len(pairs)):
     for k in range(len(kino_numbers)):
         if (pairs[i]==kino_numbers[k]):
             count+=1
             kino_numbers.pop(k) #If a number is found, remove it to make the search faster
             break
     continue

print("{} of the generated numbers would win in the last KINO drawing".format(count))