// TODO: 
// description: 
// name: Khang Duong
// date: 7/8/2022

#include <iostream>
#include <string>

// TODO: implement the class
class Date{ 
private:
  int year = 1970;
  int month = 1;
  int day = 1;
  bool check(int y, int m, int d) {
    if (y < 0 || m < 0 || m > 12 || d < 0 || d > 31) return false;
    if (m == 1 || m == 3 || m == 5 || m == 7 || m == 8 || m == 10 || m == 12) {
      return true;
    } else if (m == 4 || m == 6 || m == 9 || m == 11) {
      if (d > 30) return false;
      else return true;
    } else if (y % 4 == 0) {
      if (d > 29) return false;
      else return true;
    } else {
      if (d > 28) return false;
      else return true;
    }
  }
public:
  Date() {}
  Date(int yyyy, int mm, int dd) {
    if (check(yyyy, mm, dd)) {
      year = yyyy;
      month = mm;
      day = dd;
    }
  }
  void setYear(int value) {
    if (check(value, month, day)) year = value;
  }
  void setMonth(int value) {
    if (check(year, value, day)) month = value;
  }
  void setDay(int value) {
    if (check(year, month, value)) day = value;
  }

  int getYear() const {return year;}
  int getMonth() const {return month;}
  int getDay() const {return day;}
  void print() const {
    std::cout << year << "-" 
    << ((month / 10 > 0) ? "" : "0") << month << "-" 
    << ((day / 10 > 0) ? "" : "0") << day << std::endl;
  }
  friend std::ostream& operator<<(std::ostream& os, const Date & obj) {
    return os << obj.year << "-" 
      << ((obj.month / 10 > 0) ? "" : "0") << obj.month << "-" 
      << ((obj.day / 10 > 0) ? "" : "0") << obj.day;
  }
  bool operator==(const Date & obj) {
    return year == obj.year && month == obj.month && day == obj.day;
  }
  bool operator<(const Date & obj) {
    if (year < obj.year) return true;
    else if (year > obj.year) return false;
    else if (month < obj.month) return true;
    else if (month > obj.month) return false;
    else if (day < obj.day) return true;
    else if (day > obj.day) return false;
    else return true;
  }
  bool operator>(const Date & obj) {
    return !(operator<(obj));
  }
};

int main(){ 
  /*Date d1; 
  Date d2{2022, 2, 28}; 
  Date d3{2022, 2, 29}; 

  // step1: test following code snippet 
  // expected output: 
  // 1970-01-01 
  // 2022-02-28
  // 1970-01-01
  d1.print();     
  d2.print();
  d3.print(); 


  // step1: test following code snippet 
  // expected output
  // 2022-02-28
  // 2022-03-20
  d2.setDay(29); 
	d2.print();
  Date d4{2022, 3, 12};   // yay! spring break 
  d4.setDay(20);          // spring break is alway fast
  d4.print(); 
  */
    Date d1; 
  Date d2{2022, 3, 2}; 
  Date d3{2021, 3, 3}; 

  // step1: test following code snippet 
  // expected output: 
  // 1970-01-01 
  // 2022-03-02
  // 2021-03-03
  std::cout << d1 << std::endl;
  std::cout << d2 << std::endl;
  std::cout << d3 << std::endl;


  // step2: test following code snippet 
  // expected output
  // true
  // false
  // false
  std::cout << std::boolalpha << (d1 == Date{1970, 1, 1}) << std::endl; 
  std::cout << std::boolalpha << (d2 < d3) << std::endl; 
  std::cout << std::boolalpha << (Date{2000, 2, 29} > d3) << std::endl;  
}