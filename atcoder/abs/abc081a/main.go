package main

import (
	"fmt"
	"strings"
)

func main() {
	var s string
	fmt.Scanf("%s", &s)

	ans := strings.Count(s, "1")
	fmt.Printf("%d\n", ans)
}
