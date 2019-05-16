user = int(input("How many numbers ? :"))

result = []
for i in range(user):
    
    n = int(input("Enter the number {} : ".format(i+1)))
    
    rev = 0
    fd = 0
    s = 0
    
    ld = n % 10
    
    while n > 0:
        
        r = n % 10
        rev = rev * 10 + r
        n = int(n / 10)
        fd = rev % 10
    
    
    s = fd + ld
    
    result.append(s)


for j in range(len(result)):
    print("\nSum of first and last digit is of number {} is :".format(j+1), result [j])



#the current output (only prints the last index):
#
#How many numbers ? :3
#Enter the number 1 : 456
#Enter the number 2 : 678
#Enter the number 3 : 432
#('\nSum of first and last digit is of number 1 is :', 6)
#('\nSum of first and last digit is of number 2 is :', 6)
#('\nSum of first and last digit is of number 3 is :', 6)
#
#the expected output:
#
#How many numbers ? :3
#Enter the number 1 : 456
#Enter the number 2 : 678
#Enter the number 3 : 432
#('\nSum of first and last digit is of number 1 is :', 10)
#('\nSum of first and last digit is of number 2 is :', 14)
#('\nSum of first and last digit is of number 3 is :', 6)
