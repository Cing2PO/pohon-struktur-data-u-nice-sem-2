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

    def print_tree(self):
        spaces = " " * self.get_level() * 3
        print(spaces + self.data)
        if len(self.child) > 0:
            for child in self.child:
                child.print_tree()

def plant_tree():
    root = treenode("car")

    tuner = treenode("tuner")
    tuner.add_child(treenode("Nissan"))
    tuner.add_child(treenode("Toyota"))
    tuner.add_child(treenode("Honda"))

    muscle = treenode("muscle")
    muscle.add_child(treenode("Ford"))
    muscle.add_child(treenode("Chevrolet"))
    muscle.add_child(treenode("Dodge"))

    exotic = treenode("exotic")
    exotic.add_child(treenode("Ferrari"))
    exotic.add_child(treenode("Lamborghini"))

    root.add_child(tuner)
    root.add_child(muscle)
    root.add_child(exotic)

    return root

if __name__ == '__main__':
    root = plant_tree()
    #print(root.get_level())
    root.print_tree()