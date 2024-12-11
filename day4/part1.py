with open("day4.txt") as f:
    wordsearch = f.read().split("\n")
    
    count = 0
    for i in range(len(wordsearch)):
        for j in range (len(wordsearch[i])):
            if wordsearch[i][j] == "X":
                left_up = wordsearch[i][j]
                left_down = wordsearch[i][j]
                right_up = wordsearch[i][j]
                right_down = wordsearch[i][j]
                up = wordsearch[i][j]
                down = wordsearch[i][j]
                left = wordsearch[i][j]
                right = wordsearch[i][j]

                for k in range(1,4):
                    if (i - k) >= 0 and (j - k) >= 0:
                        left_up += wordsearch[i - k][j - k] # build string back diagnol
                    
                    if (j - k) >= 0 and (i + k) <= len(wordsearch) - 1:
                        left_down += wordsearch[i + k][j - k]
                    
                    if (i - k) >= 0 and (j + k) <= len(wordsearch[i]) - 1:
                        right_up += wordsearch[i - k][j + k]
                    
                    if (i + k) <= len(wordsearch) - 1 and (j + k) <= len(wordsearch[i]) - 1:
                        right_down += wordsearch[i + k][j + k]
                    
                    if (i - k) >= 0:
                        up += wordsearch[i - k][j]
                    
                    if (i + k) <= len(wordsearch) - 1:
                        down += wordsearch[i + k][j]
                    
                    if (j - k) >= 0:
                        left += wordsearch[i][j - k]
                    
                    if (j + k) <= len(wordsearch[i]) - 1:
                        right += wordsearch[i][j + k]
            
                candidates = [up, down, left, right, left_down, left_up, right_down, right_up]
                count += sum(x == "XMAS" for x in candidates)

print(count)