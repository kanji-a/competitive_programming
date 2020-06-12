#include <iostream>
#include <string>
using namespace std;
int main(void){
  int n;
  string s;
  int ans=0;
  int flg=0;

  cin >> n;
  cin >> s;

  string s_temp;

  int w_first=0;
  int w_last=0;
  int b_first=0;
  int b_last=0;

  while(true) {
    s_temp = s;
    flg = 0;
    w_first = s.find('w');
    w_last = s.rfind('w');
    b_first = s.find('b');
    b_last = s.rfind('b');
    if(w_last < b_first || b_last < w_first) {
      break;
    } else {
      for(int i=0; i<n; i++) {
        if(w_first <= i && i <= w_last && s[i] == 'b') {
          s_temp[i] = 'w';
        }
        if(b_first <= i && i <= b_last && s[i] == 'w') {
          s_temp[i] = 'b';
        }
      }
    }
    s = s_temp;
  }

  for(int i=0; i<n; i++) {
    if(s[i] == 'b') {
      ans++;
    }
  }

  cout << ans << endl;
  return 0;
}

