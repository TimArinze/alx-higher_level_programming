#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - function that checks if a singly linked list is a palindrome
 * @head: Pointer to the head pointer
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *reversed;

	if (*head == NULL)
		return (1);

	reversed = malloc(sizeof(listint_t));
	reversed = reverselist(head);
	while (*head != NULL)
	{
		if ((*head)->n != reversed->n)
			return (0);
		*head = (*head)->next;
		reversed = reversed->next;
	}
	return (1);
}

/**
 * reverselist - A function that reverses a singly linked list
 * @head: Pointer to head pointer
 * Return: Pointer to the reversed list
 */
listint_t *reverselist(listint_t **head)
{
	listint_t *curr, *prev;

	if ((*head) == NULL)
		return (NULL);

	prev = *head;
	*head = (*head)->next;
	curr = *head;
	prev->next = NULL;
	while (*head != NULL)
	{
		*head = (*head)->next;
		curr->next = prev;
		prev = curr;
		curr = *head;
	}
	*head = prev;
	return (*head);
}
