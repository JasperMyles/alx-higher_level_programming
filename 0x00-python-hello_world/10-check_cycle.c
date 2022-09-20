#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - Checks if a singly-linked list contains a cycle in it
 * @list: A linked list.
 * Return: If there is no cycle 0.If there is a cycle 1
 */
int check_cycle(listint_t *list)
{
  listint_t *first, *second;

  if (list == NULL || list->next == NULL)
    return (0);

  first = list->next;
  second = list->next->next;

  while (first && second && second->next)
    {
      if (first == second)
	return (1);

      first = first->next;
      second = second->next->next;

    }
  return (0);
}
