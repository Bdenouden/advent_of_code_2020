file <- file("day1/input.txt", open='r')

sum<-c()

lines <- readLines(file)
for (i in 1:length(lines)){
    val1 <- strtoi(lines[i], 10L)

    for(j in (length(tail(lines, -i))):length(lines)){
        if(j==0){
            print("ignored!")
            break;
        }
        val2 <- strtoi(lines[j], 10L)
        sum<-append(sum, val1+val2)

        # print(sprintf("%d + %d = %d", val1, val2, sum))

        sum = val1 + val2
        if(sum == 2020){
            print(sprintf("%d + %d = %d", val1, val2, sum))
            print(sprintf("solution = %d", val1*val2))
        }
    }
}
# print(sum)
print("done!")

close(file)