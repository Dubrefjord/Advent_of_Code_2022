from anytree import Node, RenderTree, PreOrderIter
root = Node('',size = 0)
current_node = root
def main():
    global current_node
    with open('input7.txt') as file:
        file.readline()
        for line in file:
            line = line.strip().split()
            if line[0] == '$':
                parse_command(line)
            else:
                create_node(current_node,line)
        calc_size(root)

        free_space = 70000000-root.size
        smallest_sufficient_node = root
        for node in PreOrderIter(root):
            if not node.is_leaf:
                if free_space + node.size >= 30000000:
                    if node.size < smallest_sufficient_node.size:
                        smallest_sufficient_node = node
        print(smallest_sufficient_node.size)
    
def create_node(current, line):
    if line[0] == 'dir':
        return Node(line[1],current,size=0)
    return Node(line[1],current,size=int(line[0]))

def calc_size(node):
    if node.is_leaf:
        return node.size
    node.size = 0 
    for child in node.children:
        node.size += calc_size(child)
    return node.size
        
def parse_command(line):
    global current_node
    if line[1] == 'cd' and line[2] == '..':
        current_node = current_node.parent
        return
    if line[1] == 'cd':
        for node in current_node.children:
            if line[2] == node.name:
                current_node = node
                return
    return

if __name__ == "__main__":
   main()
