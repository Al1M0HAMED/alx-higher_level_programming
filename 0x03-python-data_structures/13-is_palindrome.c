#include "lists.h"
/**
 * is_palindrome - this function detect a linked list palindrome.
 * @head: is the linked list address.
 *
 * Return: 1 on success and 0 of faileir.
 */
int is_palindrome(listint_t **head)
{
	listint_t *left, *right;
	size_t mid_index, len;
	int j, i;

	if (!*head || !(*head)->next)
		return (1);
	
	len = listint_len(*head);

	if (len % 2 == 0)
		mid_index = len / 2, j = 1;
	else
		mid_index = len / 2 + 1, j = 2;
	if (len <= 1)
		return (1);

	left = *head;
	i = mid_index;
	while(i)
	{
		left = left->next;
		i--;
	}
	while (left)
	{
		right = *head;
		i = mid_index - j;
		while(i)
		{
			right = right->next;
			i--;
		}
		if (left->n != right->n)
			return (-1);
		left = left->next;
		j++;
	}

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
