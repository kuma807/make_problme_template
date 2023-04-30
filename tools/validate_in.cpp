#include <bits/stdc++.h>
// #include <atcoder/modint>
#define rng(a) a.begin(),a.end()
#define rrng(a) a.rbegin(),a.rend()
#define INF 2000000000000000000
#define ll long long
#define ull unsigned long long
#define ld long double
#define pll pair<ll, ll>
using namespace std;
template<class T>bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T>bool chmin(T &a, const T &b) { if (b<a) { a=b; return 1; } return 0; }
const double PI = 3.141592653589793238462643383279;

bool AC = true;
void check(bool condition) {
  AC = (AC && condition);
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  ll A, B;
  cin >> A >> B;
  check(1 <= A && A <= 100000);
  check(1 <= B && B <= 100000);
  //入力終了確認
  string line;
  while (getline(cin, line)) {
    check(line == "");
  }
  check(cin.eof());
  if (AC) {
    cout << "AC" << "\n";
  }
  else {
    cout << "WA" << "\n";
  }
}
