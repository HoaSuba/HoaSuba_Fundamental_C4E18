# tính tổng các số từ 1 đến n
n= 10

# Cách 1
total = 0

for i in range(n+1):
    total += i
print(total)

# Cách 2: pythonic
total = sum(range(n+1)) # range: tạo nên 1 dãy số
print(total)

