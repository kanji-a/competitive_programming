#include <iostream>
using namespace std;

int main() {
  
  string s;
  string f;
  string b;

  cin >> s;

  f = s.substr(0, 4);
  b = s.substr(4);

  cout << f << " " << b << endl;
  
  return 0;
}
