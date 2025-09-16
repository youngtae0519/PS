#include <bits/stdc++.h>

using namespace std;

int T, C;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> T;

  for(int i = 0; i < T; i++) {
    cin >> C;

    cout << C / 25 << " ";
    C = C % 25;;

    cout << C / 10 << " ";
    C = C % 10;;

    cout << C / 5 << " ";
    C = C % 5;

    cout << C << "\n";
  }

  return 0;
}