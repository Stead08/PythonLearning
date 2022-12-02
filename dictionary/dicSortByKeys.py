#https://paiza.jp/works/mondai/forest_contest_001/forest_contest_001__c_player_number
#辞書の要素数n
n = int(input())
dic = {}
for _ in range(n):
    s, t = input().split()
    dic[int(s)] = t
#keyによる昇順のソート
sorted_dic = sorted(dic.items())
for i in range(n):
    print(*sorted_dic[i])
