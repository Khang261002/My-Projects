#include "StackFrame.h"
#include <iostream>
#include <fstream>
#include "errors.h"
#include "constants.h"
using namespace std;

StackFrame::StackFrame() : opStackMaxSize(OPERAND_STACK_MAX_SIZE), localVarArrSize(LOCAL_VARIABLE_ARRAY_SIZE) {}

/*Pair DKdata(string cmdline) {
    string tmp1 = "";
    string tmp2 = "";
    bool check = false;
    for (int i; i < int(cmdline.size());i++){
        if (cmdline[i] == ' ')
            check = true;
        else if (!check)
            tmp1 +=cmdline[i];
        else
            tmp2+= cmdline[i];
    }
    Pair p;
    p.id = tmp1;
    return;
}*/

void StackFrame::AI_dunglailaptrinh (string cmd, int line) {
    string id = "";
    string num = "";
    bool check = false;
    for (int i; i < int(cmd.size());i++){
        if (cmd[i] == ' ')
            check = true;
        else if (!check) id +=cmd[i];
        else num+= cmd[i];
    }
    if (id == "iadd") {

    } else if (id == "fadd") {

    } else if (id == "isub") {

    } else if (id == "fsub") {

    } else if (id == "imul") {

    } else if (id == "fmul") {

    } else if (id == "idiv") {

    } else if (id == "fdiv") {

    } else if (id == "irem") {

    } else if (id == "ineg") {

    } else if (id == "fneg") {

    } else if (id == "iand") {

    } else if (id == "ior") {

    } else if (id == "ieq") {

    } else if (id == "feq") {

    } else if (id == "ineq") {

    } else if (id == "fneq") {

    } else if (id == "ilt") {

    } else if (id == "flt") {

    } else if (id == "igt") {

    } else if (id == "fgt") {

    } else if (id == "ibnot") {

    } else if (id == "iconst") {

    } else if (id == "fconst") {

    } else if (id == "iload") {

    } else if (id == "fload") {

    } else if (id == "istore") {

    } else if (id == "fstore") {

    } else if (id == "i2f") {

    } else if (id == "f2i") {

    } else if (id == "top") {

    } else if (id == "val") {

    } else if (id == "par") {

    } else throw TypeMisMatch(line);
}

void StackFrame::run(string filename) {
    ifstream readcmd;
    readcmd.open(filename);
    string cmd;
    int line = 0;
    while (!readcmd.eof()) { line++;
        getline(readcmd,cmd);
        if(cmd.empty()) throw TypeMisMatch(line);
        AI_dunglailaptrinh (cmd, line);
        
    }
}