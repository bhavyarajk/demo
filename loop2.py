#FOR LOOP
n=[1,2,3,4]
for i in n:
    print(i,end=" ")
print()
s="hello"
for i in s:
    print(i,end=" ")
print()
#Print Numbers from 1 to 100
for i in range(1,101):
    print(i,end=" ")
print()
#print odd numbers from 1 to 100
for i in range(1,101,2):
    print(i,end=" ")
#sum of first 10 numbers
s=0
for i in range(1,11):
    s=s+i
print(s)
#product of first 10 even numbers
# s=1
# for i in range(2,21,2):
#     s=s*i
# print(s)
s=1
for i in range(1,21):
    if(i%2==0):
        s=s*i
print(s)
#print those elemnts which are divisble by 7 and 5 in the range 1500,2700
for i in range(1500,2701):
    if(i%7==0 and i%5==0):
        print(i)