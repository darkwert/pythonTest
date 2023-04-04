setOfNumber = []
mostValue = 0

while True:
    number = input("Enter number('d' when done):")
    if(number == 'd'):
        break
    else:
        setOfNumber.append(int(number))
        
for i in range(len(setOfNumber)):
    if mostValue < setOfNumber[i]:
        mostValue = setOfNumber[i]

print(mostValue)