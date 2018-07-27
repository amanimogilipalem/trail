//palendrome program

#include<stdio.h>
#include<string.h>
void main()
{
	char *p="veccev";
	int i,j;
	for(i=0,j=strlen(p)-1;p[i];i++,j--)
	{
		if(p[i]!=p[j])
		{
			printf("not plendrome\n");
			break;
		}
	}
	printf("palendrome\n");
}
