#逆ポーランド記法
from collections import deque
n = int(input())
a = input().split()
ans = 0
q = deque()
for i in a:
    if i == "+" or i == "-":
        num_1 = q.pop()
        num_2 = q.pop()
        if i == "+":
            q.append(num_1 + num_2)
        else:
            q.append(num_2 - num_1)
    else:
        q.append(int(i))
print(*q)

# a = 1 2 + 3 4 + -
# dequeの中身
# deque([1])
# deque([1, 2])
# deque([3])
# deque([3, 3])
# deque([3, 3, 4])
# deque([3, 7])
# deque([-4]) 
