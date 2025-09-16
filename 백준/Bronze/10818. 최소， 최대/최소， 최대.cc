#include <iostream>

using namespace std;

int N, num;
int maxNum = -1000000001;
int minNum = 1000000001;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> N;

  for(int i = 0; i < N; i++) {
    cin >> num;
    
    if(num > maxNum) {
      maxNum = num;
    }
    if(num < minNum) {
      minNum = num;
    }
  }

  cout << minNum << " " << maxNum << "\n";

  return 0;
}