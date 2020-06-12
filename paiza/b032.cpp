#include <iostream>
#include <string>
using namespace std;
int main(void){
  int w;
  cin >> w;
  char a[8][w];
  char b[8][w];
  string a_str(w, '0');
  string b_str(w, '0');
  string c_str(w, '0');

  for(int i=0; i<8; i++) {
    cin >> a[i];
  }
  for(int i=0; i<8; i++) {
    cin >> b[i];
  }

  for(int i=0; i<w; i++) {
    if(a[0][i] == '|') {
      a_str[i] += 5;
    }
    if(b[0][i] == '|') {
      b_str[i] += 5;
    }
    for(int j=0; j<5; j++) {
      if(a[j+3][i] == '|') {
        a_str[i] += j;
      }
      if(b[j+3][i] == '|') {
        b_str[i] += j;
      }
    }
  }

  for(int i=0; i<w; i++) {
    c_str[w-i-1] += (a_str[w-i-1]-'0') + (b_str[w-i-1]-'0');
    if(c_str[w-i-1]-'0' > 9) {
      c_str[w-i-1] -= 10;
      if(i < w-1){
        c_str[w-i-2] ++;
      }
    }
  }

  char c[8][w];
  for(int i=0; i<w; i++) {
    for(int j=0; j<8; j++) {
      if(j == 2) {
        c[j][i] = '=';
      } else {
        c[j][i] = '*';
      }
    }
  }

  for(int i=0; i<w; i++) {
    if(c_str[i] >= '5') {
      c_str[i] -= 5;
      c[0][i] = '|';
    } else {
      c[1][i] = '|';
    }
    c[(c_str[i]-'0')+3][i] = '|';
  }

  for(int i=0; i<8; i++) {
    for(int j=0; j<w; j++) {
      cout << c[i][j];
    }
    cout << endl;
  }

  return 0;
}

