#include <iostream>
using namespace std;

int main() {
  
  string s;
  int k;
  cin >> s;
  cin >> k;

  for(int i=0; i<s.size(); i++){
    if(k == 0){
      break;
    }else if(i == s.size()-1){
      s[i] = 'a' + (((s[i] - 'a') + k) + 26) % 26;
      k = 0;
      break;
    }else if(s[i] != 'a' && 26 - (s[i] - 'a') <= k){
      k -= (26 - (s[i] - 'a'));
      s[i] = 'a';
    }
  }

  cout << s << endl;

  return 0;
}
