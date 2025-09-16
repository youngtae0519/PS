#include <iostream>

using namespace std;

string S;
int i;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> S >> i;

  cout << S[i - 1] << "\n";

  return 0;
}