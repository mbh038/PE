function [ lcm ] = PE_0005( n )
% PE_0005

% Smallest multiple

% What is the smallest positive number that is evenly divisible
% by all of the numbers from 1 to 20?

%check that n is a positive integer scalar
if ~isscalar(n) || n < 1 || n ~= floor(n)
    fprintf('Invalid input. Must be a positive integer scalar');
    return
end

maxval=intmax('uint64');

plist=primes(n);

for i=1:length(plist)
    powers(i)=1;
    while plist(i)^(powers(i)+1) <= n
        powers(i)=powers(i)+1;
    end
end
   
pplist=uint64(plist) .^uint64(powers) ;   

prod=uint64(1);
for i=1:length(pplist)
    prod=prod*pplist(i);
end

lcm=prod;

if lcm >= maxval
    lcm=uint64(0);
    return
end

end