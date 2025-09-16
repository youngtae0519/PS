#include <iostream>

using namespace std;

int main() {
  int A, B, C;
  int H, M;

  cin >> A >> B >> C;

  if(B + C >= 60) {
    M = (B + C) % 60;
    H = A + ((B + C) / 60);
    if(H >= 24) {
      H -= 24;
    }
  }
  else {
    H = A;
    M = B + C;
  }

  cout << H << " " << M << endl;

  return 0;
}