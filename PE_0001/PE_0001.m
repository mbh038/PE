function [ s ] = PE_0001( n )
    
    %% Project Euler Problem 1
    
    % If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    % The sum of these multiples is 23.
    % Find the sum of all the multiples of 3 or 5 below 1000.
    
    tic
    %muls3and5=(1:n-1)/3-fix((1:n-1)/3)==0 | (1:n-1)/5-fix((1:n-1)/5)==0;
    %s=(1:n-1)*muls3and5'
    s = sum(3:3:n-1) + sum(5:5:n-1) - sum(15:15:n-1);
    toc
    
end