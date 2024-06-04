import java.util.Scanner;

public class Main {

    public static treenode make_root(String value){
        treenode root = new treenode(value);
        return root;
    }
    public static void make_child(String value,String value2, treenode root){
        treenode parent = root.findnode(value2);
        if (parent != null){
            treenode child = new treenode(value);
            parent.addchild(child);
        } else {
            System.out.println("parent tidak ditemukan");
        }
    }
    public static void main(String[] args){
    treenode root = null;
     while (true){
         Scanner x = new Scanner(System.in);
         System.out.println("pilih program");
         System.out.println("1.make root");
         System.out.println("2.make child");
         System.out.println("3.print tree");
         System.out.println("4.exit");
         System.out.println("masukkan pilihan");
         int pilihan = x.nextInt();

         if (pilihan == 1) {
            Scanner y = new Scanner(System.in);
            System.out.println("masukan nilai root: ");
            String value = y.nextLine();

            root = make_root(value);
         }
         else if (pilihan == 2) {
             Scanner z = new Scanner(System.in);
             System.out.println("masukan nilai anak yang ingin dimasukkan: ");
             String value1 = z.nextLine();
             System.out.println("masukan parent: ");
             String value2 = z.nextLine();
            
             make_child(value1,value2,root);
         } else if (pilihan == 3) {
             root.print_tree();
         }
         else {
             break;
         }
     }
    }
}