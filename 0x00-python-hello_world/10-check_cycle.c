#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

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
