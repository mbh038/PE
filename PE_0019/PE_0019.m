function [ output_args ] = PE_0019( dow,year_begin,year_end )
% PE_0019

% Counting Sundays

% How many Sundays fell on the first of the month during the twentieth century
% (1 Jan 1901 to 31 Dec 2000)?

%   day: day of week (1 - Sunday through to 7 - Saturday): positive integer 1-7
%   year_begin: 01-01 of beginning year: positive integer
%   year_end:: 31-12 ofend year: positive integer > year_begin

% test for valid input:dow
if ~isscalar(dow)  || dow <1 || dow > 7 || dow ~= floor(dow)
    fprintf('Invalid input for year_begin. Enter a positive integer ')
    return
end

% test for valid input:year_begin
if ~isscalar(year_begin) || year_begin ~= floor(year_begin)
    fprintf('Invalid input for year_begin. Enter a positive integer ')
    return
end

% test for valid input:year_end
if ~isscalar(year_end) || year_end ~= floor(year_end) || year_end < year_begin
    fprintf('Invalid input for year_end. Enter a positive integer >= year_begin ')
    return
end

foms=0
for y=year_begin:year_end
foms=foms+sum(weekday(datetime(y,1:12,dow))==1)
end

end