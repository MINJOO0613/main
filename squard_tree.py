#스쿼드03 우재튜터님 숙제 (이진트리)
# 7
# A B C    #(세로읽기)A부터 세로는 parents // B부터 세로는 left 위치 // C부터 세로는 right 위치
# B D .
# C E F
# E . .
# F . G
# D . .
# G . .

n = int(input())
tree = {}

#딕셔너리로 이진트리 만들기
for _ in range(n):
    parents, left, right = map(str,input().split())   # 2번째줄 주석대로 각각 parents, left, right에 값을 할당한다.
    tree[parents] = [left, right]  #{'A': ['B', 'C'], 'B': ['D', '.'], 'C': ['E', 'F'], 'E': ['.', '.'], 'F': ['.', 'G'], 'D': ['.', '.'], 'G': ['.', '.']}
#tree[parents][0] = parents의 left
#tree[parents][1] = parents의 right

############################무시하세요 연습장 같은 거예요#################################################
# 아래처럼 계속 하다가
# def preorder(parents):
#     if parents != ".":
#         print(parents)
#         node1 = tree[parents][0]
#
#     if node1 in tree:
#         if tree[node1][0] != ".":
#             print(node1)
#             node2 = tree[node1][0]
#
#     if node2 in tree:
#         if tree[node2][0] != ".":
#             print(node2)
#             node3 = tree[node2][0]
#         else:
#             print(f'>>>끄읕{node2}')
# 이거 어디서 많이 본 것이, 재귀 같다는 생각을 하게 되는데.....
########################################################################################################

def preorder(parents):      #전위 순회 (루트->왼쪽 자식->오른쪽 자식)
    if parents != ".":
        print(parents, end="")      #부모 출력! (처음에 루트부터 출발하여 부모값 출력!)
        preorder(tree[parents][0])  #왼쪽 자식 출력!
        preorder(tree[parents][1])  #왼쪽 자식이 모두 출력되면, "dict['A'][1]"이 재귀함수로 반복하며 오른쪽 자식을 출력함

# 솔직히 "preorder(tree[parents][0])" 이 줄에서 parents의 right값을 어케 실행해야 되누 하다가
# 구글님의 도움을 받아 다음 코드 완성함(우재튜터님 눈 감아...)
# 하 값 제대로 나올 때, 이때 겁나 짜릿함...(참고, 이때 새벽 1시 43분이었음)
########################################################################################################
# inorder말고 postorder 먼저 만들자. 이게 더 쉬울 것 같애...후...

def postorder(parents):     #후위 순회 (왼쪽 자식->오른쪽 자식->루트)
    if parents != ".":
        postorder(tree[parents][0]) #왼쪽 자식부터 dfs방법으로 계층 끝까지 탐색함
        postorder(tree[parents][1]) #왼쪽 자식의 탐색이 끝나면 오른쪽 자식의 탐색을 시작하여 계층 끝까지 탐색함
        print(parents, end="")      #끝까지 탐색이 끝난 순으로 출력함(왼쪽 -> 오른쪽 -> 루트) (스택처럼 마지막 값이 먼저 나옴)

########################################################################################################
# inorder 함수 만드는데 30분 걸렸다고 하면 믿으시겠어요? (현 시각 새벽 3시 지나고 있음)

def inorder(parents):       #중위 순회 (왼쪽 자식->루트->오른쪽 자식)
    if parents != ".":
        inorder(tree[parents][0]) #왼쪽 자식부터 dfs방법으로 계층 끝까지 탐색함
        print(parents, end="")    #왼쪽 자식의 탐색이 끝나면 마지막 왼쪽 자식부터 출력 후 부모 출력
        inorder(tree[parents][1]) #부모 위치 출력까지 끝나면, 오른쪽 자식 탐색 시작, 왼쪽 자식이 있을 경우 다시 위 내용처럼 반복


root = 'A'
preorder(root)       #ABDCEFG
print()              #한줄씩 띄우는 방법은 이것 밖에 없으실까요? 나 진짜 별짓 다 해봤어
inorder(root)        #DBAECFG
print()
postorder(root)      #DBEGFCA