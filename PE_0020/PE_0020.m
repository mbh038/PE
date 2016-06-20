function [ dsum ] = PE_0020( n )

% PE_0020 

% Factorial digit sum

% Find the sum of the digits in the number n!

% n is a  positive integer
% dsum is the sum of these digits

% get the digits of n?

nfact='1'
nstring=num2str(n);

if length(nstring)==1
    for i=2:n
      nfact=smult(num2str(i),nfact);
    end
end

if length(nstring)==2
    for i=2:9
      nfact=smult(num2str(i),nfact);
    end

    for i=10:n
       istring=num2str(i); 
       units=istring(2);
       tens=istring(1);
       unitsmult=smult(units,nfact);
       tensmult=dpshift(smult(tens,nfact),1);
       nfact=sadd(unitsmult,tensmult);
    end
end

if length(nstring)==3
    for i=2:9
      nfact=smult(num2str(i),nfact);
    end

    for i=10:99
       istring=num2str(i); 
       units=istring(2);
       tens=istring(1);
       unitsmult=smult(units,nfact);
       tensmult=dpshift(smult(tens,nfact),1);
       nfact=sadd(unitsmult,tensmult);
    end
    
    for i=100:n
       istring=num2str(i); 
       units=istring(3);
       tens=istring(2);
       hundreds=istring(1);
       unitsmult=smult(units,nfact);
       tensmult=dpshift(smult(tens,nfact),1);
       hundredssmult=dpshift(smult(hundreds,nfact),2);
       nfact=sadd(unitsmult,tensmult);
       nfact=sadd(nfact,hundredssmult);
    end
end

% sum the digits
dsum=0
for i=1:length(nfact)
  dsum=dsum+str2num(nfact(i))  
end
end

function smult=smult (digit,number)
% multiply a number by a single digit
% digit and number: strings of digits only. digit is a single digit.
% smult: string
    carry=0;
    for i = length(number):-1:1
        add=str2double(digit)*str2double(number(i))+carry;
        smult(i)=num2str(mod(add,10));
        carry=floor(add/10);
    end

    if carry >0
        carry=num2str(carry);
        smult=[carry,smult];
    end
end

function sadd=sadd (n1,n2)
% add two numbers
% n1 and n2: strings of digits only. 
% sadd: string
    if length(n1)>length(n2)
        for i=1:length(n1)-length(n2)
            n2=['0',n2];
        end
    elseif length(n2)>length(n1)
        for i=1:length(n2)-length(n1)
            n1=['0',n1];
        end
    end

    len = length(n1);
    carry =0;
    for i=len:-1:1
        add=str2double(n1(i))+str2double(n2(i))+carry;
        sadd(i)=num2str(mod(add,10));
        carry=floor(add/10);
    end
    if carry >0
        carry=num2str(carry);
        sadd=[carry,sadd];
    end
end

function sshift = dpshift(number,n)
% shifts number by n decimal places
% number: string
% n: positive integer
% numshift: string
    for i=1:n
        sshift=[number,'0'];
    end
end
