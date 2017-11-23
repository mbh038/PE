def t(n:Int) = 2L*n*n-1L

def solve(N:Int) = {

  val v=Array.tabulate(N+1)(t)
  var count=0

  for (n<-(2 to N)) { 
    val r=v(n)
    if (r==t(n)) count+=1
    if (r!=1) {
      if (r<N) spray(n,r.toInt,r)
      val p=r-2*n;
      if (p<N) spray(n+p.toInt,r.toInt,r)
    }
  }

  def spray(n:Int,p:Int,f:Long):Unit = {
    for (x <- (n to N by p)) {
      while (v(x)%f==0L) v(x)/=f
    }
  }

  count
}

require(solve(10000)==2202)

println(solve(50000000))  