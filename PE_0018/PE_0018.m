
% PE_0018

% Maximum path sum I

% By starting at the top of the triangle below and moving to adjacent numbers
% on the row below, find the maximum total from top to bottom of the triangle below

 M=csvread('PE_0018.txt');
 
 %greedy algorithm - always choose the largest option in the row below
 [mroute,msum ] = mgreedy(M);


u