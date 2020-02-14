# Modular arithmetic

#from Wikipedia - faster than using Mods: inv(Mod(a,n)).val
function inverse(a, n)
    #returns multiplicative inverse of a mod n. a and n must be-co-prime
    t1,t2=0,1
    r1,r2=n,a
    while r2!=0
        q = div(r1,r2)
        t1, t2 = t2, t1 - q * t2
        r1, r2 = r2, r1 - q * r2
    end
    if t1 < 0
        t1 +=n
    end
    return t1
end

function extended_gcd(a, b)

    s,old_s = 0,1
    t,old_t = 1,0
    r,old_r = b,a

    while r != 0
        q = div(old_r,r)
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    end

    println( "Bézout coefficients:", old_s," ", old_t)
    println( "greatest common divisor:", old_r)
    println( "quotients by the gcd:", " ",t, " ",s)
end

function crt(a,n)
    # a=[a_0....a_i], n=[n_0...n_i] in x = a_i mod n_i (all n_i are co-prime)
    # returns unique solution for x, mod product of the n_i
    nprod=prod(n)
    xsum=0
    for i in 1:length(n)
        Ni=div(nprod,n[i])
        xsum+=a[i]*inverse(Ni,n[i])*Ni
    end
    return xsum %nprod
end

using Mods
function test(trials=1000000,n=123456789123456789,m=10^9+7)

    @time for i in 1:trials; a=powermod(n,123456789,m); end #4 x faster for small powers
    @time for i in 1:trials; b=(Mod(n,m)^123456789).val; end
end

# #from Rosetta code
# def mul_inv(a, b):
#     b0 = b
#     x0, x1 = 0, 1
#     if b == 1: return 1
#     while a > 1:
#         q = a // b
#         a, b = b, a%b
#         x0, x1 = x1 - q * x0, x0
#     if x1 < 0: x1 += b0
#     return x1
#
# # from PE user fakesson
# def invmod(b, n):    #modinv
#   x0, x1 = 1, 0
#   while n:
#     (q, n), b = divmod(b,n), n
#     x0, x1 = x1, x0 - q * x1
#   return x0
