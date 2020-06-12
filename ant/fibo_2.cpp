#include <iostream>
#include <vector>
using namespace std;

vector<int> memo(100);

int fibo(int n){
  if(memo[n] == -1){
    if(n == 0 || n == 1){
      memo[n] = 1;
      return 1;
    }else{
      memo[n] = fibo(n-1) + fibo(n-2);
      return memo[n];
    }
  }else{
    return memo[n];
  }
}

int main() {
  int x;
  cin >> x;
  fill(memo.begin(), memo.end(), -1);
  for(int i=0; i<=x; i++){
    cout << i << " : ";
    cout << fibo(i) << endl;
  }
  return 0;
}
