
define carmichael(n,verbose){
    auto number,index,q[],a[],phi_n[],result,i,j,t,prime_count,u

    if(n%2 && n>1){
        print n," is odd!\n"
        print "The number of solutions x of phi(x)=",n, " is "
        return(0)
    }
    prime_count=divisor_pminus1(n)
    /* This produces the primes p in increasing size, such that p-1 divides n */
    prime_found[prime_count]=0
    number=0
    index=0
    q[0]=2

    if(verbose==0){
        print "Solutions of phi(x)=",n,":\n"
    }else{
        print "Testing Carmichael's conjecture for phi(x)=",n,":\n"
    }
    if(n==1){
        print "1: 1 2\n"
        print "The number of solutions x is "
        return(2)
    }
    phi_n[0]=n
    while(1){
        if(phi_n[index]==1) {
            number=number+1
            result=construct_n(q[],a[],index)
            print result," "
            if(number==2 && verbose){
                print "are two solutions\n"
                return
            }
            index=index-1
        }else{
            if(q[index] == 0 || (index < prime_count && q[index]>phi_n[index]+1)){
                if(index==0){
                    print "\n"
                    print "The number of solutions x is "
                    return(number)
                }
                if(phi_n[index]%q[index-1]==0){
                    a[index-1]=a[index-1]+1
                    phi_n[index]=phi_n[index]/q[index-1]
                    q[index]=q[index-1]
                }else{
                    index=index-1
                }
            }else{
                if(phi_n[index]%(q[index]-1)==0){
                    phi_n[index+1]=phi_n[index]/(q[index]-1)
                    q[index+1]=q[index]
                    a[index]=1
                    index=index+1
                }
            }
        }
        for(u=0;u<prime_count;u++){
            if(q[index]==prime_found[u]){
                q[index]=prime_found[u+1]
                break
            }
        }
    }
}

define divisor_pminus1(n){
    auto list[],i,j,k,t,d,list_length,e,f,l,m,prime_count
    /*
     if(verbose){
     print "The divisors of ",n," are "
     }*/
    t=omega(n)
    list_length=kglobal[0]+1
    prime_count=0
    for(k=0;k<list_length;k++){
        list[k]=(qglobal[0])^k
        d=list[k]
        l=d+1
        f=lucas0(l)
        if(f){
            /*if(n%d==0){*/
            prime_found[prime_count]=l
            prime_count=prime_count+1
            /*}*/
        }
        /*if(verbose){
         print d," "
         }*/
    }
    for(i=1;i<t;i++){
        e=list_length
        for(k=0;k<list_length;k++){
            for(j=1;j<=kglobal[i];j++){
                d=list[k]*(qglobal[i]^j)
                l=d+1
                f=lucas0(l)
                if(f){
                    if(n%d==0){
                        prime_found[prime_count]=l
                        prime_count=prime_count+1
                    }
                }
                list[e]=d
                /* if(verbose){
                 print d," "
                 }*/
                e=e+1
            }
        }
        list_length=list_length*(kglobal[i]+1)
        /*print"\n"*/
    }
    /*if(verbose){
     print "There are ", prime_count, " primes p such that p-1 divides ",n,": "
     for(m=0;m<prime_count;m++){
     print prime_found[m]," "
     }
     print"\n"
     }*/
    temp=sort_array(prime_found[],prime_count)
    for(m=0;m<prime_count;m++){
        prime_found[m]=output_array[m]
    }
    return(prime_count)
}

define sort_array(a[],n){
    auto i,j,temp,s,t

    t=n-1
    for(i=0;i<t;i++){
        s=i+1
        for(j=s;j<n;j++){
            if(a[i]>a[j]){
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
            }
        }
    }
    for(i=0;i<n;i++){
        output_array[i]=a[i]
    }
}

define construct_n(q[],a[],n){
    auto i,result
    result=1
    for(i=0;i<n;i++){
        for(j=0;j<a[i];j++){
            result=result*q[i]
        }
    }
    return(result)
}

define tree(n,p){
    auto j,g,e,number
    prime_count=divisor_pminus1(n)
    print "prime_count=",prime_count,"\n"
    number=0
    j=0
    for(j=0;j<prime_count;j++){
        if(prime_found[j]>p){
            g=0
            while(g>=0){
                e=(prime_found[j]^g)*(prime_found[j]-1)
                if(n%e==0){
                    print "(",prime_found[j],",",g,",",n/e,") "
                    number=number+1
                }else{
                    break
                }
                g=g+1
            }
        }
    }
    print "\n"
    return(number)
}

define carmichael_k(n){
    auto prime_count,j,g,e,temp1,temp2,temp3,t
    e=n
    j=0
    prime_count=divisor_pminus1(n)
    while(j<prime_count){
        p[j]=prime_found[j]
        if(e%(p[j]-1)==0){
            g=0
            f=e/(p[j]-1)
            while(g>=0){
                if(f%p[j]==0){
                    print "(",p[j],",",g,",",f,")\n"
                    f=f/p[j]
                }else{
                    print "(",p[j],",",g,",",f,")\n"
                    break
                }
                g=g+1
            }
        }
        j=j+1
    }
}

define carmichael_nodes(n){
    auto number,index,q[],a[],phi_n[],result,i,j,t,prime_count,u

    if(n%2 && n>1){
        print n," is odd!\n"
        print "The number of solutions x of phi(x)=",n, " is "
        return(0)
    }
    prime_count=divisor_pminus1(n)
    /* This produces the primes p in increasing size, such that p-1 divides n */
    prime_found[prime_count]=0
    number=0
    index=0
    q[0]=2

    print "Solutions of phi(y) divides ",n," and phi(x)=",n,":\n"
    if(n==1){
        print "1: 1 2\n"
        print "The number of solutions x is "
        return(2)
    }
    phi_n[0]=n
    while(1){
        if(phi_n[index]==1) {
            number=number+1
            result=construct_n(q[],a[],index)
            print ": x = ",result," "
            index=index-1
            print "\n"
        }else{
            if(q[index] == 0 || (index < prime_count && q[index]>phi_n[index]+1)){
                if(index==0){
                    print "\n"
                    print "The number of solutions x is "
                    return(number)
                }
                if(phi_n[index]%q[index-1]==0){
                    a[index-1]=a[index-1]+1
                    phi_n[index]=phi_n[index]/q[index-1]
                    q[index]=q[index-1]
                    print "(",index,": ",q[index],",",a[index-1]-1,",",phi_n[index],") "
                    result=construct_n(q[],a[],index)
                    print "(y=",result,") "
                }else{
                    print "\n"
                    index=index-1
                }
            }else{
                if(phi_n[index]%(q[index]-1)==0){
                    phi_n[index+1]=phi_n[index]/(q[index]-1)
                    print "(",index+1,": ",q[index],",0,",phi_n[index+1],") "
                    q[index+1]=q[index]
                    a[index]=1
                    index=index+1
                    result=construct_n(q[],a[],index)
                    print "(y=",result,") "
                }
            }
        }
        for(u=0;u<prime_count;u++){
            if(q[index]==prime_found[u]){
                q[index]=prime_found[u+1]
                break
            }
        }
    }
}
