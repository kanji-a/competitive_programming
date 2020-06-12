#include <iostream>
#include <vector>
using namespace std;

int dfs(int n, vector<int> a, int k, int depth, int sum) {
  if(depth == n){
    return (sum == k);
  }else{
    if(dfs(n, a, k, depth+1, sum)) return 1;
    if(dfs(n, a, k, depth+1, sum+a[depth])) return 1;
  }
  return 0;
}

int main() {
  int n;
  vector<int> a(n);
  int k;

  cin >> n;
  for(int i=0; i<n; i++){
    cin >> a[i];
  }
  cin >> k;

  if(dfs(n, a, k, 0, 0)){
    cout << "Yes" << endl;
  }else{
    cout << "No" << endl;
  }

  return 0;
}
