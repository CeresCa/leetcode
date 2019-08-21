func isValid(s string) bool {
	par := map[byte]byte{
		')': '(',
		']': '[',
		'}': '{'}
	keys := map[byte]byte{
		')': 0,
		']': 0,
		'}': 0}
	values := map[byte]byte{
		'(': 0,
		'[': 0,
		'{': 0}
	stack := []byte{}
	res := false
	for i := 0; i < len(s); i++ {
		if _, ok := values[s[i]]; ok {
			stack = append(stack, s[i])
		} else if _, ok := keys[s[i]]; ok {
			if len(stack) == 0 {
				res = false
				return res
			}
			result := stack[len(stack)-1]
			stack = stack[:len(stack)-1]

			if result != par[s[i]] {
				res = false
                return res
			}
		}

	}
	if len(stack) > 0 {
		res = false
	} else {
		res = true
	}
	return res
}