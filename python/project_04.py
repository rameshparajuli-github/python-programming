'''Write a program to find out wheather a students is pass or fail , if it require total 40% and 
at least 33% in each subject to pass . Assume 3 subject and take marks as an input from 
the user '''
sub1=  int(input("Enter the English marks: "))
sub2=  int(input("Enter the Maths marks: "))
sub3=  int(input("Enter the Computer marks: "))
 
if (sub1<33 or sub2<33 or sub3<33):
    print("Your are fail due to your are getting less then 33 marks in one subject ")
elif (sub1 + sub2 + sub3)/3 <40:
    print("Your are fail due to your are getting total marks less then 40 ")
else:
    print("Congratulation your are pass ")



