function [ a,b,c,psum,product ] = PE_0009()
%PE_0009 

% A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
%
% a^2 + b^2 = c^2
%
% There exists exactly one Pythagorean triplet for which a + b + c = 1000.
% Find the product abc.


k=1;
n=0;
while n<1000

    m=n+1:1000; % m>n
    n=n+1;
    m=m(iscoprime([m,n]) == 1 & mod(m-n,2)~=0); %m,n coprime, m-n odd

    fprintf('n: %d, there are %d ms\n',n,length(m)) 

    as=k*( m.^2-n^2);
    bs=k*(2*m*n);
    cs=k*(m.^2+n^2);

    for i=1:length(as)        
        if as(i)+bs(i)+cs(i) == 1000
            a=as(i);
            b=bs(i);
            c=cs(i);           
            psum=as(i)+bs(i)+cs(i);
            product=as(i)*bs(i)*cs(i);
            return
        end
    end
end

end

function GCD = iscoprime(x) % assuming x is an array, 
    GCD = x(1);             % returning greatest common divisor for the array
    for i=1:size(x, 2)
        GCD = gcd(GCD, x(i));
    end
end

