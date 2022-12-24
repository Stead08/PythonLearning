# https://paiza.jp/works/mondai/stack_queue/stack_queue__practice_step5
from collections import deque
n, k = map(int, input().split())
A = list(map(int, input().split()))
time = A[-1]
# キューの長さは最大k
A = set(A)
q = deque()
for i in range(time + 1):
    if i in A:
        q.append(1)
    else:
        q.append(0)
    if len(q) > k:
        q.popleft()
    if i in A:
        print(q.count(1))
