# 最短経路問題をダイクストラ法を用いて解く
# https://qiita.com/shizuma/items/e08a76ab26073b21c207
import math
# 初期のノード間の距離のリスト
route_list = [[0, 50, 80, 0, 0], [0, 0, 20, 15, 0 ], [0, 0, 0, 10, 15], [0, 0, 0, 0, 30], [0, 0, 0, 0, 0]]
#ノードの数
node_num = len(route_list)
#未探索ノード
unsearched_nodes = list(range(node_num))
#ノードごとの距離のリスト
distance = [math.inf] * node_num
# 最短経路でそのノードのひとつ前に到達するノードのリスト
previous_nodes = [-1] * node_num
#初期のノードの距離は０とする
distance[0] = 0

def get_target_min_index(min_index, distance, unsearched_nodes):
    start = 0
    while True:
        index = distance.index(min_index, start)
        found = index in unsearched_nodes
        if found:
            return index
        else:
            start = index + 1
#未探索ノードがなくなるまで繰り返す
while(len(unsearched_nodes) != 0):
    #まず未探索ノードのうちdistanceが最小の物を選択する
    possible_min_distance = math.inf #最小のdistanceを見つけるための一時的なdisntance
    for node_index in unsearched_nodes: #未探索のノードのループ
        if possible_min_distance > distance[node_index]:
            # より小さい値が見つかれば更新
            possible_min_distance = distance[node_index]
    target_min_index = get_target_min_index(possible_min_distance, distance, unsearched_nodes)
    #ここで探索するので未探索リストから除去
    unsearched_nodes.remove(target_min_index)

    target_edge = route_list[target_min_index] #ターゲットになるノードから伸びるエッジのリスト
    for index, route_dis in enumerate(target_edge):
        if route_dis != 0:
            if distance[index] > (distance[ target_min_index] + route_dis):
                #過去に設定されたdistanceよりも小さい場合はdistanceを更新
                distance[index] = (distance[ target_min_index]+ route_dis)
                previous_nodes[index] = target_min_index #ひとつ前に到達するノードのリストも更新

previous_node = node_num - 1
ans_route = []
while previous_node != -1:
    ans_route.append(previous_node + 1)
    previous_node = previous_nodes[previous_node]

for i in reversed(ans_route):
    print(i)
#距離
print(distance[node_num - 1])
