function [ fibn ] = PE_0025( n)
    
% PE_0025 Summary of this function goes here

% 1000-digit Fibonacci number

% What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

% uses Guttage python code (Guttag p294) using a memo.

% only works up to fib(n) < intmax('uint64')

    fibn=fastFib(n);

end

function fibn = fastFib(n,memo)

    if nargin == 1
        memo = containers.Map;
    end
    
    if n == 1 || n == 2
        fibn = 1;
        return
    end
    
    if ~isKey (memo,num2str(n))
        result = fastFib(n-1,memo) + fastFib(n-2,memo);
        memo(num2str(n))=uint64(result);
        fibn=result;
        return
    else
        fibn=memo(num2str(n));
        return
    end

end