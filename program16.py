def is_palindrome(string):
    # Remove non-alphanumeric characters and convert to lowercase
    string = ''.join(e for e in string if e.isalnum()).lower()
    
    left, right = 0, len(string) - 1
    while right >= left:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

# Test cases
print(is_palindrome('malayalam'))  # Output: True
print(is_palindrome('A man, a plan, a canal, Panama'))  # Output: True
print(is_palindrome('Hello'))  # Output: False
