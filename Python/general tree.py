class treenode:
    #inisialisasi variabel
    def __init__(self, data):
        self.data = data
        self.child = []
        self.parent = None

    #fungsi untuk menambah child ke dalam tree
    def add_child(self, child):
        child.parent = self
        self.child.append(child)

    #fungsi untuk mennentukan hierarki data pada tree
    #semakin besar level semakin rendah hierarki nya
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    #fungsi untuk mencari node tertentu dengan memasukan key node nya
    def find_node(self, key):
        #recursive limit
        if self.data == key:
            return self
        #melakukan recursive fungsi sampai node yang dicari ketemu/sama value nya dengan key
        for child in self.child:
            found_node = child.find_node(key)
            #jika ketemu maka node akan di return
            if found_node:
                return found_node
        #jika tidak ketemu maka tidak akan me return apapun/null
        return None

    #fungsi untuk menghapus sebuah node dengan
    def remove_node(self,target):
        #list children dari parent target akan di update tanpa target dan akan membuat koneksi target dan parent nya terputus
        self.child = [child for child in self.child if child.data != target.data]

    #fungsi untuk melakukan print pada tree
    def print_tree(self):
        #spaces akan digunakan untuk membuat indentasi yang menunjukkan hierarki sebuah data
        #semakin besar level hierarki data, semakin banyak space yang diberikan sehingga akan berada semakin ke kanan
        #semakin ke kanan hierarki nya semakin rendah
        spaces = " " * self.get_level() * 3
        print(spaces + self.data)
        if len(self.child) > 0:
            for child in self.child:
                child.print_tree()

#fungsi untuk menambahkan anak/cabang ke dalam pohon
def make_child(val,parent,root):
    #key value2 akan digunakan sebagai key untuk mencari node yang ingin dijadikan sebagai parent dari node baru
    parent = root.find_node(parent)
    if parent:
        #jika node yang dicari ada, value yang dimasukkan akan menjadi salah satu anak dari node yang dicari/parent
        parent.add_child(treenode(val))
    else:
        print("Parent node not found")

#fungsi untuk menghapus sebuah node/data pada tree
def delete_node(val,parent,root):
    # key value2 akan digunakan sebagai key untuk mencari parent dari node yang ingin dihapus
    parent = root.find_node(parent)
    if parent:
        #jika node dicari ketemu maka value yang dimasukkan akan dapat dihapus dari tree
        parent.remove_node(treenode(val))
    else:
        print("Parent node not found")


def main():
    root = None
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

#inisialisai program
if __name__ == '__main__':
    main()
