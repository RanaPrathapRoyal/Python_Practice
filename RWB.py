'''Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.You must solve this problem without using the library's sort function.
Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
'''
def color_sort(colors):
    lst = []
    #For red color
    for i in colors:
        if i == 0:
            lst.append(i)
    #For whilte color
    for i in colors:
        if i == 1:
            lst.append(i)
    # For Blue color
    for i in colors:
        if i == 2:
            lst.append(i)
    return lst

l = []
Data = int(input("Enter the number of colors in a list : "))
for i in range(0,Data):
    Data1 = int(input("Enter the input list : "))
    l.append(Data1)

print(type(Data1))
print(f"Input list : {l}")
Result = color_sort(l)
print(f"Sorted list : {Result})
