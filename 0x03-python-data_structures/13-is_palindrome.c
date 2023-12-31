#include "lists.h"

/**
 * is_palindrome - check if linked list is palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 1 if palindrome else 0.
 */

int is_palindrome(listint_t **head)
{
	listint_t *first_list = *head;
	listint_t *sec_list = *head;
	int x = 1, i, j, k;

	if (!*head)
		return (1);
	while (first_list->next)
	{
		first_list = first_list->next;
		x++;
	}
	if (sec_list->n != first_list->n)
		return (0);
	for (i = 0; i < x / 2 - 1; i++)
	{
		first_list = *head;
		sec_list = *head;
		for (j = 0, k = 0; k < x - i - 2; j++, k++)
		{
			if (j < i + 1)
				first_list = first_list->next;
			sec_list = sec_list->next;
		}
		if (sec_list->n != first_list->n)
			return (0);
	}
	return (1);
}
