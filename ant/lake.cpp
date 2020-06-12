#include <iostream>
#include <vector>
using namespace std;

int dfs(vector<vector<char>>& field, int x, int y, int M, int N) {
  field[y][x] = '.';
  for(int i=-1; i<2; i++){
    for(int j=-1; j<2; j++){
      if(0<=x+i && x+i<N && 0<=y+j && y+j<M){
        if(field[y+j][x+i] == 'W'){
          dfs(field, x+i, y+j, M, N);
        }
      }
    }
  }
  return 0;
}

int main() {

  int N;
  int M;
  cin >> N;
  cin >> M;
  vector<vector<char>> field(M, vector<char>(N));
  for(int i=0; i<N; i++){
    for(int j=0; j<M; j++){
      cin >> field[j][i];
    }
  }
  int ans=0;

  for(int i=0; i<N; i++){
    for(int j=0; j<M; j++){
      if(field[j][i] == 'W'){
        ans++;
        dfs(field, i, j, M, N);
      }
    }
  }

  cout << ans << endl;

  /*
  for(int i=0; i<N; i++){
    for(int j=0; j<M; j++){
      cout << field[j][i];
    }
      cout << endl;
  }
  */

  return 0;
}
