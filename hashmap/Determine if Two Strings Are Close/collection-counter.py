from collections import Counter
word1 = "cabbba"
word2 = "abbccc"

if len(word1) != len(word2):
    print(False)
if set(word1) != set(word2):
    print(False)
s1, s2 = Counter(word1), Counter(word2)

if sorted(s1.values()) == sorted(s2.values()):
    print(True)
print(False)