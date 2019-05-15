
#اكتب برنامج يستقبل مجموعة من الاعداد  الصحيح N ثم يقوم بطباعة مجموع اول واخر خانة  من عدد N
#0 < T <= 100
#0 <= N <= 1000000
#*المدخلات*
#T عدد صحيح يساوي عدد حالات الاختبار
#N الاعداد الصحيحة
#*المخرجات*
#    مجموع اول واخر خانة  من العدد N


user = int(input("How many numbers ? :"))

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

print("\nSum of first and last digit is of number {} is :".format(i+1), s)
