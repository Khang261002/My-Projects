#include <iostream>
#include <fstream>
#include <string>
using namespace std;

struct Pair {
    float num;
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
        Node(string e, bool f) {
            data.num = stof(e);
            data.code = f;
            next = nullptr;
        }
    };
protected:
    Node *head;
public:
    Stack(): head(nullptr) {};
    ~Stack() {}
    void insert(string id, string var);
    void get_value();
};

void Stack::insert(string id, string var) {
    bool check;
    if (id == "i") check = 0;
    else check = 1;
    if (!head) {
        head = new Node(var, check);
        return;
    }
    Node *tmp = head;
    while (tmp) {
        if (!tmp->next) {
            tmp->next = new Node(var, check);
            return;
        }
        tmp = tmp->next;
    }
}

void Stack::get_value() {
    if (!head) {
        cout << "invalid";
        return;
    }
    Node *tmp = head;
    int i = 1;
    while (tmp) {
        cout << tmp->data.num << ' ' << tmp->data.code << endl;
        tmp = tmp->next;
        i++;
    }
    return;
}

void readfile(string file_name) {
    fstream filename;
    Stack new_head;
    filename.open(file_name);
    string cmd = "";
    while (!filename.eof()) {
        getline(filename, cmd);
        
        if (!cmd.empty()) {
            string id = "";
            string var = "";
            bool check = false;
            for (int i = 0; i < int(cmd.size());i++){
                if (cmd[i] == ' ')
                    check = true;
                else if (!check) id +=cmd[i];
                else var += cmd[i];
            }
            new_head.insert(id, var);
            new_head.get_value();
            if (!filename.eof()) cout << "====================" << endl;
        }
    }
}

int main() {
    string file_name = "test.txt";
    readfile (file_name);

    return 0;
}
