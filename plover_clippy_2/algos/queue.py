class IterableQueue:
    def __init__(self, num):
        self.queue = []
        self.max = num
        self.size = 0

    def full(self):
        return self.size == self.max

    def empty(self):
        return self.size == 0

    def put(self, val):
        if len(self.queue) == 0:
            self.queue.append(val)
            self.start = 0
            self.end = 0
            self.size = 1

        elif len(self.queue) < self.max:  # not full yet
            self.queue.append(val)
            self.end += 1
            self.size += 1

        elif self.size == self.max:
            raise ValueError(
                    "queue is full, need to remove some elements first")

        else:  # len(self.queue) == self.max
            self.end = (self.end + 1) % self.max
            self.queue[self.end] = val
            self.size += 1

    def remove(self):
        if len(self.queue) == 0 or self.size == 0:
            raise ValueError(
                    "queue is empty, need to put some elements first")
        self.size -= 1
        val = self.queue[self.start]
        self.start = (self.start + 1) % len(self.queue)
        return val

    def iterable(self):
        for i in range(self.start, self.start + self.size):
            yield self.queue[i % len(self.queue)]


if __name__ == "__main__":
    import unittest

    class TestQueue(unittest.TestCase):
        def test_single_element(self):
            queue = IterableQueue(1)
            queue.put(1)
            with self.assertRaises(ValueError):
                queue.put(1)
            self.assertEqual(queue.remove(), 1)
            with self.assertRaises(ValueError):
                queue.remove()

        def test_order(self):
            queue = IterableQueue(4)
            queue.put(1)
            queue.put(2)
            queue.put(3)
            queue.put(4)
            self.assertEqual(queue.remove(), 1)
            self.assertEqual(queue.remove(), 2)
            self.assertEqual(queue.remove(), 3)
            self.assertEqual(queue.remove(), 4)

        def test_combination_put_remove(self):
            queue = IterableQueue(5)
            queue.put(1)
            queue.put(2)
            queue.put(3)
            queue.put(4)
            queue.put(5)
            self.assertEqual(queue.full(), True)
            with self.assertRaises(ValueError):
                queue.put(1)
            self.assertEqual(queue.remove(), 1)
            self.assertEqual(queue.remove(), 2)
            queue.put(-1)
            queue.put(-2)
            self.assertEqual(queue.remove(), 3)
            self.assertEqual(queue.remove(), 4)
            self.assertEqual(queue.remove(), 5)
            self.assertEqual(queue.remove(), -1)
            self.assertEqual(queue.remove(), -2)
            queue.put(1)
            queue.put(3)
            queue.put(4)
            self.assertEqual(queue.full(), False)
            self.assertEqual(queue.remove(), 1)
            self.assertEqual(queue.remove(), 3)
            self.assertEqual(queue.remove(), 4)
            with self.assertRaises(ValueError):
                queue.remove()
            self.assertEqual(queue.empty(), True)

        def test_iterate(self):
            queue = IterableQueue(5)
            queue.put(1)
            queue.put(2)
            queue.put(3)
            queue.put(4)
            queue.put(5)
            self.assertEqual(list(queue.iterable()), [1, 2, 3, 4, 5])
            self.assertEqual(queue.remove(), 1)
            self.assertEqual(queue.remove(), 2)
            self.assertEqual(list(queue.iterable()), [3, 4, 5])
            queue.put(-1)
            queue.put(-2)
            self.assertEqual(list(queue.iterable()), [3, 4, 5, -1, -2])
            self.assertEqual(queue.remove(), 3)
            self.assertEqual(queue.remove(), 4)
            self.assertEqual(queue.remove(), 5)
            self.assertEqual(queue.remove(), -1)
            self.assertEqual(queue.remove(), -2)
            self.assertEqual(list(queue.iterable()), [])
            queue.put(1)
            queue.put(3)
            queue.put(4)
            self.assertEqual(list(queue.iterable()), [1, 3, 4])
            self.assertEqual(queue.remove(), 1)
            self.assertEqual(queue.remove(), 3)
            self.assertEqual(queue.remove(), 4)
            self.assertEqual(list(queue.iterable()), [])


    unittest.main()
