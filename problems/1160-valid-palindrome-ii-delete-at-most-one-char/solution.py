def valid_palindrome(s):
    # s: a string of lowercase letters
    # return True or False
    if len(s)==0:
        return "True"
    for pointer in range(len(s)):
        candidate_palindrome = s[:pointer] + s[pointer+1:]
        if candidate_palindrome[::-1] == candidate_palindrome:
            return "True"
    return "False"
 