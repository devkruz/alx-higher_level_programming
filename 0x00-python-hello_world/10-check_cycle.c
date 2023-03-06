#include "lists.h"

int check_cycle(listint_t *list)
{
    listint_t *current = list;

    if (current == NULL)
        return (0);

    while (current->next != NULL)
    {
        if (current->next == list)
            return (1);

        current = current->next;
    }

    return (0);

}
