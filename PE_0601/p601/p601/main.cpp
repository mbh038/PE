//
//  main.cpp
//  p601
//
//  Created by Michael Hunt on 02/05/2017.
//  Copyright © 2017 Michael Hunt. All rights reserved.
//



#include <stdio.h>

long long gcd(long long a, long long b)
{ return b ? gcd(b, a%b) : a; }

long long lcm(long long a, long long b)
{ return a * (b / gcd(a, b)); }

long long p(int s, long long n)
{
    long long l = 1;
    int i;
    for (i = 2; i <= s; i++)
        l = lcm(i, l);
    return (n - 2) / l - (n - 2) / lcm(l, s + 1);
}

int main()
{
    long long result = 0;
    for (int i = 1; i <= 31; i++) {
        result += p(i, 1LL << (2*i));
    }
    printf("%lld\n", result);
    return 0;
}

/*
 #include <iostream>
 using namespace std;
 #include <ctime>
 #include  <cmath>
 
 int p2(int s, long long limit){
 int Psum=0;
 long long k=s;
 while (k<limit){
 k+=s;
 int j=1;
 while (j<s){
 if ((k-j)%(s-j)){
 break;
 }
 j+=1;
 }
 if(j==s){
 if ((k+1)%(s+1)>0){
 Psum+=1;
 }
 }
 }
 return Psum;
 }
void p2v2(long long s, long long limit){
    int Psum=0;
    long long k=s;
    long long val1=0;
    long long dval=0;
    long long klast=0;
    long long count=0;
    while (k<limit){
        k+=s;
        long long j=1;
        while (j<s){
            if ((k-j)%(s-j)){
                break;
            }
            j+=1;
        }
        if(j==s){
            if ((k+1)%(s+1)>0){
                cout<<count<<","<<k-s+1<<","<<k-klast<<endl;
                dval=k-klast;
                klast=k;
                count+=1;
                if (count==1){
                    val1=k-s+1;
                }
            }
        }
        if (count>1.5*s){
            break;
            }
    }
    cout << s <<","<<val1<<","<<dval<<endl;
}

int main(int argc, const char * argv[]) {
    clock_t t;
    t = clock();
    long long s;
    long long limit;
    for (s=31;s<32;s++){
        t = clock();
        limit=pow(4,s);
        p2v2(s,limit);
    }
    
    cout << ((float)(clock()-t))/CLOCKS_PER_SEC<<"\n";
    return 0;
}


*/
