class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.mid = None
        self.right = None

class TernarySTree:

    def __init__(self):
		self.root = Node()
        self.leaf = None

    def add(self, node, string):
        if len(string) == 0:
            return node

        head = string[0]
        tail = string[1:]

        if node is None:
            node = Node(head)
        if head < node.data:
            node.left = self.add(node.left, string)
        elif head > node.data:
            node.right = self.add(node.right, string)
        else:
            if len(tail) == 0:
                node.end = 1
            else:
                node.mid = self.add(node.mid, tail)
        return node
    
    def delete(self, node, string):
        None
    
    def search(self, node, string):
        
        if node is None or len(string) == 0:
            return False

        head = string[0]
        tail = string[1:]
        if head < node.data:
            return self.search(node.left, string)
        elif head > node.data:
            return self.search(node.right, string)
        else:
            # use 'and' for matches on complete words only,
            # versus 'or' for matches on string prefixes
            if len(tail) == 0 or node.end:
                return True
            return self.search(node.mid, tail)
        
    def show():
        None
        
tie = TernarySTree()
node = Node("")
tie.add(node, 'data')
tie.add(node, 'OKK')
tie.add(node, '52')
a = tie.search(node, 'OKK')
b = tie.search(node, 'data')
c = tie.search(node, '52')
print(a)
tie.delete(node, 'data')
print(a)
#print(b)
#print(c)

