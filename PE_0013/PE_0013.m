function [ C ] = PE_0013( filename,n )
    
% PE_0013

% Large sum

% Work out the first ten digits of the sum of the following one-hundred 50-digit numbers

fid = fopen(filename,'rt');
if fid < 0c
    fprintf('error opening file\n');
    return;
end

% Read file as a set of strings, one 50 digit number per line:
line_number = 1;
oneline{line_number} = fgetl(fid);
while ischar(oneline{line_number})
    line_number = line_number + 1;
    oneline{line_number} = fgetl(fid);
end
fclose(fid);

% remove empty array in last element of cell.
oneline=oneline(1,1:100);

% add the lines using traditional arithmetic
carry=0;
for i=50:-1:1
    add=0;
    for j=1:100
        newline=oneline{j};
        add=add+str2double(newline(i));
    end
    add=add+carry;
    C(i)=num2str(mod(add,10));
    carry=floor(add/10);
end

% include the last carry at the beginning
carry=num2str(carry);
C=[carry,C];
        
% get first n digits of the sum
C=C(1:n);

end