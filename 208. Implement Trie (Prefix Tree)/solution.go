type Trie struct {
    root *TrieNode
}

type TrieNode struct {
    children  []*TrieNode
    isWord bool
}

func Constructor() Trie {
    return Trie{&TrieNode{children: make([]*TrieNode, 26)}}
}

func (this *Trie) Insert(word string) {
    if len(word) == 0 {
        return
    }

	node := this.root
	for _, char := range word {
		if node.children[char-'a'] == nil {
			node.children[char-'a'] = &TrieNode{make([]*TrieNode, 26), false}
		}
		node = node.children[char-'a']
	}
	node.isWord = true
}

func (this *Trie) Search(word string) bool {
    if len(word) == 0 {
        return false
    }

    node := this.root
    for _, char := range word {
        if node.children[char-'a'] == nil {
            return false
        }
        node =  node.children[char-'a']
    }

    return node.isWord
}

func (this *Trie) StartsWith(prefix string) bool {
    if len(prefix) == 0 {
        return true
    }

    node := this.root
    for _, char := range prefix {
        if node.children[char-'a'] == nil {
            return false
        }
        node =  node.children[char-'a']
    }


    return true
}