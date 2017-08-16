//
//  p010.cpp
//  
//
//  Created by Michael Hunt on 16/05/2017.
//
//

#include <primesieve.hpp>
#include <iostream>
#include <ctime>

using namespace std;

int main()
{
    clock_t t;
    t = clock();
    
    primesieve::iterator it;
    uint64_t prime = it.next_prime();
    uint64_t sum = 0;
    
    // iterate over the primes below 2 million
    for (; prime < 2000000ull; prime = it.next_prime())
        sum += prime;
    
    cout << "Sum of the primes below 2 million = " << sum << endl;
    cout << ((float)(clock()-t))/CLOCKS_PER_SEC<<"\n";
    return 0;
}


