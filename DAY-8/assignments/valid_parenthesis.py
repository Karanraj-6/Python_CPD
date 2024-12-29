from collections import Counter
string = input()
counter = Counter(string)
if counter['('] == counter[')'] and counter['{'] == counter['}'] and counter['['] == counter[']']:
    print('Valid')
else:
    print('Invalid')