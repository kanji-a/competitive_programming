#include <iostream>
using namespace std;

int main() {
  
  string a;
  string b;
  string c;
  char turn = 'a';
  char ans;

  int a_pnt = 0;
  int b_pnt = 0;
  int c_pnt = 0;

  cin >> a >> b >> c;

  while(true) {

    // 勝利条件
    /*
    if(turn == 'A' && a_pnt == a.size()) {
      break;
    } else if(turn == 'B' && b_pnt == b.size()) {
      break;
    } else if(turn == 'C' && c_pnt == c.size()) {
      break;
    }
    */

    //cout << turn << endl;

    if(turn == 'a') {
      if(a_pnt == a.size()) {
         break;
      }
      turn = a[a_pnt];
      a_pnt++;
    }else if(turn == 'b') {
      if(b_pnt == b.size()) {
         break;
      }
      turn = b[b_pnt];
      b_pnt++;
    }else if(turn == 'c') {
      if(c_pnt == c.size()) {
         break;
      }
      turn = c[c_pnt];
      c_pnt++;
    }
  }

  ans = turn - 32;

  cout << ans << endl;

  return 0;
}
