#include<stdio.h>
void fib(int n)
{   
    int a,s=0;//a=next number in series after first,s=previous number in series number in series
    for(int i=1;i<=n;i++)
    {
        if(i==1)
        {
            a=0;
            printf("%d",i);
            s=a+i;
            continue;
        }
        printf(", ");
        printf("%d",a);
        s=a;
        a=a+s;
    }
}
main(){
    int n;
    printf("Enter Number Of terms in Series: ");
    scanf("%d",&n);
    fib(n);
    return 0;
}