//
//  main.c
//  291
//
//  Created by Michael Hunt on 03/05/2017.
//  Coyright © 2017 Michael Hunt. All rights reserved.
//  4037525


#include <iostream>
using namespace std;
#include <ctime>
#include <cmath>
typedef long long ll;

//the primality tester  I used to use - not needed here in the end.
bool isPrime(ll n){
    //Returns True if n is rime.
    if (n==2 || n==3){
        return true;
    }
    if (!n%2 || !n%3){
        return false;
    }
    ll i = 5;
    ll w = 2;
    while (i * i<= n){
        if (n % i == 0){
            return false;
        }
        
        i += w;
        w = 6 - w;
    }
    return true;
}

ll nLimit(ll limit){
    return ll((-2+sqrt(4-8*(1-limit)))/(4)+1);
}

//p291 sets upper limit to prime values
//but these primes are centred square numbers that can be written as N^2 + (N+1)^2
//for prime limit = 5*10^n where n is odd, Nmax is 5* 10^((n-1)/2))

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define N 50000000  // correct for prime limit of 5 * 10^15
ll a[N+10];

int main(void){
    clock_t t;
    t = clock();
    int i,ans=0;
    REP(i,N) a[i] = 2ll*i*i + 2*i + 1;
    for(i=1;i<N;i++){
        if(a[i] == 2ll*i*i + 2*i + 1) ans++;
        if(a[i] > 1){
            ll p = a[i];
            for(ll j=i;j<N;j+=p) while(a[j] % p == 0) a[j] /= p;
            for(ll j=p-1-i;j<N;j+=p) while(a[j] % p == 0) a[j] /= p;
        }
    }
    
    cout << ans << endl;
    cout << ((float)(clock()-t))/CLOCKS_PER_SEC<<"\n";
    return 0;
}

/*
int main(int argc, const char * argv[]) {
    clock_t t;
    t = clock();
    
    ll limit = 5*pow(10,10);
    cout << p291(limit)<<endl;
    cout << ((float)(clock()-t))/CLOCKS_PER_SEC<<"\n";
    return 0;
}
*/
