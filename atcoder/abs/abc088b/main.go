package main

import (
	"fmt"
	"sort"
)

func main() {
	var N int
	fmt.Scan(&N)
	var a []int
	for i := 0; i < N; i++ {
		var num int
		fmt.Scanf("%d", &num)
		a = append(a, num)
	}

	var ans = 0

	sort.Sort(sort.Reverse(sort.IntSlice(a)))
	for i := 0; i < N; i++ {
		if i % 2 == 0 {
			ans += a[i]
		} else {
			ans -= a[i]
		}
	}

	fmt.Printf("%d\n", ans)
}
