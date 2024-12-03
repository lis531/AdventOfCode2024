package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func main() {
	content, _ := os.ReadFile("example.txt")
	input := string(content)

	mulRegex := regexp.MustCompile(`mul\((\d+),(\d+)\)`)
	splitInput := strings.Split(input, "don't()")
	sum := 0

	for _, line := range splitInput {
		doSplit := strings.Split(line, "do()")
		for index, doPart := range doSplit {
			if index > 0 {
				matches := mulRegex.FindAllStringSubmatch(doPart, -1)
				for _, match := range matches {
					a, _ := strconv.Atoi(match[1])
					b, _ := strconv.Atoi(match[2])
					sum += a * b
				}
			}
		}
	}

	fmt.Println("Sum:", sum)
}
