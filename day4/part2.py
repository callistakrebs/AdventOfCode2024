with open("day4_test2.txt") as f:
    wordsearch = f.read().split("\n")
    
    count = 0
    for i in range(len(wordsearch)):
        for j in range (len(wordsearch[i])):
            if wordsearch[i][j] == "A":
                if (i - 1) >= 0 and (j - 1) >= 0 and (i + 1) <= len(wordsearch) - 1 and (j + 1) <= len(wordsearch[i]) - 1:
                    left_diag = wordsearch[i - 1][j - 1] + wordsearch[i][j] + wordsearch[i + 1][j + 1]
                    right_diag = wordsearch[i - 1][j + 1] + wordsearch[i][j] + wordsearch[i + 1][j - 1]
                
                    if (left_diag == "SAM" or left_diag == "MAS") and (right_diag == "SAM" or right_diag == "MAS"):
                        count+=1

print(count)