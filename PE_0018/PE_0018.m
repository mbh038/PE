function [msum,gsum]=PE_0018(filename)

% PE_0018

% Maximum path sum I

% By starting at the top of the triangle below and moving to adjacent numbers
% on the row below, find the maximum total from top to bottom of the triangle below

triangle=csvread(filename);
 
 %greedy algorithm - always choose the largest option in the row below
 [mroute,gsum ] = mgreedy(triangle);
 
 frontier=triangle(end,:);
 
for line = (size(triangle,1)-1:-1:1)
    
    newline=triangle(line,:);
    newline=newline(newline>0);
    newFrontier=zeros(1,length(newline));
    for number =1:length(newline);
        newFrontier(number)=newline(number)+max(frontier(number),frontier(number+1)); 
    end
    frontier=newFrontier;
end

msum=frontier;

end
