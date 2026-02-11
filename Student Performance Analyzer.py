name="john chrysolite"
valid=0
count=0
n=int(input("Enter No. of Students:"))
marks=[0]*n
for i in range(n):
    marks[i]=int(input("Enter the marks:"))
    if len(name)>6 :
        marks[i]=marks[i]+5

    else:
        marks[i]=marks[i]-5
    if 0<=marks[i]<=100:
        valid = valid + 1

for i in range(n):
    if 90<=marks[i]<=100:
        print(marks[i],"-> Excellent")
    if 75<=marks[i]<=89:
        print(marks[i],"-> Very Good")
    if 60<=marks[i]<=74:
        print(marks[i],"-> Good")
    if 40<=marks[i]<=59:
        print(marks[i],"-> Average")
    if 0<=marks[i]<=39:
        print(marks[i],"-> fail")
        count=count+1
    if marks[i]>100 or marks[i]<0:
        print(marks[i],"->Invalid")
print("Total Valid Students:",valid)
print("Total Fail Students:",count)
