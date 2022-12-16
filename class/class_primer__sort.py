# クラスを作成
class Student:
    def __init__(self, name, old, birth, state):
        self.name = name
        self.old = old
        self.birth = birth
        self.state = state
        
n = int(input())

roster = [None] * n
#リストにインスタンスを逐一代入
for i in range(n):
    name, old, birth, state = input().split()
    roster[i] = Student(name, old, birth, state)
# roaster[i].oldより右にあるroster[j]が小さければ場所を交換する
#sort
for i in range(n):
    for j in range(i+1, n):
        if roster[i].old > roster[j].old:
            roster[i], roster[j] = roster[j], roster[i]
    
#出力
for student in roster:
    print(student.name, student.old, student.birth, student.state)
