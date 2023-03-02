def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
s = input()
print("The reversed string is:")
print(reverse(s))

'''
input:
vsdevelopers
output:
The reversed string is:
srepolevedsv
'''
