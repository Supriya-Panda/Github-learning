#1st program
dictionary = { 1: 'one', 2:'two', 3:'three' }
dictionary['ONE'] = dictionary.pop(1)
print(dictionary)
print("---------------------------------------------------------------")



#2nd program
l=[11,45,8,11,23,45,23,45,89]
o={x:l.count(x) for x in l}
print(o)
print("---------------------------------------------------------------")




#3rd program
SampleList=[87,45,41,65,94,41,99,94]
print(SampleList)
res = [] 
[res.append(x) for x in SampleList if x not in res] 
print("After removing the duplicate values:"+str(res))
print("tuple:",tuple(res))
print("maxmium value:",max(res))
print("minimum value:",min(res))
print("---------------------------------------------------------------")




#4th program
def showEmployee(name,salary=50000):
    print("Employee ", name ," salary is:",salary)
def main():
    showEmployee("Eddy",40000)
    showEmployee("Ramu")
main()
print("---------------------------------------------------------------")




#5th program
def outerFunction(a,b):
    def innerFunction():
        return a+b
    x= innerFunction()
    print("actual output is:",x)
    x=x+5
    return x
z=outerFunction(5,10)
print("added output is:",z)
print("---------------------------------------------------------------")




#6th program
def recur(n):  
   if n <= 1:  
       return n  
   else:  
       return(recur(n-1) + recur(n-2))  
nterms = int(input("How many terms: "))  
if nterms <= 0:  
   print("Plese enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(nterms):  
       print(recur(i))      
print("---------------------------------------------------------------")




#7th program
def displayStudent(name, age):
    print(name, age)
displayStudent("Emma", 26)
showStudent = displayStudent
showStudent("Emma", 26)
print("---------------------------------------------------------------")


#8th program
import re 
def isValid(s):   
    Pattern = re.compile("[6-9][0-9]{9}") 
    return Pattern.match(s)   
count=0
while count == 0:
    s =input("Enter any 10 digit number:")
    if (isValid(s)):
        print ("Valid Number")
        count+=1
    else : 
        print ("Invalid Number")
print("---------------------------------------------------------------")




#9th program
def string(s):
    d={"upperCase":0, "lowerCase":0}
    for c in s:
        if c.isupper():
           d["upperCase"]+=1
        elif c.islower():
           d["lowerCase"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["upperCase"])
    print ("No. of Lower case Characters : ", d["lowerCase"])

string('The quick Brown Fox')
print("---------------------------------------------------------------")




#10th program
n = int(input("Enter any number: "))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")



































































