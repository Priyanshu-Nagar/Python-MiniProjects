
while True:
    no_ofscore=int(input())    
    if 2 <= no_ofscore <= 10:
        while True:
            scores=input().split()
            scores=[int(x) for x in scores]
            if len(scores) != no_ofscore:
                print("Number of scores does not match the specified count.")
                continue
            if any(score < -100 or score > 100 for score in scores):
                print("Scores must be between -100 and 100.")    
                continue   
            else:
                scores.remove(max(scores))
                # scores.remove(min(scores))
                print(max(scores))
                break
        break
    else:
        print("Invalid input, please enter a number between 2 and 10.")

