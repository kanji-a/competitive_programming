#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

int main() {

  long long h, w;
  int n;
  cin >> h >> w >> n;

  int a[n], b[n];
  for(int i=0; i<n; i++) {
    cin >> a[i] >> b[i];
  }

  unsigned long long ans[10];
  for(int i=0; i<10; i++) {
    ans[i] = 0;
  }

  vector<pair<int, int>> window;

  for(int i=0; i<n; i++) {
    for(int j=0; j<3; j++) {
      for(int k=0; k<3; k++) {
        if(0 <= (a[i]-1)+j-2 && (a[i]-1)+j <= h-1
            && 0 <= (b[i]-1)+k-2 && (b[i]-1)+k <= w-1) {
          window.push_back(make_pair((a[i]-1)+j-2, (b[i]-1)+k-2));
        }
      }
    }
  }

  sort(window.begin(), window.end());

  map<pair<int, int>, int> c;
  for(auto t: window) {
    ++c[t];
  }
  for(auto t: c) {
    ans[t.second]++;
  }

  ans[0] = (h-2) * (w-2);
  for(int i=1; i<10; i++) {
    ans[0] -= ans[i];
  }

  for(int i=0; i<10; i++) {
    cout << ans[i] << endl;
  }

  return 0;
}
