#include <iostream>

int main() {
  
  double tempf;
  double tempc;
  
  std::cout << "Enter a temp in F to convert to C! /n";
 std::cin >> tempf;

  tempc = (tempf - 32) / 1.8;
  
  std::cout << "The temp is " << tempc << " degrees Celsius.\n";
  
}

/* RESULT:

$ g++ temperature.cpp
$ ./a.out
Enter a temp in F to convert to C! 
100
The temp is 37.7778 degrees Celsius.
*/