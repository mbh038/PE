function [ n ] = PE_0004( dig,lim )
%PALIN_PRODUCT Summary of this function goes here
%   Detailed explanation goes here

nums=10^(dig-1):10^dig-1;

count=0;
prod=zeros(length(nums));
for i=1:length(nums)
    for j=1:length(nums)
        prod(i,j)=nums(i)*nums(j);
    end
end

produ=unique(prod);
produ=produ(:);

palins=zeros(length(produ),1);
count=0;
tic

for i=1:length(produ)
    str=num2str(produ(i));
    strinv=flip(str);
    if str==strinv
        count=count+1;
        palins(count)=str2num(str);
    end
end
toc


if lim <min(palins)
    n=0;
else
    n=max(palins(palins<lim));
end

end