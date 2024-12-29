from collections import Counter

ransomNote = "aa"
magazine = "ab"

count_rN = Counter(ransomNote)
count_ma = Counter(magazine)
flag = False
if count_rN.items() in count_ma.items():
    flag = True
str = count_rN.values()
print(str)

