#include<stdio.h>

#define MAXSIZE 10

typedef struct Stack
{
	int entry[MAXSIZE];
	int top;	
}stack;

void init(stack *sptr)
{
	sptr->top=0;
}
int isfull(stack *sptr)
{
	if(sptr->top==MAXSIZE)
		return 1;
	else
		return 0;
}

void push(stack *sptr)
{
	int item;
	
	if(isfull(sptr))
		printf("Stack is fulll......\n");
	else
	{
		printf("Enter any item:");
		scanf("%d",&item);
		
		sptr->entry[sptr->top]=item;
		sptr->top++;//sptr->top+=1;
		
	}
	
}
int isempty(stack * sptr)
{
	if(sptr->top==0)
	     return 1;
	else
	    return 0;
}

void pop(stack *sptr)
{
	int item;
	if(isempty(sptr))
		printf("Stack is Empty......\n");
	else
	{
		sptr->top--;
		item=sptr->entry[sptr->top];
		printf("%d item is deleted from stack.....\n",item);
	}
	
}
void peep(stack * sptr)
{
	int i;
	if(isempty(sptr))
		printf("Stack is Empty......\n");
	else
	{
	
	
		for(i=sptr->top-1;i>=0;i--)
		{	
			printf("Value=%d\n",sptr->entry[i]);
		}
    }
}
void main()
{
	
	stack s;
	init(&s);
	int ch;	
	do
	{
	
	printf("Your choice are:\n");
	printf("1 for push:\n2 for pop:\n3 for display:\n4 for Exit:\n");
	printf("Enter any choice:");
	scanf("%d",&ch);
	
	switch(ch)
	{
		case 1:
				push(&s);
				break;
		case 2:
				pop(&s);
				break;
		case 3:
				peep(&s);
				break;
	}
  }while(ch!=4);
}