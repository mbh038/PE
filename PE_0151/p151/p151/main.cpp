//
//  main.cpp
//  p151
//
//  Created by Michael Hunt on 29/04/2017.
//
//by PE user SMQ Wed, 25 Apr 2007, 14:30
//
//  Copyright © 2017 Michael Hunt. All rights reserved.
//
#include <iostream>
using namespace std;

double expected = 0.0;

struct Envelope {
    int A[6]; // number of sheets of each size (A0 is never used)
    
    Envelope() { A[1] = 1; A[2] = A[3] = A[4] = A[5] = 0; }
    
    Envelope(const Envelope & prev, int remove) {
        for(int i = 1; i <= 5; i++)
            A[i] = prev.A[i] + (i < remove ? 0 : i > remove ? 1 : -1);
    }
    
    int sheets() const { return A[1] + A[2] + A[3] + A[4] + A[5]; }
    
    void pickeach(int singles = 0, double probability = 1.0) const {
        if (sheets() == 0) {
            expected += probability * (singles - 2);
        } else {
            if (sheets() == 1) singles++;
            for(int i = 1; i <= 5; i++) if (A[i] > 0) {
                Envelope(*this, i).pickeach(singles, probability * A[i] / sheets());
            }
        }
    }
};

int main(void) {
    Envelope().pickeach();
    cout << expected << endl;
}
