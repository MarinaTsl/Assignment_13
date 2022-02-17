latest_randomness = '4787572d39364760def4802effe4e576a131def40fc80b9af36de29bbfcfd105'

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


