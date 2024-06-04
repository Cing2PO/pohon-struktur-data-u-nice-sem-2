import java.util.ArrayList;
import java.util.List;

public class treenode {
    private String data = null;
    private List<treenode> children = new ArrayList<>();
    private treenode parent = null;

    public treenode(String data){
        this.data = data;
    }

    public void addchild(treenode child){
        child.parent = this;
        this.children.add(child);
    }

    public Integer getlevel(){
        Integer level = 0;
        treenode p = this.parent;
        while (p != null){
            level++;
            p = p.parent;
        }
        return level;
    }

    public treenode findnode(String parent){
        if(this.data.equals(parent)) {
            return this;
        }
        for (treenode children : this.children) {
            treenode foundNode = children.findnode(parent);
            if (foundNode != null) {
                return foundNode;
            }
        }
        return null;
    }

    public void print_tree(){
        int size = this.children.size();
        String spaces = " ";
        String repeated_space = spaces.repeat(this.getlevel());
        System.out.println(repeated_space + this.data);
        if (size>0){
            for (treenode children : this.children){
                children.print_tree();
            }
        }
    }
}
