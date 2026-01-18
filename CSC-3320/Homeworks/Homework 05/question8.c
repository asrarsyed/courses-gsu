/*
  Program: Linked List
*/

#include <stdio.h>
#include <stdlib.h>

// Definition of the node structure
struct node {
    int value;
    struct node *next;
};

// Function to find the last occurrence of n in the linked list
struct node *find_last(struct node *list, int n) {
    struct node *last_found = NULL;
    while (list != NULL) {
        if (list->value == n) {
            last_found = list;
        }
        list = list->next;
    }
    return last_found;
}

// Helper function to create a new node
struct node *create_node(int value) {
    struct node *new_node = (struct node *)malloc(sizeof(struct node));
    if (new_node == NULL) {
        printf("Memory allocation failed.\n");
        exit(1);
    }
    new_node->value = value;
    new_node->next = NULL;
    return new_node;
}

// Helper function to append a node to the linked list
void append_node(struct node **head, int value) {
    struct node *new_node = create_node(value);
    if (*head == NULL) {
        *head = new_node;
        return;
    }
    struct node *current = *head;
    while (current->next != NULL) {
        current = current->next;
    }
    current->next = new_node;
}

// Helper function to print the linked list
void print_list(struct node *head) {
    while (head != NULL) {
        printf("%d -> ", head->value);
        head = head->next;
    }
    printf("NULL\n");
}

// Helper function to free the linked list
void free_list(struct node *head) {
    struct node *temp;
    while (head != NULL) {
        temp = head;
        head = head->next;
        free(temp);
    }
}

// Main function to test find_last
int main() {
    struct node *head = NULL;

    // Creating the linked list
    append_node(&head, 3);
    append_node(&head, 5);
    append_node(&head, 7);
    append_node(&head, 5);
    append_node(&head, 9);

    printf("Linked list: ");
    print_list(head);

    int target = 5;
    struct node *result = find_last(head, target);

    if (result != NULL) {
        printf("Last occurrence of %d found at node with value: %d\n", target, result->value);
    } else {
        printf("%d not found in the list.\n", target);
    }

    // Free the allocated memory
    free_list(head);
    return 0;
}
