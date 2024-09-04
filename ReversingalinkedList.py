class Node:
    def __init__(self, value):
        self.data = value
        self.next = None 

def reverse(head):
    prev, curr = None, head 
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev 

def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


if __name__ == "__main__":

    # Creating a linked list
    # 1 -> 2 -> 3 -> 4 -> 5 -> None
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Original list: ")
    print_list(head)
    # reversing the linked list 
    head = reverse(head)
    print("List after reversing it: ")
    print_list(head)   
