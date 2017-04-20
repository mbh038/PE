/*
Project Euler
Problem 225
Tribonacci non-divisors
*/

#include<iostream>
using namespace std;
#include<time.h>

int main(){

    clock_t t;
    t = clock();

    int limit=124;
    int countval=0;
    int n=25;
    int a,b,c,s,tmp;
    while (countval<limit){
        n += 2;
        a=b=c=1;
        while (1>0){
            tmp = a;
            a=b;
            b=c;
            c=tmp;
            s=a+b+c;
            c=s%n;
            if (c==0) break;
            if (a==1 && b==1 && c==1){
                countval += 1;
                break;
            }
        }
    }
    cout << countval <<","<< n << endl;
    cout << ((float)(clock()-t))/CLOCKS_PER_SEC<<endl;
    return 0;
}

