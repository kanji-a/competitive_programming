#include <iostream>
#include <cmath>
using namespace std;

int main() {
  
  string s_str;
  long long int ans = 0;

  cin >> s_str;

  ans += stoll(s_str);
  for(int i=1; i<s_str.size(); i++) {
    for(int j=0; j<=i; j++) {
      if(j==0 || j==i){
        ans += stoll(s_str.substr(j, s_str.size()-i)) * pow(2, i-1);
      } else {
        ans += stoll(s_str.substr(j, s_str.size()-i)) * pow(2, i-2);
      }
    }
  }

  cout << ans << endl;

  return 0;
}
