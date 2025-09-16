#include <iostream>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int T, A, B, total;

  cin >> T;
  total = T;

  while(T--){
    cin >> A >> B;

    cout << "Case #" << total - T << ": " << A + B << "\n";
  }

  return 0;
}