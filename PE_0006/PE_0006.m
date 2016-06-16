function sumsqdiff=PE_0006(n)
    
% PE_0006

% Sum square difference

% Find the difference between the sum of the squares of the first one hundred
% natural numbers and the square of the sum.
    
    nums=1:n;
    sumsq=sum(nums.*nums);
    sqsum=sum(nums)^2;
    sumsqdiff=sqsum-sumsq;
end
