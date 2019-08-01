func lengthOfLongestSubstring(s string) int {
	start := 0
	maxLen := 0
	used := [256]int{}
	for i := 0; i < len(used); i++ {
		used[i] = -1
	}

    for i := 0; i < len(s); i++ {
        if used[s[i]]  >= start {
            start = used[s[i]] +1
        } else if i - start + 1 >maxLen {
            maxLen = i - start +1
        }
        used[s[i]] = i
    }

	return maxLen
}
