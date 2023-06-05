#include "lists.h"

/**
 * check_cycle - check if a singly linked list has a cycle in it.
 * @list: head of the singly linked list.
 *
 * Return: 0 if there is no cycle and 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *p, *q;

	if (list == NULL || list->next == NULL)
		return (0);

	p = list->next;
	q = list->next->next;

	while (p != NULL && q != NULL && q->next != NULL)
	{
		if (p == q)
		{
			return (1);
		}
	p = p->next;
	q = q->next->next;
	}

	return (0);
}
