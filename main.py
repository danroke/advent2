Total_safe_reports = 0

with open('input.txt', 'r') as file:
    for line in file:    
        # each line will contain 6 ints
        row = line.split()
        row_size = len(row)
        # Valid reports must: 
        # - The levels are either all increasing or all decreasing.
        # - Any two adjacent levels differ by at least one and at most three.
        flag_inc = True
        flag_dec = True
        flag_diff = True

        index = 0
        while (index < row_size-1):

            curr = int(row[index])
            next = int(row[index+1])

            if curr < next:
                flag_inc = False
            if curr > next:
                flag_dec = False
            if (abs(curr - next) < 0) or (abs(curr - next) > 3):
                flag_diff = False
            index = index + 1

        # Check flags
        if (flag_inc == False and flag_dec == False) or (flag_diff == False):
            continue
        # Passed all checks, add report to count
        Total_safe_reports = Total_safe_reports + 1

    print("Total safe reports: ", Total_safe_reports)