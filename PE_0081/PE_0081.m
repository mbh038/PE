function [ minPathSum ] = PE_0081( filename )
    
% PE_0081 

% Path sum: two ways

% Find the minimal path sum, in matrix.txt (right click and
%  "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix,
% from the top left to the bottom right by only moving right and down.

    M=csvread(filename);
    
    rows=size(M,1);
    cols=size(M,2);
    
    LSMrows=zeros(rows,cols);    
    LSMrows(1,1)=M(1,1);
    
    for col=2:cols
        LSMrows(1,col)=LSMrows(1,col-1)+M(1,col);
    end
    
    for row=2:rows
        LSMrows(row,1)=LSMrows(row-1,1)+M(1,row);
    end
    
    for row =2:rows
        for col = 2:cols
            LSMrows(row,col)=M(row,col)+min(LSMrows(row-1,col),LSMrows(row,col-1));
        end
    end
    
    minPathSum = LSMrows(end,end);

end

