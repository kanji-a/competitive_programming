#include <iostream>
#include <vector>
using namespace std;

int main() {
  
  int rr;
  int cc;
  int n;
  cin >> rr;
  cin >> cc;
  cin >> n;

  vector<int> r(n);
  vector<int> c(n);
  vector<int> a(n);
  for(int i=0; i<n; i++){
    cin >> r[i] >> c[i] >> a[i];
  }

  cout << c[0] << endl;
  
  return 0;
}
