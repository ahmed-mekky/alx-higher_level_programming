#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
#include <time.h>

/**
 * main - check the code for
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;

	clock_t begin = clock();
    head = NULL;
    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 1);
    print_listint(head);

    if (is_palindrome(&head) == 1)
        printf("Linked list is a palindrome\n");
    else
        printf("Linked list is not a palindrome\n");

    free_listint(head);
	clock_t end = clock();
	double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
	printf("Time taken by function %f\n", time_spent);

    return (0);
}
