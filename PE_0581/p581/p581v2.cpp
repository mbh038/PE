//
//  p581.cpp
//  
//
//  Created by Michael Hunt on 17/05/2017.
//
//

#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

const long long M=1000000000000;
vector <long long> ns;

//const vector<int> primes ={2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,43, 47};
const vector<int> primes ={2, 3, 5, 7, 11};

long long ghamming(int k,long long n){
    if (k==0) return log(n)/log(2) + 1;
    if (n==0) return 0;
    return ghamming(k-1,n) + ghamming(k,n/primes[k]);
}

void nsgen(vector <long long> &ns){
    ns.push_back(0);
    vector <long long> is(primes.size());
    vector <long long> xs(primes.size());
    for (int n=1;n<primes.size();++n){
        double min = *min_element(xs.begin(), xs.end());

        ns.push_back(min);
        for (int i=0;i<xs.size();i++){
            for(int x=0;x<xs.size();x++){
                for(int p=0;p<primes.size();p++){
                    if (xs[i]==ns[n]){
                        xs.push_back(primes[p]*ns[i]);
                    }
                }
            }
        }
    }
}

int main(){
    vector <long long>ns;
    nsgen(ns);
    for(int p : primes) {
        cout<<p<<endl;
    }
    return 0;
}
