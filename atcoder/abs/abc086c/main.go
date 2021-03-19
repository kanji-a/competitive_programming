package main

import (
	"fmt"
	"math"
)

func main() {
	var N int
	fmt.Scanf("%d", &N)

	ans := "Yes"

	t := 0
	x := 0
	y := 0
	t_pre := 0
	x_pre := 0
	y_pre := 0
	t_d := 0
	x_d := 0
	y_d := 0
	for i := 0; i < N; i++ {
		fmt.Scanf("%d", &t)
		fmt.Scanf("%d", &x)
		fmt.Scanf("%d", &y)
		t_d = t - t_pre
		x_d = int(math.Abs(float64(x - x_pre)))
		y_d = int(math.Abs(float64(y - y_pre)))
		t_pre = t
		x_pre = x
		y_pre = y
		if x_d + y_d > t_d || (t_d - x_d - y_d) % 2 == 1 {
			ans = "No"
			break
		}
	}

	fmt.Printf("%s\n", ans)
}
