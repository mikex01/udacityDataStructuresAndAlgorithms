## **rlu_cache**

Basically, an LRU cache is made up of two data structures.
- HashMap
- DobleLinkedList

For this structure, we get a search quickly thanks to the **HashMap**, which points to a node in the DoubleLinkedList, making it easy to insert data = `O(1)`.
On the other hand, we have the **DoubleLinkedList** to order data, when data is required it can be obtained using its key = `O(1)`.

In conclusion, what we get from LRU Cache is time, but we lose a bit of space because it requires two data structures for implementation. See figure rlu_cache

![rlu_cache](https://github.com/mikex01/udacityDataStructuresAndAlgorithms/blob/master/02_show_me_the_data_structures/01_lru_cache/lru_cache.png?raw=true)