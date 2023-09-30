#include<stdio.h>
main()
{
      int i,a[i],r1,r2,n;
      printf("enter n value\n");
      scanf("%d",&n);
      printf("enter range1\n");
      scanf("%d",&r1);
	  printf("enter range2\n");
      scanf("%d",&r2);
      printf("enter the elements");
      {
	  
      for(i=0;i<n;i++)
      {
	     
	      scanf("\n%d",&a[i]);
        
      }
       for(i=0;i<n;i++)
      {
           printf("\t%d",a[i]);
       }
     }
      printf("even numbers=\n");
      for(i=0;i<n;i++)
        {
		if(a[i]%2==0)
		{
			while(r1<r2)
			{
		
      
      	     printf("%d\n",a[i]);
	       }
        }
      }
     
    for(i=0;i<n;i++)
      { 
      while(r1<r2)
      {

      printf("%d\n",a[i]);
      }
   }
   printf("\n");
}
   
       
