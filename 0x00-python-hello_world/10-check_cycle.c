#include "lists.h"

int check_cycle(listint_t *list)
{
    listint_t *current = list, *prev = list;

    if (current == NULL)
        return (0);

    while (current && prev && current->next != NULL)
    {
        prev = prev->next;
        current = current->next->next;

        if (current == prev)
            return (1);
    }

    return (0);

}
