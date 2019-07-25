package main

import "fmt"

func isOneBitCharacter(bits []int) bool {
	var i = 0

	for i < len(bits)-1 {
		if bits[i] == 0 {
			i++
		} else {
			i += 2
		}
	}
	if i == len(bits)-1 {
		return true
	} else {
		return false
	}
}
func main() {
	var res = isOneBitCharacter([]int{1, 1, 0})
	fmt.Println(res)
}
