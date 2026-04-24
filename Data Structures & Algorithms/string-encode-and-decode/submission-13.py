class Solution:
    def encode(self, strs: List[str]) -> str:
        # For each string, store it as "length#string" and join them all
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            # Find the next delimiter to get the length of the string
            j = s.find("#", i)
            length = int(s[i:j])
            # Extract the string based on the length and move the pointer
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res
