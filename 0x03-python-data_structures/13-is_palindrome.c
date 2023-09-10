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
	int idx;
	listint_t *first = *head, *seccond, *current = *head;

	if (!*head || !(*head)->next)
		return (1);
	len = listint_len(*head);
	if (len % 2 == 0)
		idx = (len / 2);
	else
		idx = ((len / 2) + 1);

	while (idx && current)
	{
		current = current->next;
		idx--;
	}
	seccond = current;
	while (seccond)
	{
		if (first->n != seccond->n)
			return (1);
		first = first->next;
		seccond = seccond->next;
	}
	return (0);
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
