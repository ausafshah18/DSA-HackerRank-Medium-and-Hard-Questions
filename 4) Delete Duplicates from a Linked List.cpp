/* Delete duplicate-value nodes from a sorted linked list */
SinglyLinkedListNode* removeDuplicates(SinglyLinkedListNode* llist) 
{
    SinglyLinkedListNode *temp1 = llist;
    while(temp1 != NULL && temp1 -> next != NULL)
    {
        if(temp1 -> data == temp1 -> next -> data)
        {
            SinglyLinkedListNode * curr = temp1 -> next;
            temp1 -> next = temp1 -> next -> next;
            delete(curr);
        }
        else
        {
            temp1 = temp1 -> next;
        }
    }
   return llist;
}