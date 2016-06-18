function [ routes ] = PE_0015( m,n )
    
% PE_0015 

% Lattice paths

% Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
% there are exactly 6 routes to the bottom right corner. 
% How many such routes are there through a 20×20 grid?

% m,n = steps along each side of the rectangular grid

routes=nchoosek(uint64(m+n),uint64(n));

end