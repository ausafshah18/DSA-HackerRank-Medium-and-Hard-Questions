/* Merge two sorted linked lists */
SinglyLinkedListNode* mergeLists(SinglyLinkedListNode* head1, SinglyLinkedListNode* head2) 
{
    vector<int> v;
    SinglyLinkedListNode *temp1 = head1;
    SinglyLinkedListNode *temp2 = head2;
    while(temp1 != NULL)
    {
        v.push_back(temp1 -> data);
        temp1 = temp1 -> next;
    }
    while(temp2 != NULL)
    {
        v.push_back(temp2 -> data);
        temp2 = temp2 -> next;
    }
    sort(v.begin(),v.end());
    SinglyLinkedListNode *head = new SinglyLinkedListNode(v[0]);
    SinglyLinkedListNode *temp = head;
    int n = v.size();
    for(int i = 1;i < n;i++)
    {
        head -> next = new SinglyLinkedListNode(v[i]);
        head = head -> next;
    }
    return temp; 
}