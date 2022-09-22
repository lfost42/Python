#include <iostream>

int main() {
  int earthW;
  int planet;
  std::cout << "What is your earth weight?\n";
  std::cin >> earthW;

  std::cout << "What planet number do you want to fight on?\n";
  std::cin >> planet;

  std::cout << "Destination planet weight: ";
    switch(planet) {
    
    case 1 :
      std::cout << earthW*0.38 << "\n";
      break;
    case 2 :
      std::cout << earthW*0.91 << "\n";
      break;
    case 3 :
      std::cout << earthW*0.38 << "\n";
      break;
    case 4 :
      std::cout << earthW*2.34 << "\n";
      break;
    case 5 :
      std::cout << earthW*1.06 << "\n";
      break;
    case 6 :
      std::cout << earthW*0.92 << "\n";
      break;
    default:
      std::cout << earthW*1.19 << "\n";
      break;
  }  
  
}

/* RESULT
$ g++ space.cpp
$ ./a.out
What is your earth weight?
120
What planet number do you want to fight on?
4
Destination planet weight: 280.8
END RESULT */