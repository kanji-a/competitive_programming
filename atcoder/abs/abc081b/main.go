package main

import (
	"fmt"
	"math"
)

func main() {
	var N int
	fmt.Scanf("%d", &N)
	var A []int
	for i := 0; i < N; i++ {
		var num int
		fmt.Scanf("%d", &num)
		A = append(A, num)
	}

	ans := float64(math.MaxInt64)
	for i := 0; i < N; i++ {
		var cnt float64
		for A[i] % 2 == 0 {
			A[i] /= 2
			cnt++
		}
		ans = math.Min(cnt, ans)
	}

	fmt.Printf("%d\n", int(ans))
}
