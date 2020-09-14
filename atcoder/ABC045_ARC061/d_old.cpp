#include <iostream>
using namespace std;

int main() {

  int h, w, n;
  cin >> h >> w >> n;

  int a[n], b[n];
  for(int i=0; i<n; i++) {
    cin >> a[i] >> b[i];
  }

  long long int ans[10];
  for(int i=0; i<10; i++) {
    ans[i] = 0;
  }

  int board[h][w];
  for(int i=0; i<h; i++) {
    for(int j=0; j<w; j++) {
      board[i][j] = 0;
    }
  }
  for(int i=0; i<n; i++) {
    board[a[i]-1][b[i]-1] = 1;
  }
  /*
  for(int i=0; i<h; i++) {
    for(int j=0; j<w; j++) {
      cout << board[i][j];
    }
    cout << endl;
  }
  */

  int cnt;

  for(int i=0; i<=h-3; i++) {
    for(int j=0; j<=w-3; j++) {
      cnt = 0;
      for(int k=0; k<3; k++) {
        for(int l=0; l<3; l++) {
          if(board[i+k][j+l] == 1) {
            cnt++;
          }
        }
      }
      ans[cnt]++;
    }
  }

  for(int i=0; i<10; i++) {
    cout << ans[i] << endl;
  }

  return 0;
}
