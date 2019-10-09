
#1) Python Program for Linear Search
#Problem: Given an array arr[] of n elements, write a function to search a given element x in arr[].
#Examples :

#Input : arr[] = {10, 20, 80, 30, 60, 50, 110, 100, 130, 170}
 #         x = 110;
#Output : 6
#Element x is present at index 6

#Input : arr[] = {10, 20, 80, 30, 60, 50, 110, 100, 130, 170}
 #          x = 175;
#Output : -1
#Element x is not present in arr[].
#A simple approach is to do linear search, i.e

#Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
#If x matches with an element, return the index.
#If x doesn’t match with any of elements, return -1.

#Example:linear-search1

#filter_none
#edit
#play_arrow

#brightness_4
# Searching an element in a list/array in python 
# can be simply done using \'in\' operator 
# Example: 
# if x in arr: 
#   print arr.index(x) 
  
# If you want to implement Linear Search in python 
  
# Linearly search x in arr[] 
# If x is present then return its location 
# else return -1 
  
"""def linear_search(arr, x): 
  
    for i in range(len(arr)): 
  
        if arr[i] == x: 
            return i 
  
    return -1"""
#The time complexity of above algorithm is O(n) and space complexity is 0(1)

#How to test:(Python Shell)
#arr = [10, 20, 80, 30, 60, 50,110,100,130,170]
#x = 110
#linear_search(arr, x)


"""def linear_search(arr,x):
    i = 0
    while i<len(arr):
        if arr[i] == x:
            return i
        else:
            i = i +1
    return False
    

def binary_search(arr, x):

    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left + right)//2 
        if arr[mid] == x:
            return mid
        if arr[mid] < x:
            left = mid + 1

        else:
            right = mid -1
    return -1

#How to test in the shell:
#print(binary_search([1,2,3,5,8], 3))
#print(linear_search([10,20,80,30,60,50,110,100,130,170], 110))


#anotherway:
def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found
	
print(binary_search([1,2,3,5,8], 6))
print(binary_search([1,2,3,5,8], 5))


#Selection Sort in Python
#Python code to Implement Selection Sort. This Algorithm is very simple. Find the smallest element in the array and swap it. That's all you will get a sorted list at the end.

 
array = [1,45,10,35,100,13,147,500,80]
#def selection_sort(array)
size = len(array)
for i in range(0,size):
    for j in range(i+1,size):
        if array[j] < array[i]:
            min = array[j];
            array[j] = array[i];
            array[i] = min;
print(array)


#How to test: print( selection_sort([120,11,0,1,3,2,3,4,5,6,7,8,9,10]) )

list=[5,4,3,1,6,8,10,9]
list_sorted=[]
for i in range(len(list)):
    x = min(list)
    list.remove(x)
    list_sorted.append(x)
print(list_sorted)
"""

# Python program for implementation of Bubble Sort
#arr =[5,4,3,1,6,8,10,9]
def bubble_sort(arr):
    l = len(arr)        
    for i in range(l):
        for j in range(l-1):
            if (arr[i] < arr[j]):
              arr[i], arr[j] = arr[j], arr[i]
    return arr

#How to test:
#print(bubble_sort([5,4,3,1,6,8,10,9]))
#[1, 3, 4, 5, 6, 8, 9, 10]

def bubble_sort(list):
    for i in range(len(list)):
        for j in range(i, len(list)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    return list

#Test example:

#a = [8,1,2,4,1,3,5,1,5,6,1,8]
#bubble_sort(a)
# Result:

#[1, 1, 1, 1, 2, 3, 4, 5, 5, 6, 8, 8]

#Reverse word in a sentence:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
class Solution:
	def reverseWords(self, s: str) -> str:
        
		s = s.split(' ')        # It will create a list of words
        
		reverse = []        # reversed words will be stored here
		for word in s:
			reverse.append(word[::-1])      # adds reversed word to the reverse list

		result = ' '.join(reverse)      # It will join words with a space

		return result


# How to test in shell:
#s = "Let's take LeetCode contest"
#l =s.split()
# l = ["Let's", 'take', 'LeetCode', 'contest']
# reverse each item in the list l.
# reverse = []
# for i in l:
	#r = i[::-1]
	#reverse.append(r)
# reverse = ["s'teL", 'ekat', 'edoCteeL', 'tsetnoc']
# build the string by using the item in the list.
# res = " ".join(i for i in reverse)
# res = "s'teL ekat edoCteeL tsetnoc"


#Linear search i python with a given list

"""items = [5, 7, 10, 12, 15]
 
print("list of items is", items)

x = int(input("enter item to search:"))
 
i = flag = 0
 
while i < len(items):
	if items[i] == x:
		flag = 1
		break
 
i = i + 1
 
if i == 1:
	print("item found at position:", i + 1)
else:
	print("item not found")

"""

#Anotherway:
"""

def linear_search(x, mylist):
  found = False

  for i in range(len(mylist)):
    if x == mylist[i]:
      found=True
      break
    else:
      if x not in mylist:
        break

  if found == False:
    print("Not found")
  else:
    print("Found in position",i)
    
mylist=[2,3,4,5,6]
x = int(input("Enter a number: "))
linear_search(x,mylist)
"""


# Python program to find minimum depth of a given Binary Tree 
class Node: 
    def __init__(self , key):  #The sole purpose of __init__ is to initialize the values of instance members for the new object
        self.data = key  
        self.left = None
        self.right = None
  
def minDepth(root): 
    # Corner Case.Should never be hit unless the code is  
    # called on root = NULL 
    if root is None: 
        return 0 
      
    # Base Case : Leaf node.This acoounts for height = 1 
    if root.left is None and root.right is None: 
        return 1
      
    # If left subtree is Null, recur for right subtree 
    if root.left is None: 
        return minDepth(root.right)+1
      
    # If right subtree is Null , recur for left subtree 
    if root.right is None: 
        return minDepth(root.left) +1 
      
    return min(minDepth(root.left), minDepth(root.right))+1
  
# Driver Program  
"""root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
print minDepth(root)
"""


#Linear search i python with a given list

"""items = [5, 7, 10, 12, 15]
    
    print("list of items is", items)
    
    x = int(input("enter item to search:"))
    
    i = flag = 0
    
    while i < len(items):
    if items[i] == x:
    flag = 1
    break
    
    i = i + 1
    
    if i == 1:
    print("item found at position:", i + 1)
    else:
    print("item not found")
    
    """

#Anotherway:

def linear_search(x, mylist):
    found = False
        
        for i in range(len(mylist)):
            if x == mylist[i]:
                found=True
                    break
else:
    if x not in mylist:
        break
            
            if found == False:
print("Not found")
    else:
    print("Found in position",i)

mylist=[2,3,4,5,6]
x = int(input("Enter a number: "))
linear_search(x,mylist)
        
        









   

    
            
        







    
