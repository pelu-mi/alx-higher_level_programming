#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - function to insert a node into a sorted linked list
 * @head: pointer to head of linked list
 * @number: value of new node
 * Return: Pointer to new linked list or null
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	while (current)
	{
		if (number >= current->n && number <= (*current).next->n)
			break;
		current = current->next;
	}

	new->n = number;
	new->next = current->next;
	current->next = new;

	return (new);
}
