#include <iostream>
#include <vector>
#include <map>
#include <queue>
using namespace std;

int bfs(const vector<vector<char>> &maze, const int &N, const int &M) {

  int sx, sy;  //start
  int gx, gy;  //goal
  int px, py;  //present
  //(x, y)
  queue<pair<int, int>> que;
  //4houkou no idou
  const int dx[4] = {1, 0, -1, 0};
  const int dy[4] = {0, 1, 0, -1};
  const int INF = 100000000;
  vector<vector<int>> dist(M, vector<int>(N));

  //find Start and Goal
  for(int i=0; i<M; i++){
    for(int j=0; j<N; j++){
      dist[i][j] = INF;
      if(maze[i][j] == 'S'){
        sx = j;
        sy = i;
      }
      if(maze[i][j] == 'G'){
        gx = j;
        gy = i;
      }
    }
  }
  dist[sy][sx] = 0;

  que.push(make_pair(sx, sy));

  while(que.size()){
    px = que.front().first;
    py = que.front().second;
    for(int i=0; i<4; i++){
      if(0 <= px+dx[i] && px+dx[i] < N && 0 <= py+dy[i] && py+dy[i] < M){
      cout << maze[py+dy[i]][px+dx[i]] << endl;
        if(maze[py+dy[i]][px+dx[i]] != '#'
          && dist[py+dy[i]][px+dx[i]] == INF){
          que.push(make_pair(px+dx[i], py+dy[i]));
          dist[py+dy[i]][px+dx[i]] = dist[py][px] + 1;
        }
      }
    }
    que.pop();
  }

  for(int i=0; i<M; i++){
    for(int j=0; j<N; j++){
      if(dist[i][j] == INF) cout << '#';
      else cout << dist[i][j];
    }
    cout << endl;
  }

  return dist[gy][gx];
}

int main() {

  int N;
  int M;
  cin >> N;
  cin >> M;
  vector<vector<char>> maze(M, vector<char>(N));
  for(int i=0; i<N; i++){
    for(int j=0; j<M; j++){
      cin >> maze[i][j];
    }
  }

  cout << bfs(maze, N, M) << endl;

  return 0;
}
