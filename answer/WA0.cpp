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

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  ll A, B;
  cin >> A >> B;
  cout << A * B << "\n";
}
