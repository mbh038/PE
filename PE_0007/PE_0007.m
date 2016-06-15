function [ n,count ] = PE_0007( target )
%PE_0007 Summary of this function goes here
%   find the 10 001st prime number

    huge=1e6;
    tiny=1;
    count=0;
    current=floor((huge-tiny)/2);
    while length(primes(current)) ~=target
        count=count+1;
        if count > 1000
            fprintf('Too many iterations (1000)');
            break
        end
        current=floor((huge+tiny)/2);
        if length(primes(current))>target
            huge=(huge+current)/2;
        elseif length(primes(current))<target           
            tiny=(tiny+current)/2;
        end       
    end
    n=primes(current);
    n=n(end);
end