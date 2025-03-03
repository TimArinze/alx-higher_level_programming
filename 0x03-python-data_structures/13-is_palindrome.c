#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * is_palindrome - function that checks if a singly linked list is a palindrome
 * @head: Pointer to the head pointer
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *reversed, *curr;

	if (*head == NULL || (*head)->next ==NULL)
		return (1);

	curr = *head;
	reversed = reverselistcopy(curr);
	if (!reversed)
		return (0);
	while (reversed != NULL)
	{
		if (curr->n != reversed->n)
		{
			return (0);
		}
		curr = curr->next;
		reversed = reversed->next;
	}
	return (1);
}

/**
 * reverselist - A function that reverses a singly linked list
 * @head: Pointer to head pointer
 * Return: Pointer to the reversed list
 */
listint_t *reverselistcopy(listint_t *head)
{
	listint_t *curr, *prev = NULL, *new_node;

	if ((head) == NULL)
		return (NULL);

	curr = head;
	new_node = NULL;
	while (curr != NULL)
	{
		new_node = malloc(sizeof(listint_t));
		if (new_node == NULL)
		{
			while (prev != NULL)
			{
				listint_t *temp = prev;
				prev = prev->next;
				free(temp);
			}
			return (NULL);
		}
		new_node->n = curr->n;
		new_node->next = prev;
		prev = new_node;
		curr = curr->next;
	}
	return (prev);
}
