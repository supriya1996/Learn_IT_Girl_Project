x = int(input("Enter a number:"))
ans = 0
while( ans**3 < x):
   ans += 1
if ans**3 != x:
   print(str(x) + "is not the perfect cube");
else:
   print("cube root of" + str(x) + "is" + str(ans));
