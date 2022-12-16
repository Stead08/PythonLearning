# クラスを作成
class Student:
    def __init__(self, name, old, birth, state):
        self.name = name
        self.old = old
        self.birth = birth
        self.state = state
    
    def change_name(self, name):
        self.name = name
        
n, k = map(int, input().split())

roster = [None] * n
#リストにインスタンスを逐一代入
for i in range(n):
    name, old, birth, state = input().split()
    roster[i] = Student(name, old, birth, state)

#名前の変更
for i in range(k):
    index, new_name = input().split()
    roster[int(index) - 1].change_name(new_name)
    
#出力
for student in roster:
    print(student.name, student.old, student.birth, student.state)
