#include <iostream>

using namespace std;

int num, idx;
int maxNum = 0;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  for(int i = 0; i < 9; i++) {
    cin >> num;
    
    if(num > maxNum) {
      maxNum = num;
      idx = i + 1;
    }
  }

  cout << maxNum << "\n" << idx << "\n";

  return 0;
}