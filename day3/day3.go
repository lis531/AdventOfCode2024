package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
)

func main() {
	content, _ := os.ReadFile("example.txt")
	input := string(content)
	mulFound := regexp.MustCompile(`mul\((\d+),(\d+)\)`)
	sum := 0

	for _, match := range mulFound.FindAllStringSubmatch(input, -1) {
		a, _ := strconv.Atoi(match[1])
		b, _ := strconv.Atoi(match[2])
		sum += a * b
	}

	fmt.Println("Sum:", sum)
}
