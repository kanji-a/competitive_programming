package main

import "fmt"

func main() {
	var S string
	fmt.Scan(&S)

	var ans = "YES"
	var i = len(S)

	for i > 0 {
		if i - 5 >= 0 && (S[i-5:i] == "erase" || S[i-5:i] == "dream") {
			i -= 5
		} else if i - 6 >= 0 && S[i-6:i] == "eraser" {
			i -= 6
		} else if i - 7 >= 0 && S[i-7:i] == "dreamer" {
			i -= 7
		} else {
			ans = "NO"
			break
		}
	}

	fmt.Printf("%s\n", ans)
}
