function sumsqdiff=PE_0006(n)
    
    nums=1:n;
    sumsq=sum(nums.*nums);
    sqsum=sum(nums)^2;
    sumsqdiff=sqsum-sumsq;
end
