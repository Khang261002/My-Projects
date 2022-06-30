#include <iostream>
using namespace std;

template <typename T>
class BSTree{
public:
    class Node; // forward declaration
private:
    Node* root = nullptr;
public:
    BSTree() : root(nullptr) {}
    ~BSTree(){}
    // helper function here
    int count;
    void insertFIFO(T data) {
        //TODO
    };

    void sumLeft(){
        //TODO
    };

    void inorder( Node* root)
    {
        if (root != NULL) {
            inorder(root->pLeft);
            cout << root->data << " ";
            inorder(root->pRight);
        }
    }
    void printIn()
    {
        inorder(root);
    }
public:
    class Node
    {
    private:
        T data;
        Node *pLeft;
        Node *pRight;
        friend class BSTree<T>;
    public:
        Node(): pLeft(0), pRight(0) {};
        Node(T data): data(data), pLeft(0), pRight(0) {};
    };
};

int main() {
    BSTree<int> tree;
    BSTree<int>::Node node();
    int arr[12] = {30,19,31,6,18,20,28,16,11,13,14,7};
    for(int i = 0; i < 12; i++){
        tree.insertFIFO(arr[i]);
    }
    tree.printIn();
    cout << endl << tree.sumLeft();
    return 0;
}