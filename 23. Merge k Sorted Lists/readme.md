# Merge sort


```python
def bottomup_mergesort(list):
	length = len(list)
	size = 1
	while size < length:
		size+=size # initializes at 2 as described
		for pos in range(0, length, size):
			sublist_start = pos
			sublist_mid   = pos + (size / 2)
			sublist_end = pos + size
			left  = list[ sublist_start : sublist_mid ]
			right = list[   sublist_mid : sublist_end ]
			list[sublist_start:sublist_end] = merge(left, right)
	return list
```

```
def bottomup_mergesort(list):
    '''inplace'''
	length = len(list)
	temp = [0] * length
	size = 1
	while size < length:
		pos = 0
		while pos < length:
			if (pos+2*size-1 >= length):
				merge(list, temp, pos, pos+size-1, length-1)
			else:
				merge(list, temp, pos, pos+size-1, pos+2*size-1)
			pos+=2*size
		size+=size
	return
```
