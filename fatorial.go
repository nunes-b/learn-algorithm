package main

func fatorial(n int) int {
	if n <= 0 {
		return 1
	}
	return n * fatorial(n-1)
}

func main() {
	println(fatorial(3))
}
