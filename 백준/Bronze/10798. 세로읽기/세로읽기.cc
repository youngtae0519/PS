#include <iostream>
#include <vector>

using namespace std;

// 2차원 배열 선언
vector<vector<char>> arr;
string s;
// maxCol 0으로 초기화
// s.length()가 unsigned_int이기 때문에 maxCol을 -1로 설정하면 두 수를 비교할 때 항상 maxCol이 크다는 결과가 나옴
int maxCol = 0;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  for(int i = 0; i < 5; i++) {
    vector<char> tmp;
    arr.push_back(tmp);
    cin >> s;
    // 한줄씩 s를 입력받을 때마다 maxCol를 변경
    maxCol = (s.length() > maxCol) ? s.length() : maxCol;
    for(int j = 0; j < s.length(); j++) {
      arr[i].push_back(s[j]);
    }
  }

  // 하나의 col에 대해서 모든 row를 탐색
  for(int col = 0; col < maxCol; col++) {
    for(int row = 0; row < 5; row++) {
      // 현재 col이 arr[row]의 col보다 작으면 출력
      if(col < arr[row].size()) {
        cout << arr[row][col];
      }
    }
  }

  cout << "\n";

  return 0;
}