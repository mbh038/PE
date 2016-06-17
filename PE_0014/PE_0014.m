function [amax,lenmax] = PE_0014(n)
    
% PE_0014 

% Longest Collatz sequence

% Which starting number, under one million, produces the longest chain?

    a=n;
        
    cs=zeros(1,n);
    trial=zeros(1,1000);
    newcs=collatz(a,trial);
    lenmax=length(newcs);
    amax=a;
    newcs=newcs(newcs<=n);  
    cs(newcs)=1;
    while a > 1     
        a=a-1;
        flag=false;
        if cs(a==1)
            flag=true;
        end
        if flag==false
            newcs=collatz(a,trial);  
            if length(newcs)>lenmax
                lenmax=length(newcs);
                amax=a;
            end
            newcs=newcs(newcs<=n);
            cs(newcs)=1;
        end
    end   
end


function [ cseq ] = collatz( n,trial)
      
    count=0;
    while n > 1
        count=count+1;
        trial(count)=n;
        if mod(n,2)==0
            n=n/2;
        else
            n=3*n+1;
        end
    end

    cseq=[trial(1:count),1];

end