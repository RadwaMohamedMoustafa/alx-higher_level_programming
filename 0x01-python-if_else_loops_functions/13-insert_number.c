#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: The head of the linked list.
 * @number: The number to insert.
 * Return: 0 If the function fails or pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nod = *head, *n;

	n = malloc(sizeof(listint_t));
	if (n == NULL)
		return (NULL);
	n->n = number;

	if (!nod || nod->n >= number)
	{
		n->next = nod;
		*head = n;
		return (n);
	}

	while (nod && nod->next && nod->next->n < number)
		nod = nod->next;

	n->next = nod->next;
	nod->next = n;

	return (n);
}
