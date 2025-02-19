str1 = "ABCABC"
str2 = "ABC"

if (str1 + str2 != str2 + str1):
     print("")
gcd_length = self.gcd(len(str1), len(str2))
print(str1[:gcd_length])


def gcd(self, a: int, b: int) -> int:
    return a if b == 0 else self.gcd(b, a % b)
