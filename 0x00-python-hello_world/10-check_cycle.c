#include "lists.h"
/**
 * check_cycle - this function checks if there is a cycle in a linked list.
 * @list: is the head of the linked list.
 * Return: 1 if found an cycle 0 if did not.
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *tmp;

	tmp = list;
	while(tmp != NULL)
	{	
		current = tmp->next;
		while (current != NULL)
		{
			if (current == tmp)
				return (1);
			current = current->next;
		}
		tmp = tmp->next;
	}
	return (0);
}
