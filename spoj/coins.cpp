#include <stdio.h>

int main()
{
  long long unsigned int n,a;
  while(scanf("%llu",&n)!=EOF)
  {
    a=n/2 + n/3 +n/4;
    if(a>= n)
    {
      printf("%llu",a);
    }
    else{
      printf("%llu",n);
    }
  }
  return 0;
}
