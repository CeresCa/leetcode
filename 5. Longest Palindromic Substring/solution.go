func longestPalindrome(s string) string {
    result := ""
    if len(s) == 0{
        return ""
    } else if len(s) == 1{
        return s
    }
    for i := 0;i < len(s);i++{
        if len(s) - 1 <= len(result) / 2{
            break
        }
        temp1 := checkPalindrome(s, i, i)
        if len(temp1) > len(result){
            result = temp1
        }
        temp2 := checkPalindrome(s, i, i + 1)
        if len(temp2) > len(result){
            result = temp2
        }
    }
    return result
}

func checkPalindrome(s string, l int, r int) string{
    for l >= 0 && r < len(s) && s[l] == s[r]{
        l -= 1
        r += 1
    }
    return s[l + 1:r]
}