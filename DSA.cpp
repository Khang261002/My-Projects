#include <iostream>
#include <fstream>
#include <string>
using namespace std;

struct Pair {
    size_t num;
    int code;
};

class Stack{
public:
    class Node {
        class Pair data;
        Node *next;
        friend class Stack;
    public:
        Node(): next(nullptr) {};
        Node(int e, bool f) {
            data.num = e;
            data.code = f;
            next = nullptr;
        }
    };
protected:
    Node *head;
public:
    Stack(): head(nullptr){};
    ~Stack(){}
    void insert(string id, string var);
    void get_value();
};

void Stack::insert(string id, string var){
    double numD = stod(var);

    if (!head) {
        head = new Node(numD,true);
        return;
    }
    Node *tmp = head;
    while (tmp) {
        if (!tmp->next) {
            tmp->next = new Node (numD,true);
            return;
        }
        tmp = tmp->next;
    }
}

void Stack::get_value(){
    if (!head) {
        cout << "invalid";
        return;
    }
    Node *tmp = head;
    while (tmp) {
        cout << tmp->data.num << ' ' << tmp->data.code << endl;
        tmp = tmp->next;
    }
    return;
}
void readfile (string file_name) {
    fstream filename;
    Stack newhead;
    filename.open(file_name);
    string cmd = "";
    while (!filename.eof()) {
        getline (filename,cmd);
        string id = "";
        string var = "";
        bool check = false;
        for (int i = 0; i < int(cmd.size());i++){
            if (cmd[i] == ' ')
                check = true;
            else if (!check) id +=cmd[i];
            else var+= cmd[i];
        }
        //cout << id << endl << var << endl;
        newhead.insert(id, var);
        newhead.get_value();
        cout << "====================" <<endl;
    }
}

int main(){
    string file_name = "test.txt";
    readfile (file_name);
    Pair p;
    p.num = 9;
    p.code = 1;
    return 0;
}