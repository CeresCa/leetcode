func twoSum(nums []int, target int) []int {
    myMap := make(map[int]int)
    for i := 0;i < len(nums);i++ {
        if _, ok := myMap[target - nums[i]];ok {
            return []int{myMap[target - nums[i]], i}
        }
        myMap[nums[i]] = i
    }
    return nil
}