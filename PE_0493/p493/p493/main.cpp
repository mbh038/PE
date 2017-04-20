//
//  main.cpp
//  p493
//
//  Created by Michael Hunt on 19/04/2017.
//  Copyright © 2017 Michael Hunt. All rights reserved.
//

#include <iostream>
using namespace std;
#include <cmath>
#include <random>
#include <cstdlib>
#include <ctime>
#include <iomanip>

int main() {
    
    cout << fixed;
    cout << setprecision(9);
    
    srand((unsigned)time(NULL));
    double n=7.0,b=10.0,p=20.0;
    double trialsum=0.0;
    double newave=0.0,oldave=1.0;
    int dps=10;
    double count=0.0;
    double np,nc;
    int picks,ncols;
    double prob_np,randval;
    while (abs(newave-oldave)>1/pow(10,dps) || count < 10){
        //cout << "hello world"<<endl;
        count+=1;
        np=n*b;
        nc=0;
        picks=0;
        ncols=0;
        while (picks<p){
            prob_np=(double)np/(double)(np+nc);
            randval=(double)rand()/RAND_MAX;
            //cout << randval<<" " <<prob_np<<endl;
            if (randval<=prob_np){
                ncols+=1;
                np -= b;
                nc +=(b-1);
                //cout<<"new colour"<<ncols<<endl;
            }
            else{
                nc-=1;
                //cout<<"not new colour"<<endl;
            }
            picks+=1;
        }
        //cout<<ncols<<endl;
        trialsum+=ncols;
        oldave=newave;
        newave=(double)(trialsum)/(double) count;
        //cout <<ncols<<" "<<oldave<<" "<<newave<<endl;
        if ((int)count%100000000==0){
            //cout << fixed;
            //cout << setprecision(9);
            cout << newave;
            cout <<endl;
        }
    }
    cout << newave<<endl;
    return 0;
}


