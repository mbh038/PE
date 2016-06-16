function [ digits,mp ] = PE_0008( filename,n )
    
%   PE_0008 

%   Largest product in a series

%   Find the thirteen adjacent digits in the 1000-digit number
%   that have the greatest product. 
%   What is the value of this product?

fid = fopen(filename,'rt');
if fid < 0
    fprintf('error opening file\n');
    return;
end

% Read file as a set of strings, one per line:
line_number = 1;
oneline{line_number} = fgetl(fid);
while ischar(oneline{line_number})
    line_number = line_number + 1;
    oneline{line_number} = fgetl(fid);
end
fclose(fid);

oneline=[oneline{1,1:20}];

mp=-Inf;
for i=1:length(oneline)-n+1
    trial=oneline(i:i+n-1);
    prod=uint64(1);
    for j=1:n
        prod=prod*uint64(str2num(trial(j)));
    end
    if prod > mp
        mp=prod;
        digits=trial;
    end
end

end