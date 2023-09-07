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

	if (!list)
		return (0);
	temp1 = list;

	while (temp1)
	{
		if (temp1->next == temp1)
			return (1);
		temp2 = list;
		while (temp2 != temp1)
		{
			if (temp1->next == temp2)
			{
				return (1);
			}
			temp2 = temp2->next;
		}
		temp1 = temp1->next;
	}
	return (0);
}
