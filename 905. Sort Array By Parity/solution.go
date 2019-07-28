func sortArrayByParity(A []int) []int {
    ans := []int{}
    for _, a := range A {
        if a % 2 == 0 {
            ans = append(ans, a)
        }
        }
    for _, a := range A {
        if a % 2 != 0 {
            ans = append(ans, a)
        }
        } 
    return ans
        
}