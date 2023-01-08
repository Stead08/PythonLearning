#url: https://www.techiedelight.com/ja/calculate-height-binary-tree-iterative-recursive/
# 二分木の高さを計算する
class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

# 指定されたバイナリーツリーの高さを計算する再起的関数
count = 0
def height(root):
#ベースケース：高さ0
    if root is None:
        return 0
    # 左右の子で再帰して、最深のレベルを調べる
    return 1 + max(height(root.left), height(root.right))

# 実行例
if __name__ == '__main__':
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(16)
    root.right.right = Node(25)
    print('The height of the binary tree is', height(root))
