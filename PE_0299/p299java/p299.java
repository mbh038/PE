public class p299{
  final static long L = 100000000;

  static long gcd(long m, long n) {
    if (m < n) { long t = m; m = n; n = t; }
    long r = m % n;
    if (r == 0) return n;
    else return gcd(n, r); }

  static long incenterCase(){
    long count = 0;
    for(long n = 1; n < L/2; n++)
      for(long m = 1; m < n; m++){
        if((m+n) % 2 == 0) continue;
        if(gcd(m,n)!=1) continue;
        long b = n*n - m*m;
        long d = 2*n*m;
        long sum = b+d;
        if(sum >= L) break;
        if(b == d) count += L/sum;
        else count += 2*(L/sum); }
    System.out.println(count);
    return count; }

  static long parallelCase(){
    long count = 0;
    for(long n = 1; n < L; n+=2)
      for(long m = 1; m < L; m++){
        if(gcd(m,n)!=1) continue;
        long g = 2*n*m;
        long a = n*n + 2*m*m;
        long b = g+a;
        if(b > L/2) break;
        count += (L-1)/(2*b); }
    System.out.println(count);
    return count; }

  public static void main(String[] args) {
    System.out.println(incenterCase() + parallelCase()); }
}
