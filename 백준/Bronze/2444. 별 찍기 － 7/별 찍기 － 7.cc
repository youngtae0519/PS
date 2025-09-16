#include <iostream>

using namespace std;

int N, total, blank, star;
int idx = 0;
bool check = false;

int main() {
  cin.tie(0)->ios::sync_with_stdio(0);

  cin >> N;
  total = 2 * N - 1;

  for (int i = 1; i <= total; i++) {
    if (i > N) {
      idx--;
    } else {
      idx++;
    }
    star = 2 * idx - 1;
    blank = (total - star) / 2;
    for (int j = 0; j < blank; j++) {
      cout << " ";
    }
    for (int j = 0; j < star; j++) {
      cout << "*";
    }
    cout << "\n";
  }

  return 0;
}