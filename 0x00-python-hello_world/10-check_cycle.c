#include "lists.h"
/**
 * check_cycle - this function checks if there is linked list cycle.
 * @list: is the linked list address.
 *
 * Return: 0 if did not found a cylce and 1 if found.
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle, *hare;

	if (list == NULL || list->next == NULL)
		return (0);

	hare = list->next->next;
       	turtle = list->next;

	while (hare->next && turtle && hare)
	{	
		if (h == t)
			return (1);
		turtle = turtle->next;
                hare = hare->next->next;
	}
	return (0);
}
