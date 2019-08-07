func hammingDistance(x int, y int) int {
    z := 0
    for x > 0 || y > 0 {
        z += (x & 1) ^ (y & 1)
        x = x >> 1
        y = y >> 1
    }
    return z
}