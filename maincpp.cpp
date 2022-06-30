#include <iostream>
#include <string>

int main(){
    std::string num = "12.34";
    float x = std::stof(num);
    std::cout << x << std::endl;

    return 0;
}
