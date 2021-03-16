package main

import "fmt"

func main() {
	var N int
	var A int
	var B int
	fmt.Scan(&N)
	fmt.Scan(&A)
	fmt.Scan(&B)

	var ans = 0

	for i:=1; i<=N; i++ {
		var tmp = i
		var s = 0
		for tmp > 0 {
			s += tmp % 10
			tmp /= 10
		}
		if A <= s && s <= B {
			ans += i
		}
	}

	fmt.Printf("%d\n", ans)
}
