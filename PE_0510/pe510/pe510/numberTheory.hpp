//
//  numberTheory.hpp
//  pe510
//
//  Created by Michael Hunt on 13/04/2017.
//  Copyright © 2017 Michael Hunt. All rights reserved.
//

#ifndef numberTheory_hpp
#define numberTheory_hpp

#include <stdio.h>

//Euler gcd
int gcd(int a, int b){
    int r = a % b;
    while (r>0){
        a=b;
        int tmp=b;
        b=r;
        r=tmp%r;
    }
    return b;
}

//Euker gcd with long long precision
int64_t longGcd(int64_t a, int64_t b){
    int64_t r = a % b;
    while (r>0){
        a=b;
        int64_t tmp=b;
        b=r;
        r=tmp%r;
    }
    return b;
}



#endif /* numberTheory_hpp */
