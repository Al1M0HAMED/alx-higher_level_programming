#include "lists.h"
/**
 * insert_node - this function inserts a node to a linked list.
 * @number: is the new node n value
 * @head: is the linked list.
 * Return: adress of new node or NULL if failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	int i = 0, n[50];
	listint_t *new_node, *h = *head;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;

	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	for (; h->next != NULL; i++)
		h = h->next,  n[i] = h->n;
	for (i = i - 1, h = *head; n[i] > number;)
		i--;

	while (h != NULL)
	{
		if (h->n == n[i])
		{
			new_node->next = h->next;
			h->next = new_node;
			return (new_node);
		}
		h = h->next;
	}
	return (NULL);
}
