1. Python 中的迭代器、可迭代对象、生成器的区别是什么，分别怎么实现

    在 Python 中**迭代器一定是可迭代对象**。可以通过 *next* 方法来获取下一个元素的对象都可以称为迭代器。而可迭代对象不一定是迭代器，只是可以通过如 *for* 方法进行遍历的对象。

    ```python
    from collections.abc import Iterator
    nums = list("123")
    isinstance(nums, Iterator)  # False
    # 使用 iter 方法将可迭代对象转换未迭代器
    numsIterator = iter(nums)
    isinstance(nums, Iterator)  # True
    ```

    关于生成器最明显的特点是方法中的关键字 *yield* ，如下给出一个斐波那契的例子：

    ```python
    def fib():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b
    ```

    生成器最大的特点就是懒执行(lazy evaluation)，以 Python 2 中的 range 为例:

    ```python
    nums = range(100000)
    sys.getsizeof(nums)  # 800072
    
    def srange(n):
    	start = 0
        while start < n:
            yield start
            start += 1
    ```

    

    

