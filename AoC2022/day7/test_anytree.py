from anytree import Node, RenderTree, PostOrderIter

def create_node(current, line):
    if line[0] == 'dir':
        return Node(line[1],current,size=0)


with open('input7.txt') as file:
    file.readline()
    root = Node('',size = 0)
    create_node(root, ['dir','hej'])
    create_node(root, ['dir','hahha'])
    for node in root.children:
        create_node(node,['dir','hejhejhej'])
    print(RenderTree(root))



#root = Node('',size=0)
#a = Node('las.txt',root,size=1000)
#b = Node('mas.txt',root,size=2000)
#c = Node('dir',root,size=0)
#d = Node('asr.txt',c,size=10000)
#e = Node('asre.txt',c,size=2003)
#size = 0
#for node in root.descendants:
#    size += node.size
#print(size)
#print(RenderTree(root))


