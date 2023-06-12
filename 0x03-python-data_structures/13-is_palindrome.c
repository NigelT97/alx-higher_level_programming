#include "lists.h"
/**
 * rvesrse_list - reverse link
 * @head: pointer to node first
 * Return: pointer
 */
void rvesrse_list(listint_t **head)
{
	listint_t *p = NULL, *n = NULL, *c = NULL;

	while (c)
	{
		n = c->next;
		c->next = p;
		p = c;
		c = n;
	}
	*head = p;
}
/**
 * is_palindrome - checks palindrome
 * @head: pointer
 * Return: 1 if pali, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *s = *head, *fast = *head, *tmp = *head, *dp = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dp = s->next;
			break;
		}
		if (!fast->next)
		{
			dp = s->next->next;
			break;
		}
		s = s->next;
	}
	rvesrse_list(&dp);
	while (dp && tmp)
	{
		if (tmp->n == dp->n)
		{
			dp = dp->next;
			tmp = tmp->next;
		}
		else
			return (0);
	}
	if (!dp)
		return (1);
	return (0);
}
