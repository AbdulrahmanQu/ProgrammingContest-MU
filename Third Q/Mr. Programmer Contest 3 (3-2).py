
#برنامج يستقبل عدد صحيح عشري N ,يقوم بالتحويل العدد N من عدد عشري الى ست عشري
#0 <= N <=1000000
#lower case letters
#*المدخلات*
#عدد عشري N
#*المخرجات*
#عدد ست عشري



number = int(input("Enter a number with base 10\n"))
print("Hexadecimal form of " + str(number) + " is " + hex(number).lstrip("0x").rstrip("L"))
