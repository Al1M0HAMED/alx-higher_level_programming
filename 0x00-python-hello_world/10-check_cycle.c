#include "lists.h"
/**
 * check_cycle - this function checks if there is linked list cycle.
 * @list: is the linked list address.
 *
 * Return: 0 if did not found a cylce and 1 if found.
 */
int check_cycle(listint_t *list)
{
	listint_t *t = list, *h = list;

	while (h->next->next)
	{
		t = t->next;
		h = h->next->next;

		if (h == t)
			return (1);
	}
	return (0);
}
