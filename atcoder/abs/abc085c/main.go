package main

import (
	"fmt"
)

func main() {
	var N int
	fmt.Scanf("%d", &N)
	var Y int
	fmt.Scanf("%d", &Y)

	ans := [3]int{-1, -1, -1}

	for i := 0; i <= N; i++ {
		for j := 0; j <= N - i; j++ {
			if 10000 * i + 5000 * j + 1000 * (N - i - j) == Y {
				ans[0] = i
				ans[1] = j
				ans[2] = N - i - j
			}
		}
	}

	fmt.Printf("%d %d %d\n", ans[0], ans[1], ans[2])
}
