mat = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

op = input()
cc = 0
s = 0

for l in range(12):
    for c in range(12):
        mat[l][c] = float(input())

# para fins de teste
# for l in range(11, 6, -1):
# 	for c in range(12 - l, l):
# 		mat[l][c] = 1

if op == "S":
    for l in range(11, 6, -1):
        for c in range(12 - l, l):
            s += mat[l][c]
    print("%.1f" % s)

elif op == "M":
    for l in range(11, 6, -1):
        for c in range(12 - l, l):
            s += mat[l][c]
            cc += 1
    m = s / cc
    print("%.1f" % m)

