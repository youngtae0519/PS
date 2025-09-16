#include <iostream>
#include <vector>

using namespace std;

int N;
double score;
double maxScore = 0;
double ans = 0;
vector<double> v;

int main() {
  cin.tie(0) -> ios::sync_with_stdio(0);

  cin >> N;

  for(int i = 0; i < N; i++) {
    cin >> score;
    maxScore = (score > maxScore) ? score : maxScore;
    v.push_back(score);
  }

  for(auto it = v.begin(); it != v.end(); it++) {
    ans += (*it / maxScore * 100) / N;
  }

  cout << ans << "\n";

  return 0;
}