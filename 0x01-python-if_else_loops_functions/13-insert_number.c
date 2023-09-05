#include "lists.h"
/**
 * insert_node - this function inserts a node to a linked list.
 * @number: is the new node n value
 * @head: is the linked list.
 * Return: adress of new node or NULL if failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *h = *head;

	if (h == NULL)
	{
		new_node = malloc(sizeof(listint_t));
		if (!new_node)
			return (NULL);
		new_node->n = number;
		new_node->next = NULL;
		h = new_node;
		return (new_node);
	}
	while (h != NULL)
	{
		if (h->next->n > number || number < 0)
		{
			new_node = malloc(sizeof(listint_t));
			if (!new_node)
				return (NULL);
			new_node->n = number;
			new_node->next = h->next;
			h->next = new_node;
			return (new_node);
		}
		h = h->next;
	}
	return (NULL);
}
