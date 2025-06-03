
records = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name,score])
        
scores = sorted(set([score for name, score in records]))
second_lowest = scores[1]
        
names_with_second_lowest = sorted([name for name, score in records if score == second_lowest])
        
for name in names_with_second_lowest:
    print(name)