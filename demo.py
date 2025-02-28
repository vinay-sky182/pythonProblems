def main():
    sum = 0
    seven_count = 0

    input = [2, 3, 4, 7, 14, 21, 7, 7, 21, 23]

    for num in input:
        if num == 7:
            seven_count += 1
            if seven_count == 2 or seven_count > 3:
                sum += num
            continue
        if seven_count < 1 or seven_count > 2:
            sum += num

    print("Result:", sum)

main()

