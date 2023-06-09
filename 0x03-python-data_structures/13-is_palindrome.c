#include "lists.h"

/**
 * is_palindrome - a function that finds if the singly linked list is alindrome or not.
 * @head: the head of the list.
 * Return: 1 if it is palindrome and 0 if not.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast;

	slow = malloc(sizeof(
