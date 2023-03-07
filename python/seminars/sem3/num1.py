s = ['1', '2', '3', '4']

s = list(map(int, s))

count = len(set(s))

s[::-1]

indices = [i for i in range(len(s)) if s[i] == x]

sum = sum(s[::2])

max_string = max(s, key=len)
