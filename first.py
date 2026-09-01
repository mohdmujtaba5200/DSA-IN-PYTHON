phrase = "hello"
print(phrase)

gender = "is male"
age = "50"
print("the person is " + gender + " and is " + age + " years old")

phrase = "hello world"
print (phrase [ 0:5])

def sayhi (name ,age):
    print ("hello" +name + "you are" +age  )

sayhi ("mike", "50")

cards = [ 10 , 9,8,7,6,5,4,3,2,1]
query =[7]

def locate_cards (cards,query):
    position = 0
    while position < (len(cards)):
        if cards[position] == query[7]:
            return position
        position +=1
        return -1
cards = [ 10 , 9,8,7,6,5,4,3,2,1]
query =[7]
    