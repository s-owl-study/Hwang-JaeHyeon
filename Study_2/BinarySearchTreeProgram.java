public class BinarySearchTreeProgram {
    public static void main(String[] args) {
        BinaryTree bsT = new BinaryTree();

        bsT.insert(1); bsT.insert(2); bsT.insert(3);
        bsT.insert(6); bsT.insert(5); bsT.insert(4);
        bsT.insert(9); bsT.insert(88); bsT.insert(7);

        System.out.print("\nBinaryTree : ");
        bsT.Print();
    }
}

class BinaryTree {
    private Node root = null;
    private class Node {
        int key;
        Node left;
        Node right;
    }

    public void insert(int key) {
        root = insertKey(root, key);
    }
    

    public void Print() {
        DFS(root);
        System.out.println();
    }

    private void DFS(Node node) {
        if(node != null) {
            DFS(node.left);
            System.out.print(node.key + " ");
            DFS(node.right);
        }
    }

    private Node insertKey(Node node, int key) {
        if(node == null) {
            Node newNode = new Node();
            newNode.key = key;
            newNode.left = null;
            newNode.right = null;
            return newNode;
        }
        else if(key < node.key) {
            node.left = insertKey(node.left, key);
            return node;
        }
        else if(key > node.key) {
            node.right = insertKey(node.right, key);
            return node;
        }
        else {
            System.out.println("삽입 실패");
            return node;
        }
    }
   
}