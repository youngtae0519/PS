#include <iostream>
#include <vector>

using namespace std;

int num;
vector<int> v(31);

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  for(int i = 0; i < 28; i++) {
    cin >> num;
    v[num] = 1;
  }

  for(int i = 1; i < 31; i++) {
    if(v[i] == 0) {
      cout << i << "\n";
    }
  }

  return 0;
}