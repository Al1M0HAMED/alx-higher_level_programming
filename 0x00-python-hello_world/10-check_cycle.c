#include "lists.h"
/**
 * check_cycle - this function checks if there is a cycle in a linked list.
 * @list: is the head of the linked list.
 * Return: 1 if found an cycle 0 if did not.
 */
int check_cycle(listint_t *head)
{
	listint_t *sonic = head;
	listint_t *super_sonic = head;

	if (list == NULL)
		return (0);
	while (sonic && super_sonic && super_sonic->next)
	{
		sonic = sonic->next;
		super_sonic = super_sonic->next->next;
		if (super_sonic == sonic)
			return (1);
	}
	return (0);
}
