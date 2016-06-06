PE_0001= function (n){

    ## Project Euler Problem 1
    
    # If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    # The sum of these multiples is 23.
    # Find the sum of all the multiples of 3 or 5 below 1000.
    
    #tbegin=Sys.time()
    #muls3and5=seq(1:(n-1))/3-floor(seq(1:(n-1))/3)==0 | seq(1:(n-1))/5-floor(seq(1:(n-1))/5)==0
    #t(seq(1:(n-1)))%*%(muls3and5) 
    # or
    #sum(seq(1:(n-1))[muls3and5])
    
    sum(seq(3,n-1,3))+sum(seq(5,n-1,5))-sum(seq(15,n-1,15))
    #Sys.time()-tbegin

}