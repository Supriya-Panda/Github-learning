#Python Program to Find the Largest Number in a List

list1 = [10, 20, 4, 45, 99] 
# sorting the list 
list1.sort()
print(list1)
# printing the largest or last element 
print("Largest element is:", list1[-1]) 
print("Largest element is:", max(list1)) 

print("--------------------------------------------------------------------------------------------------------")

#Python Program to Find the Second Largest Number in a List

list1 = [10, 20, 45, 4, 99] 
# sorting the list 
list1.sort()   
# printing the 2nd largest or last element 
print("Largest element is:", list1[-2])

print("--------------------------------------------------------------------------------------------------------")

#Python Program to Merge Two Lists and Sort it

list1 = [10, 20, 4, 5, 99] 
list2 = [100, 12, 40, 7, 15] 
list3=list1+list2
# sorting the list 
list3.sort()   
print(list3)
print("--------------------------------------------------------------------------------------------------------")

#Python Program to Swap the First and Last Value of a List

list = [100, 12, 40, 7, 15] 
list[0],list[-1]=list[-1],list[0]
print(list)
