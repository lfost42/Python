#include <iostream>
#include <vector>

//Write a program to find the sum of even numbers and the product of odd numbers in a vector.

int main () {
  std::vector<int> myVector = {2, 4, 3, 6, 1, 9};
  int sumTotal = 0;
  int prodTotal = 1;

  for (int i = 0; i < myVector.size(); i++) {
    if (myVector[i] % 2 == 0) {
      sumTotal += myVector[i];
    }
    if (myVector[i] % 2 != 0) {
      prodTotal *= myVector[i];
    }
  }
    std::cout << "Sum of even numbers is " << sumTotal << "\n";
    std::cout << "Product of odd numbers is " << prodTotal << "\n";
}


/* RESULT
Sum of even numbers is 12
Product of odd numbers is 27
END RESULT */