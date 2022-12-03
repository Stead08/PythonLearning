#区間内の個数 (文字列)
#https://paiza.jp/works/mondai/prefix_sum_problems/prefix_sum_problems__string_count_boss
n, x, y = map(int, input().split())
str1 = input()
l_str = list(str1)
A = []
for i in l_str:
    if i == 'b':
        A.append(1)
    else:
        A.append(0)
S = [0]
for i in A:
    s = i + S[-1]
    S.append(s)
print(S[y] - S[x-1])
