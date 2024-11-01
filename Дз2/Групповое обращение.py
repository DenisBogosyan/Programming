g = int(input())
s = input()
a = ''
for i in range(0, len(s), g):
    a += s[g - i - 1]
print(a)