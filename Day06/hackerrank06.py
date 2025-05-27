# Given the participants' score sheet for your University Sports Day,
# you are required to find the runner-up score. You are given n scores. 
# Store them in a list and find the score of the runner-up.
import math

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    scores = list(set(arr))
    scores.sort(reverse = True)
    runnerUp = scores[1]
    print(runnerUp)

