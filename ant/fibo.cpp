#include <iostream>
using namespace std;

int fibo(int n){
  if(n == 0 || n == 1){
    return 1;
  }else{
    return fibo(n-1) + fibo(n-2);
  }
}

int main() {
  int x;
  cin >> x;
  for(int i=0; i<=x; i++){
    cout << i << " : ";
    cout << fibo(i) << endl;
  }
  return 0;
}
