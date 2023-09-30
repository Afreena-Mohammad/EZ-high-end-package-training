#include<stdio.h>
main()
{
      int n,i ,j,a[5][5],m;
      printf("enter n value");
      scanf("%d",&n);
      printf("enter m value");
      scanf("%d",&m);
      printf("enter the elements");
      for(i=0;i<n;i++)
      {
	     for(j=0;j<m;j++)
	    {
	      scanf("\n%d",&a[i][j]);
        }
      }
       for(i=0;i<n;i++)
      {
            for(j=0;j<m;j++)
            {
                printf("\t%d",a[i][j]);
            }
            printf("\n");
      }
      printf("transpose of a matrix\n");
       for(i=0;i<n;i++)
      { 
	     for(j=0;j<m;j++)
		 {
            printf("\t%d",a[j][i]);
        }
        printf("\n");
      }
      printf("rotated matrix\n");
        for(i=0;i<m;i++)
      { 
	     for(j=0;j<n;j++)
		 {
            printf("\t%d",a[j+1][i+1]);
        }
        printf("\n");
      }
      
}
    
      
    
