import sys

# 전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
# 중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
# 후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트

N = int(sys.stdin.readline().strip())
tree = {}

for n in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]

print(tree)


def preorder(root):
    if root != '.':
        print(root, end='')  # root
        preorder(tree[root][0])  # left -> 맨 처음 0 번째 항목이 들어간 재귀함수가 끝나기 전까지 계속 0번째 인덱스를 탐색
        preorder(tree[root][1])  # right


def inorder(root): # -> A -> B -> D  순으로 들어감 D가 root인 상태로 ㅎ마수에 들어가면 D의 tree[D][0]  의값은 '.'임으로 return none을 하고, 그때 다시 inorder tree[D][1] 로 넘어가지만 값이 '.'임으로 none을 리턴한다 그리고 계쏙 나옴
    if root != '.': # 그렇게 tree[D][0], tree[D][1]이 스택프레임에서 빠져 나오게되면 tree[B][0]은 종료가되고 tree[B][1]의 값이 비로소 들어가는데, 이때 값이 '.' 임으로 none를 리턴 그다음에 tree[A][1]값은 아직 있음으로 이값이 다시 스택에 쌓임
        inorder(tree[root][0])  # left
        print(root, end='')  # root # Tree[B][1] 값이 none을 리턴하고 한단계 위인 이 부분이 실행이되는데, 이때 A가 출력이됨
        inorder(tree[root][1])  # right

# 즉 이거는 tree[x][0] 이 none을 출력하고 tree[x][1] 로 넘어갈때 중간에 출:q!력인된다
def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right # 위와 A 가 출력되기 전가지는 같지만, 이 경우 DB까진 출력이 되고 A는 스택프레임에서 빠져나오지 않고, tree[A][1]의 값이 스택에 들어간다 (C)
        print(root, end='')  # root
# 즉 이거는 tree[x][1] 이 none을 출# 즉 이거는 tree[x][0] 이 none을 출력하고 tree[x][1] 로 넘어갈때 중간에 출력인된다 력할때

preorder('A')
print()
inorder('A')
print()
postorder('A')
