//
//  p512
//
//  See https://math.stackexchange.com/questions/316376/how-to-calculate-these-totient-summation-sums-efficiently

#include <iostream>
using namespace std;
#include<map>
#include<time.h>

typedef long long LL;
map<LL,LL> X2;

LL F2(LL N){
    return N*(N-1)/2;
}

LL R2(LL N){
    if(N==1) return 0;
    if(X2[N]) return X2[N];
    LL sum = F2(N);
    LL m=2;
    while(true){
        LL x = N/m;
        LL nxt = N/x;
        if(nxt >= N) return X2[N] = sum - (N-m+1)*R2(N/m);
        sum -= (nxt-m+1) * R2(N/m);
        m = nxt+1;
    }
}

//returns sum of totients of x<=n
//wrapper for R2
//sum of totient(x) for x<=n
LL totientSum(LL n){
    return R2(n)+1;
}

//sum of totient(x) for x<=n and x is even
LL evenTotientSum(LL N){
    if (N < 2) return 0;
    return totientSum(N/2)+evenTotientSum(N/2);
}

//sum of totient(x) for x<=n and x is odd (answer to PE p512)
LL oddTotientSum(LL N){
    return totientSum(N)-evenTotientSum(N);
}

int main(){
    clock_t t;
    t = clock();
    cout << oddTotientSum(500000000)<<"\n";
    cout << ((float)(clock()-t))/CLOCKS_PER_SEC<<"\n";
    return 0;
}
