#include "lists.h"
/**
 * check_cycle - function that checks linked lists
 * if the are cycle or not
 * @list: pointer to the linked list
 * Return: 0 if theres no cycle and 1 if theres a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_ptr;
	listint_t *fast_ptr;

	if (list == NULL)
		return (0);
	slow_ptr = list;
	fast_ptr = list;

	while (1)
	{
		if (fast_ptr == NULL)
			return (0);
		fast_ptr = (fast_ptr->next)->next;
		slow_ptr = slow_ptr->next;
		if (fast_ptr == slow_ptr)
			return (1);
	}
	return (0);
}
