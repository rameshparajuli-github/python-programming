from functools import reduce
sum =lambda a, b: a + b
ls= [1, 2 ,3 ,4]    # firts 1 rw 2 sum huncha =3 , first  ans 3 rw 3 sum huncha =6 aane second ko ans 6 rw 4 =10 ..... 2 ota ko sequence ma sum garcha 
val= reduce(sum,ls)
print(val)