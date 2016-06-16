function [ sumeven ] = PE_0002( maxf )
%   PE_0002

%   Even Fibonacci numbers

%   sum of all even valued members of the Fibonacci sequence that are less than 4 million

    terms=[];
    f=0;
    sumeven=0;
    n=1;
    while f < maxf
        f = fibo(n);
        terms=[terms,f];
        sumeven=sum(terms(mod(terms,2)==0)) ;
        n=n+1;
    end
end
   
function f = fibo(n)
    if ( ~isscalar(n) || n < 1 || n ~= fix(n))
        error('n must be a positive integer!');
    end
    if n <= 2
        f = 1;
    else
        f = fibo(n-2) + fibo(n-1);
    end

end