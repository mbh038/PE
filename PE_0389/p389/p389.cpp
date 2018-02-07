//
//  p389.cpp
//  
//
//  Created by Michael Hunt on 14/01/2018.
//

#include "p389.hpp"

#include <cstdio>
#include <iostream>
using namespace std;

const int N = 4 * 6 * 8 * 12 * 20 + 10;

double ans[N], f[N], g[N];

int dp(int n, int d) {
    for (int i = 0; i <= n * d; ++i)
        f[i] = g[i] = 0;
    f[0] = 1;
    for (int i = 1; i <= n; ++i) {
        for (int j = n * d; j >= 0; --j) {
            f[j] = 0;
            for (int k = 1; k <= d && k <= j; ++k)
                f[j] += f[j - k] / d;
        }
        for (int j = 1 * i; j <= d * i; ++j)
            g[j] += f[j] * ans[i];
    }
    for (int i = 0; i <= n * d; ++i)
        ans[i] = g[i];
    return n * d;
}

int main() {
    ans[1] = 1;
    int n = 1;
    n = dp(n, 4);
    cout<<"4: "<<n<<"\n";
    n = dp(n, 6);
    cout<<"6: "<<n<<"\n";
    n = dp(n, 8);
    cout<<"8: "<<n<<"\n";
    n = dp(n, 12);
    cout<<"12: "<<n<<"\n";
    n = dp(n, 20);
    cout<<"20: "<<n<<"\n";
    
    double Ex = 0, Ex2 = 0;
    for (int i = 0; i <= n; ++i) {
        Ex  += ans[i] * i;
        Ex2 += ans[i] * i * i;
    }
    printf("%.4f\n", Ex2 - Ex * Ex);
    return 0;
}
