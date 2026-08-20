import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean=re.sub(r'[^a-zA-Z0-9]', '', s)
        print( clean.lower(), clean[::-1].lower())
        return clean.lower() == clean[::-1].lower()