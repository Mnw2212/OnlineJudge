#include <stdio.h>

int main()
{
  float a,val=0.00;
  int i;
  scanf("%f",&a);
  while(a)
    {
      val=0.00;
      for(i=0;val<=a;i++)
        {
          val= val + (1/(2.0+i));
        }

        printf("%d card(s)\n",i);
        scanf("%f",&a);
    }
    return 0;
}
