#include "lists.h"

/**
 * insert_node - add a node in sorted list
 *
 * @head: ....
 * @number: .....
 *
 * Return: NULL or address of the new node
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *old_node = *head;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;

	if (!old_node || number < old_node->n)
	{
		new_node->next = old_node;
		old_node = new_node;
		return (new_node);
	}

	while (old_node && old_node->next && old_node->next->n < number)
		old_node = old_node->next;
	new_node->next = old_node->next;
	old_node->next = new_node;

	return (new_node);
}
