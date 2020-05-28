def rotation(Ochered, N):
    for i in range(N):
        Ochered.enqueue(Ochered.dequeue())
    return Ochered
