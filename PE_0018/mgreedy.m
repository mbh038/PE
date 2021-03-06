function [ mroute,gsum ] = mgreedy( M )

% PE_0018

% Maximum path sum I

% By starting at the top of the triangle below and moving to adjacent numbers
% on the row below, find the maximum total from top to bottom of the triangle below

 % greedy algorithm
 
    [nrow,ncol]=size(M);

    
    msum=zeros(nrow,1);
    msum(1)=M(1,1);
    mroute=zeros(nrow,1);
    mroute(1)=M(1,1);
    col=1;
    for i=2:nrow

       if M(i,col+1) >= M (i,col)
           col=col+1;
       end
       msum(i)=msum(i-1) +M(i,col);
       mroute(i)=M(i,col);
    end
    
    gsum=msum(end);
end

