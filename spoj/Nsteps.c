#include <stdio.h>

int main(void)
{
	int i,num,a,b;
	scanf("%d",&num);
	for(i=0;i<num;i++)
	{
	
		scanf("%d %d",&a,&b);
		if(a>=b)
		{
			if(a%2==0 && b%2==0)
			{
				printf("%d\n",a+b);
			}
			else if(a%2==1 && b%2==1)
			{
				printf("%d\n",a+b-1);
			}
			else
			printf("No Number\n");
		}
		else
			printf("No Number\n");
}

return 0;
}


