// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution {
	public:
		string FirstNonRepeating(string A){
		    // Code here
		    int flag[26]={0};

            deque<char> dq;

            string ans;

            for(int i=0; i<A.size(); i++)

            {

            dq.push_back(A[i]);

            flag[A[i]-'a']++;

            while(!dq.empty() && flag[dq.front()-'a']!=1)

            {

             dq.pop_front();

             }

             if(dq.empty())

             ans+="#";

            else

             ans+=dq.front();

            }

            return ans;

            }
};


// { Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		string A;
		cin >> A;
		Solution obj;
		string ans = obj.FirstNonRepeating(A);
		cout << ans << "\n";
	}
	return 0;
}  // } Driver Code Ends