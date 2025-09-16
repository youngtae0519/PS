#include <iostream>

using namespace std;

string s;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  while(!getline(cin, s).eof()) {
    cout << s << '\n';
  }

  return 0;
}