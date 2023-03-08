#include <iostream>
#include <fstream>
#include <string>
using namespace std;

struct Pair {
    int numi;
    float numf;
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
            if (f == 0) this->data.numi = stoi(e);
            else {
                this->data.numf = stof(e);
                this->data.numi = 0;
            }
            this->data.code = f;
            this->next = nullptr;
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
    bool check; if (id == "i") check = 0; else check = 1;
    if (!head) {
        head = new Node(var,check);
        return;
    }
    Node *tmp = head;
    while (tmp) {
        if (!tmp->next) {
            tmp->next = new Node (var,check);
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
    int i = 1;
    while (tmp) {
        cout << i << " " << tmp->data.numi << ' ' << tmp->data.numf << ' ' << tmp->data.code << endl;
        tmp = tmp->next;
        i++;
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
        if (!cmd.empty()) {
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
            if (!filename.eof()) cout << "====================" <<endl;
        }
    }
}

int main(){
    string file_name = "test.txt";
    readfile (file_name);
    return 0;
    
}