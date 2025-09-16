#include <iostream>
#include <vector>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int N, v, num;
  // vector 선언 방법
  // 1. vector<자료형> 변수명
  // 2. vector<자료형> 변수명(개수) -> {0, 0, 0, ...}
  // 3. vector<자료형> 변수명(개수, 초기값) -> {초기값, 초기값, 초기값, ...}
  // 3. vector<자료형> 변수명 = {변수 1, 변수 2, ...}
  vector<int> arr;
  int ans = 0;

  cin >> N;

  for(int i = 0; i < N; i++) {
    cin >> num;
    // push_back : vector 맨 뒤에 변수 삽입
    arr.push_back(num);
  }

  cin >> v;

  // vector 순회 방법
  // 1. for(int i = 0; i < vector.size(); i++) -> vector[i]로 접근
  // 2. for(auto it = vector.begin(); it != vector.end(); it++) -> *it로 접근
  // 3. for(auto it = vector.rbegin(); it != vector.rend(); it++) -> 역으로 순회 가능
  for(auto it = arr.begin(); it != arr.end(); it++) {
    if(*it == v) {
      ans++;
    }
  }

  cout << ans << "\n";

  return 0;
}