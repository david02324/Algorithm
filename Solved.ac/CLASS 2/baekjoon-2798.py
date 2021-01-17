cardNum, target = map(int,input().split())
cards = list(map(int,input().split()))
sortedCards = [i for i in cards if i <= target-3]
sortedCards.sort()
cardsLen = len(sortedCards)
def find(cardsLen,sortedCards):
    a = []
    for i in range(cardsLen-1,1,-1):
        for j in range(i-1,0,-1):
            for k in range(j-1,-1,-1):
                sum = sortedCards[i] + sortedCards[j] + sortedCards[k]
                if sum <= target:
                    a.append(sum)
                    break
    
    return max(a)

print(find(cardsLen,sortedCards))