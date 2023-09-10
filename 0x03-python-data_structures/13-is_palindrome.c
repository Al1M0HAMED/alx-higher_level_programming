#include "lists.h"
/**
 * is_palindrome - this function detect a linked list palindrome.
 * @head: is the linked list address.
 *
 * Return: 1 on success and 0 of faileir.
 */
int is_palindrome(listint_t **head)
{
	size_t len;
	int idx, arr[2056], i;
	listint_t *current = *head;

	if (!*head || !(*head)->next)
		return (1);

	len = listint_len(*head);
	idx = (len / 2), i = 0;
	while (idx && current)
	{
		arr[i] = current->n;
		current = current->next;
		idx--, i++;
	}
	idx = 0, i--, current = current->next;
	while (i >= 0)
	{
		if (current == NULL || arr[i] != current->n)
			return (0);
		current = current->next, i--;
	}
	return (1);
}
/**
 * listint_len - returns the number of elements in a linked lists
 * @h: linked list of type listint_t to traverse
 *
 * Return: number of nodes
 */
size_t listint_len(const listint_t *h)
{
	size_t num = 0;

	while (h)
	{
		num++;
		h = h->next;
	}

	return (num);
}
