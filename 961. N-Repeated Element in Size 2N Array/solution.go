func repeatedNTimes(A []int) int {
    counts := make(map[int]int)
    for _,a := range A {
        if _,ok := counts[a]; ok {
            return a
        } else {
            counts[a] = 1
        }
    }
    return 0
}