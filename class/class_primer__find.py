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
    roster[i] = Student(name, old, birth, state
#old == k　であるインスタンスからnameを抽出
k = input()
for student in roster:
    if student.old == k:
        print(student.name)
        break
