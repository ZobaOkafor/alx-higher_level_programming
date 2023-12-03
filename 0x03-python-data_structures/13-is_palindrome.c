#include "lists.h"

/**
 * is_palindrome - This function checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the linked list
 *
 * Return: 1 if the list is a palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *slower = *head;
	listint_t *faster = *head;
	listint_t *prev = NULL;
	listint_t *tmp;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (faster != NULL && faster->next != NULL)
	{
		faster = faster->next->next;
		tmp = slower->next;
		slower->next = prev;
		prev = slower;
		slower = tmp;
	}

	if (faster != NULL)
		slower = slower->next;

	while (slower != NULL)
	{
		if (slower->n != prev->n)
			return (0);

		slower = slower->next;
		prev = prev->next;
	}

	return (1);
}
