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

	new->n = number;
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	if ((*head)->n > number)
	{
		new->next = curr;
		curr = new;
		return (new);
	}
	while (curr->next != NULL && curr->next->n < number)
		curr = curr->next;

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
