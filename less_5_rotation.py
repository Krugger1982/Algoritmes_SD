def rotation(Ochered, N):
    for i in range(N):
        target = Ochered.dequeue()
        Ochered.enqueue(target)
    return Ochered
