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

	if (list == NULL)
		return (1);
	ptr = list->next;
	while (ptr != NULL && ptr != list)
		ptr = ptr->next;
	if (ptr == list)
		return (1);
	return (0);
}
