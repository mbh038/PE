//
//  p204.cpp
//  
//
//  Created by Michael Hunt on 17/05/2017.
//
//

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

const long long M=1000000000;

const vector<int> primes ={
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
    43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97};

long long ghamming(int k,long long n){
    if (k==0) return log(n)/log(2) + 1;
    if (n==0) return 0;
    return ghamming(k-1,n) + ghamming(k,n/primes[k]);
}

int main(){
    cout<<ghamming(primes.size()-1,M)<<"\n";
    return 0;
    }

