#include <iostream>

using namespace std;

int N, X, num;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> N >> X;

  for(int i = 0; i < N; i++) {
    cin >> num;
    if(num < X) {
      cout << num << " ";
    }
  }

  return 0;
}