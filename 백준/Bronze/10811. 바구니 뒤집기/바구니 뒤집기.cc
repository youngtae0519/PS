#include <iostream>
#include <vector>

using namespace std;

int N, M, i, j;
vector<int> v;
vector<int> tmp;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> N >> M;

  for(int i = 0; i < N; i++) {
    v.push_back(i + 1);
  }

  for(int p = 0; p < M; p++) {
    cin >> i >> j;

    tmp.clear();

    for(int q = j - 1; q >= i - 1; q--) {
      tmp.push_back(v[q]);
    }

    for(int q = 0; q <= j - i; q++) {
      v[q + i - 1] = tmp[q];
    }
  }

  for(auto it = v.begin(); it != v.end(); it++) {
    cout << *it << " ";
  }

  return 0;
}