numbers = list()
a = int(input("Enter how many numbers: "))
for i in range(0, a):
    inputNr = int(input("Enter a number: "))
    numbers.append(inputNr)

sum = 0
for j, val in enumerate(numbers):
    sum += val
print("The total sum is: " + str(sum))
