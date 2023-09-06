#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - ....
 *
 * @list: the list
 *
 * Return:0 If there is no cycle.
 *        1 If there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *temp1, *temp2;

	if (list == NULL || list->next == NULL)
		return (0);

	temp1 = list;
	while (temp1)
	{
		temp2 = list->next;

		while (temp2->next)
		{
			if (temp1 == temp2)
				return (1);

			temp2 = temp2->next;
		}
		if (!temp2)
			return (0);
		temp1 = temp1->next;
	}

	return (0);
}
