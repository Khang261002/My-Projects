#ifndef __STACK_FRAME_H__
#define __STACK_FRAME_H__

#include <string>
#include <stack>

/*
StackFrame declaration
*/
class StackFrame {
    int opStackMaxSize; // max size of operand stack
    int localVarArrSize; // size of local variable array
    Stack DKStack;
public:
    /*
    Constructor of StackFrame
    */
    StackFrame();
    
    /*
    Run the method written in the testcase
    @param filename name of the file
    */
    void run(std::string filename);
    void AI_dunglailaptrinh(string cmd, int line);
};

class Stack {
    Stack *head;
    Stack *tail;
public:
    Stack () {}
public:
    class Node {
        Node *next;
        Pair data;
    };
};

class Pair {
    double num;
    int index;
};

template <class T, class K>
class AVL {
    class Node {
        T data; K key;
        Node *pLeft; Node *pRight;
        Node(T data, K key): data(data), key(key), pLeft(nullptr), pRight(nullptr){}
    };
};

#endif // !__STACK_FRAME_H__