def list_summa(list1, list2):
    list3 = LinkedList()
    if list1.len() == list2.len():
        N1 = list1.head
        N2 = list2.head
        while N1 is not None:
            list3.add_in_tail(Node(N1.value + N2.value))
            N1 = N1.next
            N2 = N2.next
    return list3
