//
//  main.cpp
//  p407
//
//  Created by Michael Hunt on 18/04/2017.
//  Copyright © 2017 Michael Hunt. All rights reserved.
//

typedef long long LL;

#include <iostream>
using namespace std;
#include<vector>
#include <time.h>

LL inverse(const  LL a, const LL n)
//returns multiplicative inverse of a mod n. a and n must be co-prime
{
    LL t1=0,t2=1,r1=n,r2=a;
    while (r2!=0){
         LL q = (r1 /r2);
         LL tmp=t1;
        t1=t2;
        t2=tmp - q * t2;
        tmp=r1;
        r1=r2;
        r2=tmp - q * r2;
    }
    if (t1 < 0){
        t1 +=n;
    }
    return t1;
}

void pflist( LL n,vector<LL> &dpfs)
//calculates the distinct prime factors of n as [2^a,3^b.....]
{
    LL i=2;
    while (i*i<=n){
        if (n%i !=0){
            i+=1;
            //cout << i << "\n";
        }
        else {
            dpfs.push_back(1);
            while (n%i==0){
                n/=i;
                dpfs.back()*=i;
            }
        }
    }
    if(n>1){
        dpfs.push_back(n);
    }
}

void combinations (vector <LL> vin,const LL r,vector<vector <LL>> &vout)
//calling function must set up a matrix std::vector<std::vector<>> vout;
//on completion of this routine, vout will contain the n!/(n-r)r! combinations
//of r elements drawn from vin, of length n.
{
    LL n;
    n=(LL)vin.size();
    vector<bool> v(n);
    fill(v.begin(), v.begin() + r, true);
    
    do {
        vector<LL> thisComb;
        for (LL i = 0; i < n; ++i) {
            if (v[i]) {
                thisComb.push_back(vin[i]);
            }
        }
        vout.push_back(thisComb);
    } while (prev_permutation(v.begin(), v.end()));
}

LL max_idempotent(const LL n)
//returns the maximum idempotent of n
{
    LL aprod=1;
    vector<LL> pfs;
    pflist(n,pfs);
    if (pfs.size()==1){
        return 1; //idempotent=1 for primes or powers of primes
    }
    //Use the CRT to find m 'base' idempotent solutions from m prime factors p_i^a_i
    vector<LL> idems;
    for (LL i=0;i<pfs.size();i++){
        vector<LL> allButOnePfs;
        for (LL j=0;j<i;j++){
            allButOnePfs.push_back(pfs[j]);
        }
        for (LL j=i+1;j<pfs.size();j++){
            allButOnePfs.push_back(pfs[j]);
        }
        LL xsum=0;
        for (LL k=0;k<allButOnePfs.size();k++){
            LL Ni=(int)n/allButOnePfs[k];
            xsum+=inverse(Ni,allButOnePfs[k])*Ni;
        }
        idems.push_back(xsum % n);
    }

    //generate all other idempotents from these, and return the maximum
    LL maxval= *max_element(idems.begin(), idems.end());
    for (LL i=2;i<idems.size();i++){
        vector<std::vector<LL>> vout;
        combinations(idems,i,vout);
        for (int ii=0;ii<vout.size();ii++){
            aprod=1;
            for (LL j=0;j<vout[ii].size();j++){
                aprod*=vout[ii][j];
                aprod=aprod%n;
            }
            if (aprod>maxval){
                maxval=aprod;
            }
        }
    }
    return maxval;
}

int main()
{
    clock_t t;
    t = clock();

    LL limit=10000000;
    LL misum=0;
    for (LL n=2;n<=limit;n++){
        LL nsum = max_idempotent(n);
        misum+=nsum;
    }
    cout  << misum << "\n";
    cout << "Elapsed time: "  << ((float)(clock()-t))/CLOCKS_PER_SEC << "s" << endl;
}

LL crt(const vector<LL> a, const vector<LL> n){
  //Chinese remainder theorem
  //a=[a_0....a_i], n=[n_0...n_i] in x = a_i mod n_i
  LL nprod=1;
  for (LL i=0;i<n.size();i++){
  nprod*=n[i];
  }
  LL xsum=0;
  for (LL i=0;i<n.size();i++){
  LL  Ni=nprod/n[i];
  xsum+=a[i]*inverse(Ni,n[i])*Ni;
  }
  return xsum%nprod;
}



