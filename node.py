#Sharv Utpat
#CS 4375.HON
#Vincent Ng
#9/10/23
class Node:
    def __init__(self, data):
        self.data = data
        self.left_label=None
        self.left = None
        self.middle = None
        self.middle_label=None
        self.right = None
        self.right_label=None

def is_leaf(node):
    if (node.left == None and node.middle == None and node.right == None):
        return True
    return False

def dfs(node, level=0,edge_label=None):
    if node is None:
        return
    if is_leaf(node) :
        return
    for i in range(level):
        print("| ", end = "")
    flag = True
    if node.left is not None and is_leaf(node.left):
        print(f"{node.data} = {node.left_label} : {node.left.data}")
        flag = False
    else:
        if node.left is not None:
            print(f"{node.data} = {node.left_label} :")
            dfs(node.left,level+1,node.left_label)
    if node.middle is not None and is_leaf(node.middle):
        for i in range(level):
            print("| ", end="")
        print(f"{node.data} = {node.middle_label} : {node.middle.data}")
        flag = False
    else:
        if node.middle is not None:
            for i in range(level):
                print("| ", end="")
            print(f"{node.data} = {node.middle_label} :")
            dfs(node.middle,level+1,node.middle_label)

    if node.right is not None and is_leaf(node.right):
        for i in range(level):
            print("| ", end="")
        print(f"{node.data} = {node.right_label} : {node.right.data}")
        flag = False
    else:
        if node.right is not None:
            for i in range(level):
                print("| ", end="")
            print(f"{node.data} = {node.right_label} :")
            dfs(node.right,level+1,node.right_label)
    #if (flag):
        #print(f"{node.data} = {edge_label} :")
    #dfs(node.left,level+1,node.left_label)
    #dfs(node.middle,level+1,node.middle_label)
    #dfs(node.right,level+1,node.right_label)

def main():
    print ("calling node.py")
    root = Node(".")
    root.left = Node("wesley = 0")
    root.middle = Node("wesley = 1")
    root.right = Node("wesley = 2")

    dfs(root)

if __name__ == '__main__':
    main()