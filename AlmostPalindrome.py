import string
def checkpalindrome(n): # Checks wether a string can be made palindrome by swapping letters or not.
    count = 0
    z = len(n) - 1
    mp=dict.fromkeys(string.ascii_lowercase,0)
    if n ==n[::-1]:
        return "YES"
    memo = []
    for i in range(len(n)//2):
        if n[i] != n[z]:
            count += 1
            memo.append(i)
        mp[n[i]] += 1
        z -= 1    
    if count > 2:
        return "No"
    if count == 2:
        return "Yes"
    if count == 1 and len(n) % 2 == 0:
        return "No"
    if count == 1 and len(n) % 2 == 1:
        return "Yes"
    if count == 0:
        return "Yes"

x = checkpalindrome('axax')
print(x)
