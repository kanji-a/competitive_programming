package main

import (
	"fmt"
)

func main() {
	var N int
	fmt.Scanf("%d", &N)
	d := make(map[int]bool)
	for i := 0; i < N; i++ {
		var num int
		fmt.Scanf("%d", &num)
		d[num] = true
	}

	ans := len(d)

	fmt.Printf("%d\n", int(ans))
}
