#include <iostream>
#include <vector>

using namespace std;

int num;
int ans = 0;
vector<int> v(42);

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  for(int i = 0; i < 10; i++) {
    cin >> num;
    if(v[num % 42] == 0) {
      v[num % 42] = 1;
    }
  }

  for(auto it = v.begin(); it != v.end(); it++) {
    ans += *it;
  }

  cout << ans << "\n";

  return 0;
}