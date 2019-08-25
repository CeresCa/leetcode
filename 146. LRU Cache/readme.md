##  题目描述

> Design and implement a data structure for [Least Recently Used (LRU) cache](https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU). It should support the following operations: `get` and `put`.
>
> `get(key)` - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
> `put(key, value)` - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
>
> The cache is initialized with a **positive** capacity.
>
> **Follow up:**
> Could you do both operations in **O(1)** time complexity?
>
> **Example:**
>
> ```
> LRUCache cache = new LRUCache( 2 /* capacity */ );
> 
> cache.put(1, 1);
> cache.put(2, 2);
> cache.get(1);       // returns 1
> cache.put(3, 3);    // evicts key 2
> cache.get(2);       // returns -1 (not found)
> cache.put(4, 4);    // evicts key 1
> cache.get(1);       // returns -1 (not found)
> cache.get(3);       // returns 3
> cache.get(4);       // returns 4
> ```

##  解题思路

lru cache在操作系统和各种数据库、缓存系统中都很常用，所以有很多成熟的实现，

参考 [LRUCache 的各种实现](https://github.com/shidenggui/blog/issues/17) 和 [LRU Cache在Python中的实现](https://hugoren.iteye.com/blog/2389628) :

一般做法是用双向链表+哈希表存储，当get set已有key时，移动到最前，当超过容量，删除最后一个节点，新节点插入到最前，
使用伪头尾节点简化链表操作、使用双向循环链表，减少插入删除节点的次数。



###  特殊实现：[redis](https://segmentfault.com/a/1190000017555834)

> 当 redis 达到设置的 `maxmemory`，会从所有key 中随机抽样 5 个值，然后计算它们的 idle time，插入一个长度为 16 的待淘汰数组中，数组中的 entry 根据 idle time 升序排列，最右侧的就是接下来第一个被淘汰的。淘汰后如果内存还是不满足需要，则继续随机抽取 `key` 并循环以上过程。