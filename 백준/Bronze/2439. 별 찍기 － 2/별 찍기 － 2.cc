#include <iostream>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int N;

  cin >> N;

  for(int i = 0; i < N; i++) {
    for(int j = N; j > 0 ; j--) {
      if(j - 1 <= i) {
        cout << "*";
      }
      else {
        cout << " ";
      }
    }
    cout << "\n";
  }

  return 0;
}