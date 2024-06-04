class treenode:
    def __init__(self, data):
        self.data = data
        self.child = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.child.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def find_node(self, parent):
        if self.data == parent:
            return self
        for child in self.child:
            found_node = child.find_node(parent)
            if found_node:
                return found_node
        return None

    def remove_node(self,target):
        self.child = [child for child in self.child if child.data != target.data]

    def print_tree(self):
        spaces = " " * self.get_level() * 3
        print(spaces + self.data)
        if len(self.child) > 0:
            for child in self.child:
                child.print_tree()

def make_child(val,parent,root):
    parent = root.find_node(parent)
    if parent:
        parent.add_child(treenode(val))
    else:
        print("Parent node not found")

def delete_node(val,parent,root):
    parent = root.find_node(parent)
    if parent:
        parent.remove_node(treenode(val))
    else:
        print("Parent node not found")


def main():
    while True:
        print("pilih program")
        print("1.tanam pohon")
        print("2.buat anak")
        print("3.delete node")
        print("4.print tree")
        print("5.exit")
        x = int(input("masukkan pilihan: "))

        if x==1:
            val = input("masukan nilai yang ingin dimasukkan: ")
            root = treenode(val)

        elif x==2:
            val = input("masukkan nilai yang ingin dimasukkan: ")
            parent = input("masukkan cabang: ")
            make_child(val,parent,root)
        elif x==3:
            val = input("masukkan node yang ingin dihapus: ")
            parent = input("masukkan cabang: ")
            delete_node(val,parent,root)
        elif x==4:
            root.print_tree()
        elif x==5:
            break
        else:
            print("pilihan tidak tersedia")

if __name__ == '__main__':
    main()
