cards = [ 10 , 9,8,7,6,5,4,3,2,1]
query =7

def locate_cards (cards,query):
    position = 0
    while position < (len(cards)):
        if cards[position] == query[0]:
            return position
        position +=1
    return -1
cards = [ 10 , 9,8,7,6,5,4,3,2,1]
query =[7]

result = locate_cards(cards,query)
#output   = 3
print (result)  









