func tribonacci(n int) int {
    res := []int{0, 1, 1}
    if n <= 2{
        return res[n]
    }
    a, b, c := 0, 1, 1

    for i := 3; i < n + 1; i++ {
        a, b, c = b, c, a + b + c
    }
    return c
}