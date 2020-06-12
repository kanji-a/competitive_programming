#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

int main() {

  int n;
  cin >> n;
  vector<int> s(n);
  vector<int> t(n);
  for(int i=0; i<n; i++){
    cin >> s[i];
  }
  for(int i=0; i<n; i++){
    cin >> t[i];
  }

  vector<pair<int, int>> job(n);
  for(int i=0; i<n; i++){
    job[i].first = t[i];
    job[i].second = s[i];
  }

  sort(job.begin(), job.end());

  int ans = 0;

  return 0;
}
