#include "lists.h"
/**
 * insert_node - inserts a number in a sorted singly linked list
 * @head: pointer to the start
 * @number: variable number
 * Return: pointer
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nd = *head, *nw;

	nw = malloc(sizeof(listint_t));
	if (nw == NULL)
		return (NULL);
	nw->n = number;
	if (nd == NULL || nd->n >= number)
	{
		nw->next = nd;
		*head = nw;
		return (nw);
	}
	while (nd && nd->next && nd->next->n < number)
		nd = nd->next;
	nw->next = nd->next;
	nd->next = nw;
	return (nw);
}
