class Node:
    def __init__(self, val):
        self.data = val
        self.next = None 

def firstDeletion(head):
    temp = head
    head = head.next

    del temp

    return head 

def print_list(head):
    while head:
        print(head.data, end = " -> ")
        head = head.next
    
    print("None")


if __name__ == "__main__":
    head = Node(99)
    head.next = Node(98)
    head.next.next = Node(97)


    print("Original List")
    print_list(head)

    print("Modified List after deletion")
    print_list(firstDeletion(head))


