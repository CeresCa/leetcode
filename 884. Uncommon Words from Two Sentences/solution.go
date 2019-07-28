import (
	"strings"
)

func uncommonFromSentences(A string, B string) []string {
	aList := strings.Split(A, " ")
	bList := strings.Split(B, " ")
	aDict := make(map[string]int)
	bDict := make(map[string]int)
	for _, a := range aList {
		if _, ok := aDict[a]; ok {
			aDict[a]++
		} else {
			aDict[a] = 1
		}
	}
	for _, b := range bList {
		if _, ok := bDict[b]; ok {
			bDict[b]++
		} else {
			bDict[b] = 1
		}
	}
	res := make([]string, 0)
	for _, a := range aList {
		if _, ok := bDict[a];! ok && aDict[a] == 1 {
			res = append(res, a)
		}
	}

	for _, b := range bList {
		if _, ok := aDict[b]; ! ok && bDict[b] == 1 {
			res = append(res, b)
		}
	}
	return res
}
