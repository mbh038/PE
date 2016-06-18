function [ digits,dsum ] = PE_0016( n )
    
% PE_0016 

% Power digit sum

% What is the sum of the digits of the number 2^1000?

% n is power to which 2 is to be raised
% digits is a cell array containing the digits of 2^n, in base 10.
% dsum is the sum of these digits

    % find the digits in base 10 of 2^n
    digits=cell(1,1000);
    
    digits{1}='2';
    count=1;
    
    for i=2:n
        carry=0;
        for j=1:count
            mult=2*str2num(digits{j})+carry;
            digits{j}=num2str(mod(mult,10));
            carry=floor(mult/10);
        end
        if carry == 1
            count=count+1;
            digits{count}='1';
        end
    end
    
    digits=flip(digits(~cellfun(@isempty, digits)));
    
    % now add the digits
    dsum=0;
    for i=1:length(digits)
        dsum=dsum+str2num(digits{i});
    end

end