#include "lists.h"

/**
 * check_cycle - This function checks if a singly linked list has a cycle
 * @list: pointer to the head of the linked list
 *
 * Return: 0 if there is no cycle or 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slower;
	listint_t *faster;

	if (list == NULL || list->next == NULL)
		return (0);

	slower = list;
	faster = list->next;

	while (faster != NULL && faster->next != NULL)
	{
		if (slower == faster)
			return (1);

		slower = slower->next;
		faster = faster->next->next;
	}

	return (0);
}
