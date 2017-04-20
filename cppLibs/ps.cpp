//
//  ps.cpp
//  
//
//  Created by Michael Hunt on 17/04/2017.
//
//


#include<iostream>
#include "ps.hpp"
#include "numberTheory.hpp"
#include <vector>
#include<time.h>
using namespace std;


int main(){
    
    clock_t t;
    t = clock();
    
    Choose choices;
    
    for (int i=10;i<=101;i++){
        std::cout <<i<<","<< choices.Evaluate(i,(int)i/2) <<"\n";
    }
    std::cout << ((float)(clock()-t))/CLOCKS_PER_SEC<<"\n";
    return 0;
}
