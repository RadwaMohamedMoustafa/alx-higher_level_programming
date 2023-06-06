#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * insert_node - insert node ascending order with value number
 * @head: head pointer
 * @number: value
 * Return: address of inserted node
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *cur, *n;

	n = malloc(sizeof(listint_t));

	if (n == NULL)
		return (NULL);

	n->n = number;
	n->next = NULL;
	cur = *head;
	while (cur && cur->next && cur->next->n <= number)
	{
		cur = cur->next;
	}
	if (cur == NULL)
	{
		*head = n;
	}
	else if (cur->n > number)
	{
		n->next = cur;
		*head = n;
	}
	else
	{
		n->next = cur->next;
		cur->next = n;
	}
	return (n);
}
