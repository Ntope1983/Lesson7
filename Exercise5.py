import random
def ace_of_spades():
    spades={("heart",1),("diamond",1),("Spade",1),("Club",1)}
    print(spades)

def card_dealing(player,num_of_cards):
    for i in range(num_of_cards):
        x = random.choice(list(playing_cards))
        playing_cards.remove(x)
        player.add(x)



playing_cards = set()
kind_playing_card = ["heart", "diamond", "Spade", "Club"]
number_playing_card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for i in kind_playing_card:
    for j in number_playing_card:
        playing_cards.add((i,j))
player1= set()
player2=set()
card_dealing(player1,5)
card_dealing(player2,5)
ace_of_spades()