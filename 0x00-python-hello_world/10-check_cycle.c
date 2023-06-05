#include "lists.h"
/**
 * check_cycle - checks singly linked is a cycle
 * @list: list to be checked
 * Return: 1 if is, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *x = list, *y = list;

	if (!list)
		return (0);
	do {
		if (x->next != NULL && x->next->next !=NULL)
		{
			x = x->next->next;
			y = y->next;
			if (x == y)
				return (1);
		}
		else
			return (0);
	} while (1);
}
