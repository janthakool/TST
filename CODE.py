class Node:
    def __init__(self, data):
        self.data = data
        self.end = False
        self.left = None
        self.mid = None
        self.right = None
    def __repr__(self):
        # useful in debugging
        return ''.join(['[', self.data,
                        ('' if not self.end else ' <end>'),
                        ('' if self.left is None else ' left: ' + self.left.__repr__()),
                        ('' if self.mid is None else ' mid: ' + self.mid.__repr__()),
                        ('' if self.right is None else ' right: ' + self.right.__repr__()), ']'])    
class TernarySTree:

    def __init__(self):
        #self.root = Node()
	    None
    def add(self, node, string):
        #node = self.root
        if len(string) == 0:
            return node

        head = string[0]
        tail = string[1:]

        if node is None:
            node = Node(head)
        if head < node.data:
            node.left = self.add(node.left,string)
        elif head > node.data:
            node.right = self.add(node.right,string)
        else:
            if len(tail) == 0:
                node.end = True
            else:
                node.mid = self.add(node.mid, tail)
        return node
    
    def delete(self, node, string):
        None
    
    def search(self, node, string):
        #node = self.root
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
        
    def show(self, node):
        #node = self.root
        return ''.join(['[', node.data,
                        ('' if not node.end else ' <end>'),
                        ('' if node.left is None else ' left: ' + node.left.__repr__()),
                        ('' if node.mid is None else ' mid: ' + node.mid.__repr__()),
                        ('' if node.right is None else ' right: ' + node.right.__repr__()), ']'])
        
tie = TernarySTree()
node = Node("None")
tie.add(node, 'data')

a = tie.search(node, 'OKK')
b = tie.search(node, 'data')
c = tie.search(node, '52')
print(a)
tie.delete(node, 'data')
print(tie.show(node))

#print(c)

