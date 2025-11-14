#include<stdio.h> 
int main(){
    int star;
    scanf("%d",&star); //9

    int temp = star;

    for(int i=1;i<=temp;i++){  
        
        int m=2*i-1;
        for(int j=star-i;j>=1;j--){printf(" ");}
          
        for(int s=1;s<=m;s++){printf("*");}
         printf("\n");
      }
    
   return 0;
    
}