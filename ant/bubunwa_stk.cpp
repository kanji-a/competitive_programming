#include <iostream>
#include <vector>
#include <stack>
#include <map>
using namespace std;

int dfs(const int &n, const vector<int> &a, const int &k) {

  stack<pair<int, int>> stk;
  stk.push(make_pair(0, 0));
  int depth=0;
  int sum=0;
  int flg=0;
  int temp;

  while(stk.size()){
    cout << stk.top().second << endl;
    if(stk.top().second == k){
      flg = 1;
      //break;
    }
    depth = stk.top().first;
    temp = stk.top().second;
    stk.pop();
    if(depth < n){
      depth++;
      stk.push(make_pair(depth, temp+a[depth]));
      stk.push(make_pair(depth, temp));
    }
  }

  return flg;
}

int main() {

  int n;
  cin >> n;
  vector<int> a(n);
  int k;
  for(int i=0; i<n; i++){
    cin >> a[i];
  }
  cin >> k;

  if(dfs(n, a, k)){
    cout << "Yes" << endl;
  }else{
    cout << "No" << endl;
  }

  return 0;
}
