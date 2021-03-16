package main

import "fmt"

func main() {
	var A int
	var B int
	var C int
	var X int
	fmt.Scan(&A)
	fmt.Scan(&B)
	fmt.Scan(&C)
	fmt.Scan(&X)

	var ans = 0
	for i:=0; i<=A; i++ {
		for j:=0; j<=B; j++ {
			var rest = X - i * 500 - j * 100
			if 0 <= rest && rest <= 50 * C {
				ans++
			}
		}
	}
	fmt.Printf("%d\n", ans)
}
