function [ n ] = PE_0004( dig,lim )
%PALIN_PRODUCT Summary of this function goes here
%   Detailed explanation goes here

nums=10^dig-1:-1:10^(dig-1);

produ=nums'*nums;
produ=produ(produ<lim);
if isempty(produ)
    n=0;
    return
end
produ=sort(produ,'descend');

for i= 1:length(produ)
    if is_pal(produ(i))
        n=produ(i);
        return
    end
    n=0;
end


end

function pal=is_pal(n) 
  if (mod(n,10) == 0) 
      pal=false;
      return
  end
  r = 0;
  while (r < n) 
    r = 10 * r + mod(n,10);
    n =floor(n/10);
  end
  pal= n == r || n == floor(r / 10);
end
