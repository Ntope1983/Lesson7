# Make a set  with number from 1-N and the tuple (N,N*N)
N = 5
A = set()

for i in range(1, N + 1):
    A.add(i)
print(A)
result = set()

for element in A:
    result.add((element, element ** 2))

print(result)
