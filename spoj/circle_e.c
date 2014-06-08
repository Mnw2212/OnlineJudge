#include <stdio.h>
#include <math.h>

int main()
{
  int n,i;
  double a,b,c,d;
  scanf("%d",&n);
  for(i=0;i<n;i++)
  {
    scanf("%lf %lf %lf",&a,&b,&c);
    a=1/a;
    b=1/b;
    c=1/c;
    d=(a*b)+(b*c)+(c*a);
    printf("%0.6lf\n",1/(a+b+c+(2*(sqrt(d)))));
  }
  return 0;
}
