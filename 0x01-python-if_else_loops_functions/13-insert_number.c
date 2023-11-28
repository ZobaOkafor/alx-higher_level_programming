#include "lists.h"


/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: pointer to pointer of the fisrts node
 * @number: inumber to be included
 *
 * Return: address of the new element or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *cur, *prev;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	cur = *head;
	prev = NULL;

	while (cur != NULL && cur->n < number)
	{
		prev = cur;
		cur = cur->next;
	}

	new->next = cur;
	prev->next = new;

	return (new);
}
