import random

def test_1():
    print()
    print('Test find all 5')
    list1 = [5, 8, 35, 2, 31, 5, 17, 10, 2, 5, 5]
    s1_list = LinkedList()
    for i in list1:
        n = Node(i)
        s1_list.add_in_tail(n)
    s1_list.print_all_nodes()
    print()
    print()
    C = s1_list.find_all(5) 
    if len(C) == 0: print('None')
    for i in C:
        if i.next != None and i.value != None:
            print(i.value, 'next -',  i.next.value, end=' ')
            print()
        elif i.value != None:
            print(i.value, 'next -', i.next, end=' ')
            print()
    print()
    print('Test find all 6')
    list1 = [5, 8, 35, 2, 31, 5, 17, 10, 2, 5, 5]
    s2_list = LinkedList()
    for i in list1:
        n = Node(i)
        s2_list.add_in_tail(n)
    s2_list.print_all_nodes()
    print()
    print()
    C = s2_list.find_all(6) 
    if len(C) == 0: print('None')
    for i in C:
        if i.next != None and i.value != None:
            print(i.value, 'next -',  i.next.value, end=' ')
            print()
        elif i.value != None:
            print(i.value, 'next -', i.next, end=' ')
            print()    
    
def test_2():
    print()
    print('Test delete 5 False')
    list1 = [5, 8, 35, 2, 31, 5, 17, 10, 2, 5]
    s1_list = LinkedList()
    for i in list1:
        n = Node(i)
        s1_list.add_in_tail(n)
    s1_list.print_all_nodes()
    print()
    s1_list.delete(5, False)
    s1_list.print_all_nodes()
    print()
    if s1_list.head != None and s1_list.tail != None:
        print('Начало списка ', s1_list.head.value , 'next - ', s1_list.head.next.value)
        print('Конец списка ', s1_list.tail.value, 'next - ', s1_list.tail.next)
    elif s1_list.head != None:
        print('Начало списка ', s1_list.head.value , 'next - ', s1_list.head.next)
        print('Конец списка ', s1_list.tail.value, 'next - ', s1_list.tail.next)
    else:
        print('Начало списка ', s1_list.head)
        print('Конец списка ', s1_list.tail)        

    print()
    print('Test delete 5 True')
    list1 = [5, 8, 35, 2, 31, 5, 17, 5, 5, 5]
    s1_list = LinkedList()
    for i in list1:
        n = Node(i)
        s1_list.add_in_tail(n)
    s1_list.print_all_nodes()
    print()
    s1_list.delete(5, True)
    s1_list.print_all_nodes()
    print()
    if s1_list.head != None and s1_list.tail != None:
        print('Начало списка ', s1_list.head.value , 'next - ', s1_list.head.next.value)
        print('Конец списка ', s1_list.tail.value, 'next - ', s1_list.tail.next)
    elif s1_list.head != None:
        print('Начало списка ', s1_list.head.value , 'next - ', s1_list.head.next)
        print('Конец списка ', s1_list.tail.value, 'next - ', s1_list.tail.next)
    else:
        print('Начало списка ', s1_list.head)
        print('Конец списка ', s1_list.tail)        
    
    print()
    print('Test delete 5 alone unit')
    list1 = [5]
    s1_list = LinkedList()
    for i in list1:
        n = Node(i)
        s1_list.add_in_tail(n)
    s1_list.print_all_nodes()
    print()
    s1_list.delete(5, True)
    s1_list.print_all_nodes()
    if s1_list.head != None and s1_list.tail != s1_list.head:
        print('Начало списка ', s1_list.head.value , 'next - ', s1_list.head.next.value)
        print('Конец списка ', s1_list.tail.value, 'next - ', s1_list.tail.next)
    elif s1_list.head != None:
        print('Начало списка ', s1_list.head.value , 'next - ', s1_list.head.next)
        print('Конец списка ', s1_list.tail.value, 'next - ', s1_list.tail.next)
    else:
        print('Начало списка ', s1_list.head)
        print('Конец списка ', s1_list.tail)        
    
    print()
    print('Test delete 5 empty list')
    list1 = []
    s1_list = LinkedList()
    for i in list1:
        n = Node(i)
        s1_list.add_in_tail(n)
    s1_list.print_all_nodes()
    print()
    s1_list.delete(5, True)
    s1_list.print_all_nodes()
    if s1_list.head != None and s1_list.tail != s1_list.head:
        print('Начало списка ', s1_list.head.value , 'next - ', s1_list.head.next.value)
        print('Конец списка ', s1_list.tail.value, 'next - ', s1_list.tail.next)
    elif s1_list.head != None:
        print('Начало списка ', s1_list.head.value , 'next - ', s1_list.head.next)
        print('Конец списка ', s1_list.tail.value, 'next - ', s1_list.tail.next)
    else:
        print('Начало списка ', s1_list.head)
        print('Конец списка ', s1_list.tail)        

