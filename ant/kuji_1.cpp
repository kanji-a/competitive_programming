#include <iostream>
using namespace std;

int main() {

  int n;
  int m;
  cin >> n >> m;
  int k[n];
  for(int i=0; i<n; i++){
    cin >> k[i];
  }

  int flg=0;

  for(int a=0; a<n; a++){
    for(int b=0; b<n; b++){
      for(int c=0; c<n; c++){
        for(int d=0; d<n; d++){
          if(k[a]+k[b]+k[c]+k[d] == m){
            flg = 1;
          }
        }
      }
    }
  }

  if(flg == 1){
    cout << "Yes" << endl;
  }else{
    cout << "No" << endl;
  }

  return 0;
}
