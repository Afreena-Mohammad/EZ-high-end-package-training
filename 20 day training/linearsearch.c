//linear search
#include<stdio.h>
main()
{
	int a[100],i,size,se,flag=0;
	printf("\nEnter size of the array");
	scanf("%d",&size);
	printf("enter array elements");
	for(i=0;i<size;i++)
	{
		scanf("%d",&a[i]);
	}
	printf("\nenter the search element");
	scanf("%d",&se);
	for(i=0;i<size;i++)
	{
		if(se==a[i])
		{
			printf("element found at %d",i);
			flag=1;
			break;
	    }
	}
	if(flag==0)
	{
		printf("element not found");
	}
}
