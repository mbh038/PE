function [ ti] = PE_0012( n)
    
% PE_0012

% Highly divisible triangular number

% What is the value of the first triangle number to have over five hundred divisors?

% MATLAB function divisors() requires license for Symbolic_Toolbox. Grr!

% See http://mathschallenge.net/library/number/number_of_divisors


ti=0;
i=1;
ndivs=1;
while ndivs<=n
    ndivs=1;
    ti=ti+i; % next triangle number
    fti=factor(ti);
    ftiu=unique(fti);
    for j=1:length(ftiu)
        ndivs=ndivs*(length(fti(fti==ftiu(j)))+1);
    end
    i=i+1;
end
%ti=ti(1:n);
end