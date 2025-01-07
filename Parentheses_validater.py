'''Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring
Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0'''

def parentheses_validator(Data):
    cb_count = 0
    ob_count = 0
    l = []
    minimum = ""
    for i in Data:
        if i == ")":
            cb_count += 1
        elif i == "(":
            ob_count += 1
    print(f"{ob_count} = ob_count")
    print(f"{cb_count} = cb_count")
    if cb_count == 0 or ob_count == 0:
        print("Parentheses substring Not possible with the given String")
    l.append(ob_count)
    l.append(cb_count)
    print(l)
    minimum = min(l)
    print(minimum)
    if minimum >0:
        len = 2*minimum
        print(f"Length of valid parenthese : {len}")
        print("And the output string is :")
    for i in range(0,minimum):
        print("()", end="")


Data =  str(input("Enter the string : "))
Result = parentheses_validator(Data)
#print(Result)