def test_3():
    print()
    print('Test clean')
    Ans = True
    for i in range(1000):
        N = random.randint(0, 15)
        s1_list = LinkedList()
        for i in range(N):
            n = Node(random.randint(1, 9))
            s1_list.add_in_tail(n)
        s1_list.clean()
        Ans = Ans and (s1_list.head == None and s1_list.tail == None)
    if Ans:
        print('OK')
    else:
        print('FAIL')
        
def test_4():
    print()
    print('Test len')
    Ans = True
    for i in range(1000):
        N = random.randint(0, 20)
        s_list = LinkedList()
        for i in range(N):
            n = Node(random.randint(1, 9))
            s_list.add_in_tail(n)
        Ans = Ans and N == s_list.len()
    if Ans:
        print('OK')
    else:
        print('FAIL')

def test_5():
    print()
    print('Test insert')
    list1 = [5, 8, 35, 2, 31, 5, 17, 5, 5]
    s1_list = LinkedList()
    s2_list = LinkedList()
    for i in list1:
        n = Node(i)
        s1_list.add_in_tail(n)
        s2_list.add_in_tail(n)
    print()
    print('inserting 666 at the top ')
    s1_list.insert(None, 666)  
    s1_list.print_all_nodes()
    print()
    if s1_list.head != None and s1_list.tail != s1_list.head:
        print('Начало списка ', s1_list.head.value , 'next - ', s1_list.head.next.value)
        print('Конец списка ', s1_list.tail.value, 'next - ', s1_list.tail.next)
    elif s1_list.head != None:
        print('Начало списка ', s1_list.head.value , 'next - ', s1_list.head.next)
        print('Конец списка ', s1_list.tail.value, 'next - ', s1_list.tail.next)
    else:
        print('Начало списка ', s1_list.head)
        print('Конец списка ', s1_list.tail)        
    
    print()
    print('inserting 666 at the middle ')
    s2_list.insert(31, 666)
    s2_list.print_all_nodes()
    print()
    if s2_list.head != None and s2_list.tail != s2_list.head:
        print('Начало списка ', s2_list.head.value , 'next - ', s2_list.head.next.value)
        print('Конец списка ', s2_list.tail.value, 'next - ', s2_list.tail.next)
    elif s2_list.head != None:
        print('Начало списка ', s2_list.head.value , 'next - ', s2_list.head.next)
        print('Конец списка ', s2_list.tail.value, 'next - ', s2_list.tail.next)
    else:
        print('Начало списка ', s2_list.head)
        print('Конец списка ', s2_list.tail)       
    print()
    print('Test inserting 666 into a list that consists of a single item ')
    s3_list = LinkedList()
    s3_list.add_in_tail(Node(5))
    s3_list.insert(5, 666)
    s3_list.print_all_nodes()
    print()
    if s3_list.head != None and s3_list.tail != s3_list.head:
        print('Начало списка ', s3_list.head.value , 'next - ', s3_list.head.next.value)
        print('Конец списка ', s3_list.tail.value, 'next - ', s3_list.tail.next)
    elif s3_list.head != None:
        print('Начало списка ', s3_list.head.value , 'next - ', s3_list.head.next)
        print('Конец списка ', s3_list.tail.value, 'next - ', s3_list.tail.next)
    else:
        print('Начало списка ', s3_list.head)
        print('Конец списка ', s3_list.tail)       
    
    print()
    print('Test inserting 666 into empty list')
    s4_list = LinkedList()
    s4_list.insert(None, 666)  
    s4_list.print_all_nodes()
    print()
    if s4_list.head != None and s4_list.tail != s4_list.head:
        print('Начало списка ', s4_list.head.value , 'next - ', s4_list.head.next.value)
        print('Конец списка ', s4_list.tail.value, 'next - ', s4_list.tail.next)
    elif s4_list.head != None:
        print('Начало списка ', s4_list.head.value , 'next - ', s4_list.head.next)
        print('Конец списка ', s4_list.tail.value, 'next - ', s4_list.tail.next)
    else:
        print('Начало списка ', s4_list.head)
        print('Конец списка ', s4_list.tail)      
        
    print()        
    print('Test inserting 666 with invalid "afterNode" == 100')     
    s5_list = LinkedList()
    for i in list1:
        n = Node(i)
        s5_list.add_in_tail(n)
    s5_list.insert(100, 666) 
    s5_list.print_all_nodes()
    print()
    if s5_list.head != None and s5_list.tail != s5_list.head:
        print('Начало списка ', s5_list.head.value , 'next - ', s5_list.head.next.value)
        print('Конец списка ', s5_list.tail.value, 'next - ', s5_list.tail.next)
    elif s5_list.head != None:
        print('Начало списка ', s5_list.head.value , 'next - ', s5_list.head.next)
        print('Конец списка ', s5_list.tail.value, 'next - ', s5_list.tail.next)
    else:
        print('Начало списка ', s5_list.head)
        print('Конец списка ', s5_list.tail)         
    
    
    
        
test_1()        
test_2()        
test_3()        
test_4()
test_5()
