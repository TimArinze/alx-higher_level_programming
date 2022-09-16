#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - function that inserts a number
 * into a sorted singly linked list
 * @head: head
 * @number: data
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *curr;

	curr = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	if (*head == NULL)
	{
		new->n = number;
		new->next = NULL;
		*head = new;
		return (*head);
	}

	while (curr->next != NULL && curr->next->n < number)
		curr = curr->next;

	new->n = number;
	if (curr->next == NULL)
	{
		new->next = NULL;
		curr->next = new;
	}
	else
	{
		new->next = curr->next;
		curr->next = new;
	}
	return (new);
}
