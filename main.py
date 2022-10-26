def find_s_no_c(a, b):
    if a + b == 1:
        s = 1
    else:
        s = 0

    return s


def generated(a, b):
    return a * b


def find_s_with_c(s_no_c, gen, c=0):
    if gen == 1 or s_no_c + c == 1:
        c_out = 1
    else:
        c_out = 0

    if s_no_c != c:
        s = 1
    else:
        s = 0

    return s, c_out


A = '0110'
B = '1010'

P = ''
G = ''
for i in range(4):
    P += str(find_s_no_c(int(A[i]), int(B[i])))
    G += str(generated(int(A[i]), int(B[i])))

out = ''
x, carry = find_s_with_c(int(P[3]), int(G[3]))
out = str(x) + out
for i in range(2, -1, -1):
    x, carry = find_s_with_c(int(P[i]), int(G[i]), carry)
    out = str(x) + out
out = str(carry) + out

print(out)
