#include <stdio.h>
long long f(long long n)
{
  long long a;
  a=f(n/2) + f(n/3) + f(n/4);

  if(a>=n )
  {
    return a;
  }
  else{
    return n;
  }
}
int main()
{
  long long int n;
  while(scanf("%lld",&n)!=EOF)
  {
    printf("%lld",f(n));
  }
  return 0;
}
