#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - Function to check if a linked list is a palindrome
 * @head: pointer to head of linked list
 * Return: 0 if not a palindrome and 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	int i, j, mid, len = 0, status = 1, values[500];
	listint_t *current = *head;

	if (current->next == NULL)
		return (status);
	while (current)
	{
		values[len] = current->n;
		len++;
		current = current->next;
	}
	i = 0, j = len - 1;
	if (len % 2 == 0)
		mid = len / 2;
	else
		mid = (len - 1) / 2;

	while (i < mid)
	{
		if (values[i] != values[j])
		{
			status = 0;
			break;
		}
		i++;
		j--;
	}
	return (status);
}
