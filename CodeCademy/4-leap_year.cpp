#include <iostream>

int main() {
  int year;

  std::cout << "Enter a year: \n";
  std::cin >> year;

  if (!(year >= 1000 && year <= 9999)) {
    std::cout << "Not a valid year.\n";
  }
  
  if (year % 4 == 0 && year % 400 == 0 && (year % 100 == 0 && year % 400 == 0)) {
      std::cout << "TRUE\n";
    } else {
      std::cout << "FALSE\n";
    }
}

/* RESULT
$ g++ leap_year.cpp
$ ./a.out
Enter a year: 
2000
TRUE
$ g++ leap_year.cpp
$ ./a.out
Enter a year: 
2100
FALSE
END RESULT */