#include <bits/stdc++.h>

using namespace std;

int N, age;
string name;
vector<tuple<int, string, int>> v;

bool compare(tuple<int, string, int> a, tuple<int, string, int> b) {
    if(get<0>(a) == get<0>(b)) {
        return get<2>(a) < get<2>(b);
    } else {
        return get<0>(a) < get<0>(b);
    }
};

int main() {
    cin.tie(0) -> ios::sync_with_stdio(0);
    
    cin >> N;
    
    for(int i = 0; i < N; i++) {
        cin >> age >> name;
        v.push_back({age, name, i});
    }
    
    sort(v.begin(), v.end(), compare);
    
    for(auto it = v.begin(); it != v.end(); it++) {
        cout << get<0>(*it) << " " << get<1>(*it) << "\n";
    }
    
    return 0;
}