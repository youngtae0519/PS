#include <iostream>
#include <vector>

using namespace std;

int N, M, i, j, k;

// vector 선언만 실행
vector<int> v;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> N >> M;

  // 실제 크기는 변수를 입력 받은 후 설정
  v.resize(N);

  for(int p = 0; p < M; p++) {
    cin >> i >> j >> k;

    for(int q = i; q <= j; q++) {
      v[q - 1] = k;
    }
  }

  for(auto it = v.begin(); it != v.end(); it++) {
    cout << *it << " ";
  }

  return 0;
}