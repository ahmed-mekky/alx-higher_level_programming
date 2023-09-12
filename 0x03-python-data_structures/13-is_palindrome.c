#include "lists.h"

/**
 * is_palindrome - check if linked list is palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 1 if palindrome else 0.
 */

int is_palindrome(listint_t **head)
{
	listint_t *list = *head;
	int x = 1, i, array[BUFSIZE];

	if (!list)
		return (1);
	array[0] = list->n;
	while (list->next)
	{
		list = list->next;
		array[x++] = list->n;
	}
	for (i = 0; i < x / 2 - 1; i++)
	{
		if (array[i] == array[x - i])
			return (0);
	}
	
	return (1);
}
