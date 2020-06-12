#include <iostream>
#include <vector>
using namespace std;

int main() {
  
  int n;
  cin >> n;

  vector<int> a(n);
  for(int i=0; i<n; i++){
    cin >> a[i];
  }

  int ans=0;

  for(int i=0; i<n; i++){
    if(a[a[i]-1]-1 == i){
      ans++;
    }
  }

  cout << ans/2 << endl;
  
  return 0;
}
