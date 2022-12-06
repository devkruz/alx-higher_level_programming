#include "lists.h"
/**
 * is_palindrome - check if a linked list
 * is a palindrome
 * @head: the head of the list
 *
 * return: 1 if the list is a palindrom else 0
*/

int is_palindrome(listint_t **head)
{
	listint_t *reversed_list;
	listint_t *current;
	listint_t *reversed_tmp;

	reversed_list = NULL;
	current = *head;

	if (current == NULL)
		return (1);

	while (current->next != NULL)
	{
		add_nodeint(&reversed_list, current->n);
		current = current->next;
	}
	add_nodeint(&reversed_list, current->n);

	current = *head;
	reversed_tmp = reversed_list;

	if (reversed_list != NULL)
	{
		while (current->next != NULL
		&& reversed_list->next != NULL)
		{
			if (current->n != reversed_list->n)
				return (0);
			current = current->next;
			reversed_list = reversed_list->next;
		}

	}

	free_listint(reversed_tmp);

	return (1);
}

/**
 * add_nodeint - add new node to the beginning
 * of a list
 * @head: the list head
 * @n: the new node element
 *
 * return: nothing
*/

void add_nodeint(listint_t **head, const int n)
{
	listint_t *new_node;
	listint_t *node_head;

	node_head = *head;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return;

	new_node->n = n;
	new_node->next = NULL;

	if (*head == NULL)
		*head = new_node;
	else
	{
		new_node->next = node_head;
		*head = new_node;
	}
}
