#include <iostream>

using namespace std;

int num, row, col;
int maxNum = -1;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  for(int i = 0; i < 9; i++) {
    for(int j = 0; j < 9; j++) {
      cin >> num;
      if(num > maxNum) {
        maxNum = num;
        row = i;
        col = j;
      }
    }
  }

  cout << maxNum << "\n" << row + 1 << " " << col + 1 << "\n";

  return 0;
}