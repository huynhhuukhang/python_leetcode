package main

import "fmt"

func minCostClimbingStairs(cost []int) int {
n := len(cost)

for i := 2; i < n; i++ {
cost[i] += min(cost[i-1], cost[i-2])
}

return min(cost[n-1], cost[n-2])
}

func min(a, b int) int {
if a < b {
return a
}
return b
}

func main() {
cost1 := []int{10, 15, 20}
result1 := minCostClimbingStairs(cost1)
fmt.Printf("Vi du 1: Chi phi toi thieu la %d\n", result1)

cost2 := []int{1, 100, 1, 1, 1, 100, 1, 1, 100, 1}
result2 := minCostClimbingStairs(cost2)
fmt.Printf("Vi du 2: Chi phi toi thieu la %d\n", result2)
}