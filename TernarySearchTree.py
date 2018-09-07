class Node:
    def __init__(self, data):
        self.data = data
        self.end = False
        self.left = None
        self.mid = None
        self.right = None
    def print_(self):
        return ''.join(['[', self.data,
                        ('' if not self.end else ' <end>'),
                        ('' if self.left is None else ' left: ' + self.left.print_()),
                        ('' if self.mid is None else ' mid: ' + self.mid.print_()),
                        ('' if self.right is None else ' right: ' + self.right.print_()), ']'])
class TernarySTree:

    def __init__(self):
        None
    def add(self, node, string):
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
            # use 'or' for matches on string prefixes
            if len(tail) == 0 and node.end:
                return True
            return self.search(node.mid, tail)
        
    def show(self, node):
        return ''.join(['[', node.data,
                        ('' if not node.end else ' <end>'),
                        ('' if node.left is None else ' left: ' + node.left.print_()),
                        ('' if node.mid is None else ' mid: ' + node.mid.print_()),
                        ('' if node.right is None else ' right: ' + node.right.print_()), ']'])


class UsingTST:
    root = None
    def __init__(self, string):
        self.append(string)
    def append(self, string):
        self.root = TernarySTree().add(self.root, string)
    def show(self):
        return TernarySTree().show(self.root)
    def search(self, string):
        return TernarySTree().search(self.root, string)

		

		
tree = UsingTST('NARESUAN')
tree.append("ENGINEER")

print(tree.show())




