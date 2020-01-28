#include<stdio.h>
void Prime(int num)
{
    int c =0; //no. of perfect divisors of num
    for(int i=1;i<=num;i++)
    {
        if(num%i==0)
            c++;
    }//code to check no. of perfect divisors
    if(c==2)
    {
        printf("Number Is Prime");
    }
    else{
        printf("Number Is Not Prime");
    }
}