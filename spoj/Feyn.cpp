#include <iostream>

int main()
{
int num;
int i,sum=0;
std::cin>>num;
for(i=1;i<=num;i++)
{
sum+=(i*i);
}
std::cout<<sum;
return 0;
}
