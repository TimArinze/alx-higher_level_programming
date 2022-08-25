#include "lists.h"
/**
 * check_cycle - function that checks linked lists
 * if the are cycle or not
 * @list: pointer to the linked list
 * Return: 0 if theres no cycle and 1 if theres a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr;

	ptr = malloc(sizeof(listint_t));
	if (list == NULL)
		return (-1);
	ptr = list->next;
	while (ptr != NULL && ptr != list)
		ptr = ptr->next;

	if (ptr == list)
	{
		free(ptr);
		return (1);
	}
	else
	{
		free(ptr);
		return (0);
	}
}
