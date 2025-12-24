#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
    int val;
    struct Node *next;
} Node;

void traverse_nodes(Node *node){
    while (1){
        printf("Current node value: %d \n",node->val);

        if (node->next == NULL) break;
        node = node->next;
    }
}

Node* insert_value(Node *head, int idx, int val){ // Returns Head of the node after insertion
 
    Node *cur = head;

    for (int i=0; i<idx-2; i++){
        if (cur->next == NULL){
            printf("IDX out of range \n");
            return head;
        }
        cur = cur->next;
    }

    Node *new_node = (Node*)malloc(sizeof(Node));

    new_node->val = val;

    if (idx == 0){
        new_node->next = cur; // cur was the old head
        return new_node;
    }

    new_node->next = cur->next;
    cur->next = new_node;
    return head;
}

Node* delete_idx(Node *head, int idx){ // Returns Head of the node after deletion
    Node *cur = head;

    if (idx == 0){
        cur = cur->next;
        free(head);
        return cur;
    }

    Node *prev;

    for (int i=0; i<idx; i++){
        prev = cur;
        cur = cur->next;
        if (cur->next == NULL){
            printf("IDX out of range");
            return NULL;
        }
    }

    prev->next = cur->next;
    free(cur);
    return head;
}

int main () {
    Node *head = (Node*) malloc(sizeof(Node));
    head->val = 0;
    head->next = NULL;

    Node *tmp = head;

    for (size_t i = 1; i < 10; i++){
        Node *cur = (Node*) malloc(sizeof(Node));
        cur->val = i;
        cur->next = NULL;

        tmp->next = cur;
        tmp = cur;
    }

    traverse_nodes(head);
    printf("\n");
    
    head = insert_value(head, 100, 100);
    traverse_nodes(head);
    printf("\n");

    head = delete_idx(head, 0);
    traverse_nodes(head);
    printf("\n");

    return 0;
}