#starting numbers
a = 0
b = 1

n = 14

seq = []

for i in range(n):
    if len(seq) == 0:
        seq.append(a)
        seq.append(b)
        print(seq)
    else:
        F = seq[i] + seq[i-1]
        seq.append(F)
        print(i)
    print(seq)

a1, b1 = 0, 1
n1 = 14
for i in range(n):
    print(a)
    a, b = b, a+b