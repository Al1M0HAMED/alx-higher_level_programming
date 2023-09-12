#include "lists.h"
/**
 * check_cycle - this function checks if there is linked list cycle.
 * @list: is the linked list address.
 *
 * Return: 0 if did not found a cylce and 1 if found.
 */
int check_cycle(listint_t *list)
{
	listint_t *t, *h;

	if (list == NULL || list->next == NULL)
		return (0);

	h = list->next->next;
       	t = list->next;

	while (h->next && t && h)
	{	
		if (h == t)
			return (1);
		t = t->next;
                h = h->next->next;
	}
	return (0);
}
