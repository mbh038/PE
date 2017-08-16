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
using namespace std;

const long long M=123199;

const vector<int> primes ={2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,43, 47};

long long ghamming(int k,long long n){
    if (k==0) return log(n)/log(2) + 1;
    if (n==0) return 0;
    return ghamming(k-1,n) + ghamming(k,n/primes[k]);
}

void primeFactors(int n,vector<int> &pf){
    // Find prime factors of n
    // Calling function would need declaration similar to
    //      vector<int> pf;
    //      primeFactors(n,pf);
    //      Program must declare #include <vector>
    int i=2;
    while (i*i<n+1){
        if (n%i){
            i+=1;
        }
        else{
            n /=i;
            pf.push_back(i);
        }
    }
    if (n>1){
        pf.push_back(n);
    }
}

//bool is47Smooth(long long n){
//    long long T=n*(n+1)/2;
//    long long i=2;
//    if (T<47) return true;
//    while (i*i<T+1){
//        if (T%i){
//            i+=1;
//        }
//        else{
//            if (i>47) return false;
//            T /=i;
//        }
//    }
//    if (T>1){
//        return T>47;
//    }
//    return true;
//}

bool is47smooth(long long n){
    const vector<long long> ps ={
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
        43, 47};
    long long i,j,ppow,p;
    double a=0;
    for (i=0;i<6;i++){
        j=1;
        p=ps[i];
        while(pow(p,j)<=n){
            if (n%(long long)pow(p,j)==0){
                a+=log(p);
            }
            j+=1;
        }
    }
//    bool result=a>log(n-1)==true;
//    cout<<n<<","<<a<<","<<result<<endl;
    return a>log(n-1);
}



int main(){
    
    const vector<long long> ps ={
        53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,173,179,181,191,193,197};
    
    long long n,T,nsum=0;
    bool flag;
    for (n=2;n<=M;n++){
//        flag=false;
//        T=n*(n+1)/2;
//        for(int i=0;i<ps.size();i++){
//            if (T%ps[i]==0)
//                flag=true;
//                break;
//        }
////        if (flag==true) continue;
        if (n%53==0 || n%59==0 || n%61==0 || n%67==0 || n%71==0 || n%73==0 || n%79==0 || n%83==0
            || n%89==0 || n%97==0 || n%101==0 || n%103==0 || n%107==0 || n%109==0 || n%113==0 || n%127==0
            || n%131==0 or n%137==0 || n%139==0 || n%149==0 || n%151==0 || n%157==0 || n%163==0
            ||n%173==0 ||n%179==0 ||n%181==0 ||n%191==0 ||n%193==0 ||n%197==0) continue;
        if ((n+1)%53==0 || (n+1)%59==0 || (n+1)%61==0 || (n+1)%67==0 || (n+1)%71==0 || (n+1)%73==0 || (n+1)%79==0 || (n+1)%83==0
            || (n+1)%89==0 || (n+1)%97==0 || (n+1)%101==0 || (n+1)%103==0 || (n+1)%107==0 || (n+1)%109==0 || (n+1)%113==0 || (n+1)%127==0
            || (n+1)%131==0 or (n+1)%137==0 || (n+1)%139==0 || (n+1)%149==0 || (n+1)%151==0 || (n+1)%157==0 || (n+1)%163==0
            ||(n+1)%173==0 ||(n+1)%179==0 ||(n+1)%181==0 ||(n+1)%191==0 ||(n+1)%193==0 ||(n+1)%197==0) continue;
        if (!is47smooth(n)) continue;
        if (!is47smooth(n+1)) {
            n++;
            continue;
        }
        
        nsum+=n;

//        if (is47smooth(T)){
//            nsum+=n;
//        }
    }
    cout<<nsum<<endl;
    return 0;
}
