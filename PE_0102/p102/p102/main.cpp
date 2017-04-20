//
//  main.cpp
//  p102
//
//  Created by Michael Hunt on 19/04/2017.
//  Copyright © 2017 Michael Hunt. All rights reserved.
//

//
//  main.cpp
//  p102
//
//  Created by Michael Hunt on 19/04/2017.
//  Copyright © 2017 Michael Hunt. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;
#include <time.h>

int main() {
    
    clock_t t;
    t = clock();

    char ch;
    int ax,ay,bx,by,cx,cy;
    int contains=0;
    bool cp0,cp1,cp2;

    ifstream tri("p102_triangles.txt");
    while(tri) {
        tri >> ax >> ch >> ay >> ch >> bx >> ch >> by >> ch >> cx >> ch >> cy;
        cp0=ax*by-ay*bx>0;
        cp1=bx*cy-by*cx>0;
        cp2=cx*ay-cy*ax>0;
        if ((cp0 && cp1  && cp2) || (!cp0 && !cp1 && !cp2)) contains+=1;
    }
    cout << contains << endl;
    cout << "Elapsed time: "  << ((float)(clock()-t))/CLOCKS_PER_SEC << "s" << endl;
    
    return 0;
}


