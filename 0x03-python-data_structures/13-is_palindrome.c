#include "lists.h"
/**
 * is_palindrome - this function detect a linked list palindrome.
 * @head: is the linked list address.
 *
 * Return: 1 on success and 0 of faileir.
 */
int is_palindrome(listint_t **head)
{
	listint_t *mid = *head, *first = *head, *last;
	size_t idx, len;

	if (!*head || !(*head)->next)
		return (1);

	len = listint_len(*head);
	if (len % 2)
		idx = (len / 2) + 1;
	else
		idx = (len / 2);

	while (idx > 0)
		mid = mid->next, idx--;

	last = reverse_listint(&mid);
	mid = last;

	while (first && last)
	{
		if (last->n != first->n)
		{
			reverse_listint(&mid);
			return (0);
		}
		first = first->next;
		last = last->next;
	}
	reverse_listint(&mid);
	return (1);
}
/**
 * reverse_listint - this function reverse a linked list.
 * @head: is the linked list address.
 * Return: the address of first node of the reversed linked list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *next, *previos;

	next = NULL, previos = NULL;
	while (*head)
	{
		next = (*head)->next;
		(*head)->next = previos;
		previos = *head;
		*head = next;
	}
	*head = previos;
	return (*head);
}
/**
 * listint_len - this function returns the number of elements in a linked.
 * @h: is the address of a linked list.
 * Return: the len of a linked list.
 */
size_t listint_len(const listint_t *h)
{
	size_t len = 0;

	while (h != NULL)
		len++, h = h->next;
	return (len);
}
