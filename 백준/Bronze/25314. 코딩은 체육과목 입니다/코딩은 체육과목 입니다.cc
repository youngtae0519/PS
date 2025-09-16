#include <iostream>

using namespace std;

int main() {
  int N;
  int cnt = 0;
  string ans;

  cin >> N;

  while(N != 0) {
    cnt++;
    N -= 4;
  }

  while(cnt--) {
    ans += "long ";
  }

  cout << ans << "int" << endl;

  return 0;
}