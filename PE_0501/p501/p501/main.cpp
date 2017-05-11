//
//  main.cpp
//  p501
//
//  Created by Michael Hunt on 06/05/2017.
//  Copyright © 2017 Michael Hunt. All rights reserved.
//

// 197912312715
// 1997171674

#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
using namespace std;
#include <stdint.h>
#include <ctime>
typedef long long ll;
#include <memory>
#include <stdexcept>
#include <array>
#include <vector>
#include <tuple>
#include <math.h>
#include <algorithm>
#include <gmp.h>


template<class Iterator>
Iterator Unique(Iterator first, Iterator last)
{
    while (first != last)
    {
        Iterator next(first);
        last = std::remove(++next, last, *first);
        first = next;
    }
    
    return last;
}

// captures as a string results sent to console by primecount
string exec(const char* cmd) {
    array<char, 128> buffer;
    string result;
    shared_ptr<FILE> pipe(popen(cmd, "r"), pclose);
    if (!pipe) throw runtime_error("popen() failed!");
    while (!feof(pipe.get())) {
        if (fgets(buffer.data(), 128, pipe.get()) != NULL)
            result += buffer.data();
    }
    return result;
}

/*
 This uses Kim Walisch's fast prime counting function implementation. This is a command line function
 that outputs to the console - we need to divert the result to a string and convert to a (ll) integer
 that we can use
 https://github.com/kimwalisch/primecount
 */

ll primecount(ll n) {
    
    string result;
    string primecount ("/Users/mbh/Documents/cspace/primesieve-6.0/./primesieve -q  ");
    string nstr (to_string(n));
    string usethis;
    usethis=primecount+nstr;
    const char * cmd = usethis.c_str();
    result=exec(cmd);
    return stoll(result.erase (0,8));
//    stringstream ss;
//    ll asInt = 0;
//    ss << result2;
//    ss >> asInt;
//    ss.str(""); //clear the stringstream
//    ss.clear();
//    return asInt;
    
}

vector<ll> primesieve(ll n){
    string primecount ("/Users/mbh/Documents/cspace/primesieve-6.0/./primesieve ");
    string nstr (to_string(n));
    string filename (" -p > /Users/mbh/Documents/PE/PE_0501/p501/p501/psieve.txt");
    string usethis;
    usethis=primecount+nstr+filename;
    //cout<<usethis<<endl;
    const char * cmd = usethis.c_str();
    exec(cmd);
    ifstream file("/Users/mbh/Documents/PE/PE_0501/p501/p501/psieve.txt");
    vector<ll>primes;
    int number;
    while(file >> number)
        primes.push_back(number);
    
    return primes;
}

vector<tuple<ll,ll>> primeProd(ll limit){
    ll p2limit=pow(limit/2,0.5);
    vector<ll> ps=primesieve(p2limit);
    vector<ll> qs=ps;
    
    vector<tuple<ll,ll>> pp;
    for (ll i=0;i<ps.size();i++){
        for (ll j=i+1;j<qs.size();j++){
            ll p2 = qs[j];
//            if (p2<=ps[i])
//                continue;
            ll prod = ps[i]*qs[j];
            if (limit/prod <=p2)
                break;
            pp.push_back(make_tuple(p2,prod));
        }
    }
//    pp.erase( Unique( pp.begin(), pp.end() ), pp.end() );
    sort(pp.begin(), pp.end(), [](const std::pair<int,int> &left, const std::pair<int,int> &right) {
        return left.first < right.first;
    });
    return pp;
}

ll sum3 (ll limit){
    vector<tuple<ll,ll>> pps;
    pps=primeProd(limit);
    ll sum3=0;
    ll lastp2=0;
    ll p2pc=0;
    for (int i=0;i<pps.size();i++){
        ll p2 = get<0>(pps[i]);
        if (p2>lastp2){
            lastp2=p2;
            p2pc=primecount(p2);
        }

        ll prod = get<1>(pps[i]);
        sum3+=primecount(limit/prod)-p2pc;
        //cout<<p2<<","<<prod<<","<<limit/prod<<","<<primecount(limit/prod)<<","<<p2pc<<endl;
    }
    return sum3;
    
}

int main(){

    clock_t t;
    t = clock();
    
    ll limit = 1e6;
    
    cout << sum3(limit)<<endl;
    
//    ll n = 1e2;
//    vector<ll> primes;
//    vector<tuple<ll,ll>> pps;
//    vector<ll> primes=primesieve(pow(limit/2,0.5));
//    cout<<primes.size()<<endl;
//    vector<tuple<ll,ll>> pps=primeProd(limit);
//    cout<<pps.size()<<endl;
//    for (int i=0;i<pps.size();i++)
//        cout<<get<0>(pps[i])<<","<<get<1>(pps[i])<<endl;
//    for (int i=1;i<12;i++)
//        cout<<i<<": "<<primecount((ll)pow(10,i))<<endl;
    cout << ((float)(clock()-t))/CLOCKS_PER_SEC<<"\n";
}

