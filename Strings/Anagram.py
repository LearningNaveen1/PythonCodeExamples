def checkAnagram(str1, str2):

    len1 = len(str1)
    len2 = len(str2)

    if(len1 != len2):
        return 0

    str1 = sorted(str1)
    str2 = sorted(str2)

    # Return 0 - Return false and Return 1 - True
    for i in range(0,len1):
        if(str1[i] != str2[i]):
            return 0
    return 1

# Taking input from console

str1 = str(input())
str2 = str(input())

print(checkAnagram(str1,str2))
