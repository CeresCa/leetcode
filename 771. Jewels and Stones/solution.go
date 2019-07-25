func numJewelsInStones(J string, S string) int {
    count := 0
    for _, s := range S {
        if strings.Contains(J, string(s)) == true{
            count++}
    }
    return count
}