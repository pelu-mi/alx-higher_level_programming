#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - function to check for cycles in a linked list
 * @list: list to check for cycle
 * Return: 1 if cycle, 0 if not
 */

int check_cycle(listint_t *list)
{
	while (list)
	{
		if (list->n == -1000)
			return (1);
		list->n = -1000;
		list = list->next;
	}
	return (0);
}
