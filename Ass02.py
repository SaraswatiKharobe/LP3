from collections import Counter
string = 'BCAADDDCCACACACA'
class NodeTree:
    def __init__(self,left=None,right=None):
        self.left = left
        self.right = right
def huffman_code_tree(node,binString=''):
    if type(node) is str:
        return{node:binString}
    (l,r) = node.left,node.right
    d=dict()
    d.update(huffman_code_tree(l,binString+'0'))
    d.update(huffman_code_tree(r,binString+'1'))
    return d
p=Counter(string)
nodes = sorted(p.items(),key = lambda x:x[1],reverse=True)
while len(nodes) > 1:
    (key1,c1) = nodes[-1]
    (key2,c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1,key2)
    nodes.append((node, c1 + c2))
    nodes = sorted(nodes,key=lambda x:x[1],reverse = True)
    huffmanCode = huffman_code_tree(nodes[0][0])
print (sorted(huffmanCode.items(),key=lambda x:x[1]))
