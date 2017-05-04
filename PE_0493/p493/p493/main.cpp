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
#include <ctime>
#include <vector>

int64_t factorial(int64_t n)
{
    return (n == 1 || n == 0) ? 1 : factorial(n - 1) * n;
}

int64_t nCk(int64_t n, int64_t k)
{
    return factorial(n)/(factorial(n-k)*factorial(k));
}

void counting(int perColour,int p)
{
    int colours=7;
    int a,b,c,d,e,f,g;
    vector<int64_t> ncks;
    
    for (int k=0;k<=perColour;k++){
        ncks.push_back(nCk(perColour,k));
    }
    
    vector<int64_t> nColours(colours+1);
    
    for (a=0;a<=perColour;a++) for (b=0;b<=perColour;b++) for (c=0;c<=perColour;c++) for (d=0;d<=perColour;d++) for (e=0;e<=perColour;e++) for (f=0;f<=perColour;f++) for (g=0;g<=perColour;g++)
    {
        vector <int64_t> pick;
        if (a+b+c+d+e+f+g==p){
            if (a>0) pick.push_back(a);
            if (b>0) pick.push_back(b);
            if (c>0) pick.push_back(c);
            if (d>0) pick.push_back(d);
            if (e>0) pick.push_back(e);
            if (f>0) pick.push_back(f);
            if (g>0) pick.push_back(g);
        }
        if (pick.size()==0) continue;
        
        int64_t newWays=1;
        for (int i=0;i<pick.size();i++)
        {
            newWays*=ncks[pick[i]];
        }
        nColours[pick.size()]+=newWays;
    }

    double num=0,den=0;
    for (int i=0;i<nColours.size();i++)
    {
        num+=i*nColours[i];
        den+=nColours[i];
    }
    cout.precision(10);
    cout<<num/den<<endl;
}


int main()
{
    clock_t t;
    t = clock();
    
    int perColour=10,picks=20;
    counting(perColour,picks);
    
    cout << ((float)(clock()-t))/CLOCKS_PER_SEC<<"\n";
    
    return 0;
}

/*
nCks=[sc.misc.comb(b,k) for k in range(b+1)]
colours={k:0 for k in range(n+1)}

for a in it.product([x for x in range(b+1)],repeat=n):
if(sum(a)==p):
valid=np.array(a)
valid=valid[valid>0]
newWays=np.prod(np.array([nCks[x] for x in valid]))
colours[len(valid)]+=newWays

meancol=sum([k*v for k,v in colours.items()])/sum([v for k,v in colours.items()])
 
*/


