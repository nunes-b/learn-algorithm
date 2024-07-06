package main

func main() {

	list := []int{1, 3, 5, 7, 9}
	item := 1
	result := binary_search(list, item)
	println(result)
}
func binary_search(list []int, item int) int {
	lower := 0
	upper := len(list) - 1
	for lower <= upper {
		middle := (lower + upper) / 2
		if list[middle] == item {
			return middle
		} else if list[middle] > item {
			upper = middle - 1
		} else {
			lower = middle + 1
		}
	}
	return -1

}
