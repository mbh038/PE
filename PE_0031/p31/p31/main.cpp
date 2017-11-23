//
//  main.cpp
//  Project Euler 31
//  Exmples of dynamic programming
//
//  Created by Michael Hunt on 20/04/2017.
//  Copyright © 2017 Michael Hunt. All rights reserved.
//

#include <iostream>
//using namespace std;
#include <ctime>
#include <vector>

void print2D(std::vector<std::vector<int> >& vec)
{
    for(auto a : vec)
    {
        for (auto b : a)
        {
            std::cout << b  << "   ";
        }
        
        std::cout << std::endl;
        
    }
    std::cout << std::endl;
}

int coin_change(int n, std::vector<int>& deno)
{
    std::vector<std::vector<int> > dp(n+1);
    
    //print2D(dp);
    
    for(int i = 0; i < dp.size(); i++)
    {
        dp[i].resize(deno.size()+1);
    }
    
    //print2D(dp);
    
    for(size_t k = 0; k < dp.size(); k++)
    {
        dp[k][0] = 0;
    }
    
    //print2D(dp);
    
    for(size_t l = 0; l < dp[0].size(); l++)
    {
        dp[0][l] = 1;
    }
    
    //print2D(dp);
    
    for(int i = 1; i <= n; i++)
    {
        for(int j = 1; j <= deno.size(); j++)
        {
            dp[i][j] = ((i- deno[j-1]) >=0 ? (dp[i-deno[j-1]][j]) : 0) + dp[i][j-1];
        }
    }
    
    
    //print2D(dp);
    return dp[n][deno.size()];
}

//slowest (by far, for large n)
void ex31b(int m){
    int count=0;
    int a, b, c, d, e, f, g;
    for( a=m ; a>=0 ; a -= 200 )
        for( b=a ; b>=0 ; b -= 100 )
            for( c=b ; c>=0 ; c -= 50 )
                for( d=c ; d>=0 ; d -= 20 )
                    for( e=d ; e>=0 ; e -= 10 )
                        for( f=e ; f>=0 ; f -= 5 )
                            for( g=f ; g>=0 ; g -= 2 )
                                count++;
    std::cout<<"ex31b: count="<<count<<std::endl;;
}

//second fastest - how I did it in Python
void coinsum(int n)
{
    std::vector<int> coins = {1,2,5,10,20,50,100,200};
    std::vector<int> ways(n+1);
    ways[0]=1;
    
    while (coins.back()>n){
        coins.pop_back();
    }
    
    for (int i=0;i<coins.size();i++)
        for (int j=coins[i];j<=n;j++)
            ways[j]+=ways[j-coins[i]];
    
    std::cout<<ways.back()<<std::endl;
}

//fastest - gotclout (same code is 100x slower in Python for n=1000)
void dp(int n)
{
    const int m=8;
    int arr[n+1][m];
    int denom[m] ={1, 2, 5, 10, 20, 50, 100, 200};
    
    for(int a=0; a<n+1; a++)
        for(int b=0; b<m; b++)
            arr[a][b] = 1;
    
    for(int i=1; i<n+1; i++)
    {
        for(int j=1; j<m; j++)
        {
            if(i-denom[j] >=0)
                arr[i][j] = arr[i][j-1]+arr[i-denom[j]][j];
            else
                arr[i][j] = arr[i][j-1];
        }
    }
    std::cout << arr[n][m-1] << std::endl;
}

int main(int argc, char** argv)
{
    clock_t t;
    
    std::vector<int> deno = {1,2,5,10,20,50,100,200};
    int n  = 200;
    
    t = clock();
    std::cout << coin_change(n, deno)<<std::endl;
    std::cout << ((float)(clock()-t))/CLOCKS_PER_SEC<<"\n";
    
    t = clock();
    ex31b(n);
    std::cout << ((float)(clock()-t))/CLOCKS_PER_SEC<<"\n";
    
    t = clock();
    coinsum(n);
    std::cout << ((float)(clock()-t))/CLOCKS_PER_SEC<<"\n";
    
    t = clock();
    dp(n);
    std::cout << ((float)(clock()-t))/CLOCKS_PER_SEC<<"\n";
    
    return 0;
}

