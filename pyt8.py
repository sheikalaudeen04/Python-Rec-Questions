def middle_char(s1):
    l= len(s1)
    if l % 2 == 0:
        mid = s1[l // 2 - 1:l // 2 + 1]
    else:
        mid = s1[l // 2]
    return mid

s= input("Enter a string: ")
mc = middle_char(s)
print("Original string: ",s)
print("Middle character(s) of the said string: ",mc)
