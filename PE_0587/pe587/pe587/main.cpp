//
//  main.cpp
//  pe587
//
//  Created by Michael Hunt on 17/04/2017.
//  Copyright © 2017 Michael Hunt. All rights reserved.
//

#include <iostream>
using namespace std;
#include <cmath>
#include <time.h>


float sideRatio(int n){
    //analytically find orange area/blue area
    float x0,y0,theta,AC,AL;
    x0=n*((n+1)-sqrt((2*n)))/(n*n+1);//lowest x value where diagonal line and leftmost circle cross
    y0=x0/n;//lowest y value where diagonal line and leftmost circle cross
    theta=atan((1-x0)/(1-y0));
    AC=(y0-theta+sin(theta))/2;
    AL=1-M_PI_4;
    return AC/AL;
}

int main() {
    clock_t t;
    t = clock();
    float target,r;
    int n,nmin,nmax,i,lastn;
    target=0.001;
    nmin=1;
    nmax=5000;
    n=(int)(nmax+nmin)/2;
    r=sideRatio(n);
    lastn=nmax;
    while (abs(lastn-n)>1){
        lastn=n;
        if (r>target){
            nmin=n;
        }
        else{
            nmax=n;
        }
        n=(int)(nmax+nmin)/2;
        r=sideRatio(n);
        //cout<<nmin<<','<< nmax <<',' << r << endl;
    }
    i=0;
    while (sideRatio(n+i)>target){
            i+=1;
        }
    cout<<n+i-1<<','<<sideRatio(n+i-1)<<','<<n+i<<','<<sideRatio(n+i) << endl;
    cout << ((float)(clock()-t))/CLOCKS_PER_SEC<<endl;

}
