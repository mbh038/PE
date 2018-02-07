//
//  main.cpp
//  p371
//
//  Created by Michael Hunt on 21/01/2018.
//  Copyright © 2018 Michael Hunt. All rights reserved.
//

#include <iostream>
#include <iomanip>
#include <vector>

// a simple pseudo-random number generator
// (produces the same result no matter what compiler you have - unlike rand() from math.h)
unsigned int myrand()
{
    // copied from problem 227
    static unsigned long long seed = 0;
    seed = 6364136223846793005ULL * seed + 1;
    return (unsigned int)(seed >> 30);
}

// simulate random journeys ...
double monteCarlo(unsigned int numPlates, unsigned int iterations)
{
    unsigned int numPlatesSeen = 0;
    for (unsigned int i = 0; i < iterations; i++)
    {
        // true if plate was seen
        std::vector<bool> seen(numPlates, false);
        
        while (true)
        {
            // generate a new plate
            auto plate = myrand() % numPlates;
            numPlatesSeen++;
            
            // look for matching plate (so that sum is 1000)
            if (plate != 0) // 0 isn't matched by any other plate
            {
                auto other = numPlates - plate;
                if (seen[other])
                    break;
            }
            
            // mark current plate as "seen"
            seen[plate] = true;
        }
    }
    
    return numPlatesSeen / double(iterations);
}

// and now smarter, faster, more precise ...
double search(unsigned int numPlates)
{
    // how I compute the expected number:
    // E              = 1 + fail * E
    // E - fail * E   = 1
    // E * (1 - fail) = 1
    // E              = 1 / (1 - fail)
    // if there is another state transition E2 then with similar argument
    // E = 1 + fail * E + good * E2
    // E = (1 + good * E2) / (1 - fail)
    
    // Seth may observe at most 499 "ordinary" plates
    // => zero and 500 are "special"
    const auto maxHave = numPlates / 2 - 1;
    
    // several times I have to divide by numPlates and have to make sure the result is a double,
    // so let's convert it to double once and keep using plates instead of numPlates from here on
    const double plates = numPlates; // actually I thought about invPlates = 1 / double(numPlates)
    
    // track expected number of plates you still have to see if n unpaired plates were already observed
    // there is a significant difference whether the "500" plate was seen or not !
    std::vector<double> have500(maxHave + 1, 0);
    std::vector<double> no500  (maxHave + 1, 0);
    
    // probabilities:
    // observe an "old" plate, nothing changes (but the expected number)
    auto probDuplicate = maxHave / plates;
    // observe a  "000" plate, nothing changes (but the expected number)
    auto probZero      =    1    / plates;
    // observe a  "500" plate, stop if already saw a "500", otherwise store it
    auto prob500       =    1    / plates;
    
    // solve the base case: all 499 plates already seen
    // compute probability that the next plate still doesn't finish the game
    auto probUnchanged = probDuplicate + probZero;
    // now find expected number in case Seth 499 plates plus the "500" plate
    have500[maxHave]   =  1                               / (1 - probUnchanged);
    // and find expected number in case Seth 499 plates BUT NOT the "500" plate
    no500  [maxHave]   = (1 + prob500 * have500[maxHave]) / (1 - probUnchanged);
    
    // continue the computation for 498, 497, ..., 1, 0 observed plates
    for (int have = maxHave - 1; have >= 0; have--)
    {
        // determine number of unpaired plates (exclude zero and 500)
        auto numNew  = plates - 2*have - 2;
        // probability that the plate wasn't seen before but pairs with no other plate yet
        auto probNew = numNew / plates;
        
        // it becomes less probable to see an "old" plate ...
        probDuplicate = have / plates;            // same as probDuplicate -= 1 / plates
        probUnchanged = probDuplicate + probZero; // same as probUnchanged += 1 / plates
        
        // same as above: E = (1 + good * E2) / (1 - fail)
        have500[have] = (1                           + probNew * have500[have + 1]) / (1 - probUnchanged);
        no500  [have] = (1 + prob500 * have500[have] + probNew * no500  [have + 1]) / (1 - probUnchanged);
    }
    
    // no plate seen yet, not even "500"
    return no500[0];
}

int main()
{
    unsigned int numPlates = 1000;
    std::cin >> numPlates;
    
    std::cout << std::fixed << std::setprecision(8);
    std::cout << search(numPlates) << std::endl;
    
    // run simulation
//    while (true)
//    std::cout << monteCarlo(numPlates, 1000000) << std::endl;
    
    return 0;
}
