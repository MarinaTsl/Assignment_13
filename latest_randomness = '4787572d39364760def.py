latest_randomness = '4787572d39364760def4802effe4e576a131def40fc80b9af36de29bbfcfd105'

digits = list(latest_randomness.strip(' '))

num_length = len(digits)

pairs = [digits[i] + digits[i+1] for i in range(0, num_length-1, 2)]


if num_length % 2 == 1:
    pairs.append(digits[num_length-1])

print(pairs)