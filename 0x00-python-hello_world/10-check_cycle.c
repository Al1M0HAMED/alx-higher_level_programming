#include "lists.h"
/**
 * check_cycle - this function checks if there is a cycle in a linked list.
 * @list: is the head of the linked list.
 * Return: 1 if found an cycle 0 if did not.
 */
int check_cycle(listint_t *list)
{
	int i = 0;
	listint_t *tmp, *head;

	tmp = list, head = list;
	while (tmp->next != NULL)
	{
		if (i)
		{
			if (tmp == head || tmp->next == head)
				return (1);
		}
		tmp = tmp->next;
		i++;
	}
	return (0);
}
