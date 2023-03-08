#include <iostream>
#include <fstream>
#include <string>

struct Pair {
    float num;
    bool code;
};

class Stack{
public:
    class Node {
        class Pair data;
        Node *next;
        friend class Stack;
    public:
        Node(): next(nullptr) {};
        Node(std::string var, bool code) {
            data.num = std::stof(var);
            data.code = code;
            next = nullptr;
        }
    };
protected:
    Node *head;
public:
    Stack(): head(nullptr) {};
    ~Stack() {}
    void insert(std::string id, std::string var);
    void get_value();
};

void Stack::insert(std::string id, std::string var) {
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
        std::cout << "invalid";
        return;
    }
    Node *tmp = head;
    int i = 1;
    while (tmp) {
        std::cout << tmp->data.num << ' ' << tmp->data.code << std::endl;
        tmp = tmp->next;
        i++;
    }
    return;
}

void readfile(std::string file_name) {
    std::fstream filename;
    Stack new_head;
    filename.open(file_name);
    std::string cmd = "";
    while (!filename.eof()) {
        std::getline(filename, cmd);
        if (!cmd.empty()) {
            std::string id = "";
            std::string var = "";
            bool check = false;
            for (int i = 0; i < int(cmd.size()); i++) {
                if (cmd[i] == ' ')
                    check = true;
                else if (!check) id += cmd[i];
                else var += cmd[i];
            }
            new_head.insert(id, var);
            new_head.get_value();
            if (!filename.eof()) std::cout << "====================" << std::endl;
        }
    }
}

int main() {
    std::string file_name = "test.txt";
    readfile(file_name);

    return 0;
}
