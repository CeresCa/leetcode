func toLowerCase(str string) string {
    lowercase := "abcdefghijklmnopqrstuvwxyz"
    uppercase := "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_dict := map[string]string{}
    for i := 0; i < 26; i++ {
        lower_dict[string(uppercase[i])] = string(lowercase[i])
    }
    str_list  := []string{}
    for _, s := range str {
        if string(lower_dict[string(s)]) != "" {
            str_list = append(str_list, lower_dict[string(s)])
        } else {
            str_list = append(str_list, string(s))
        }
    }
    return strings.Join(str_list,"")
}