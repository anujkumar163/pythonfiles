#include<stdio.h>

#define MAXSIZE 10

typedef struct Queue
{
	int entry[MAXSIZE];
	int f,r;	
}Queue;

void init(Queue *qptr)
{
	qptr->f=0;
	qptr->r=0;
}
int isfull(Queue *qptr)
{
	if(qptr->r==MAXSIZE)
		return 1;
	else
		return 0;
}

void insert(Queue *qptr)
{
	int item;
	
	if(isfull(qptr))
		printf("Queue is fulll......\n");
	else
	{
		printf("Enter any item:");
		scanf("%d",&item);
		
		qptr->entry[qptr->r]=item;
		qptr->r++;
		
	}
	
}
int isempty(Queue * qptr)
{
	if(qptr->f==qptr->r)
	     return 1;
    return 0;
}

void delete(Queue *qptr)
{
	int item;
	if(isempty(qptr))
		printf("Queue is Empty......\n");
	else
	{
		item=qptr->entry[qptr->f];
		printf("%d  is deleted from the Queue .....\n",item);
		qptr->f++;
	}
	
}
void display(Queue * qptr)
{
	int i;
	if(isempty(qptr))
		printf("Queue is Empty......\n");
	else
	{
	
	
		for(i=qptr->f;i<qptr->r;i++)
		{	
			printf("Value=%d\n",qptr->entry[i]);
		}
    }
}
void main()
{
	
	Queue s;
	init(&s);
	int ch;	
	do
	{
	
	printf("Your choice are:\n");
	printf("1 for Insert:\n2 for Delete:\n3 for display:\n4 for Exit:\n");
	printf("Enter any choice:");
	scanf("%d",&ch);
	
	switch(ch)
	{
		case 1:
				insert(&s);
				break;
		case 2:
				delete(&s);
				break;
		case 3:
				display(&s);
				break;
	}
  }while(ch!=4);
}

