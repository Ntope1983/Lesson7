# Poker game with set and list

import random


def check_ace_of_spades(player):  # Έλεγχος αν υπάρχει καρέ του άσσου
    spades = {("heart", 1), ("diamond", 1), ("Spade", 1), ("Club", 1)}
    if spades.issubset(player):
        return True
    else:
        return False


def check_straight(player):  # έλεγχος εάν υπάρχει απλή κέντα
    list_player_card = list(player)  # Δημιουργούμε μία λίστα με στοιχεία του συνόλου
    list_player_card_number = [x[1] for x in list_player_card]  # Δημιουργούμε μία λίστα μόνο με αριθμού χωρίς φιγούρες
    list_player_card_number.sort()  # Ταξινόμηση λίστας
    for index in range(len(list_player_card_number) - 1):  # Ελέγχό εάν υπάρχει κέντα
        if list_player_card_number[index + 1] - list_player_card_number[index] == 1:
            continue
        else:
            return False
    return True


def card_dealing(player, num_of_cards):  # Μοιράζω 5 κάρτες
    for i in range(num_of_cards):
        x = random.choice(list(playing_cards))
        playing_cards.remove(x)
        player.add(x)


playing_cards = set()
kind_playing_card = ["heart", "diamond", "Spade", "Club"]
number_playing_card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for i in kind_playing_card:
    for j in number_playing_card:
        playing_cards.add((i, j))  # Οι κάρτες της τράπουλας
player1 = set()
player2 = set()
card_dealing(player1, 5)  # Μοιράζω 5 χαρτιά στο παίχτη1
card_dealing(player2, 5)  # Μοιράζω 5 χαρτιά στο παίχτη2


if check_ace_of_spades(player1):  # Έλεγχοι
    print("Ο παίχτης 1 έχει καρέ του άσσου")
if check_ace_of_spades(player2):
    print("Ο παίχτης 2 έχει καρέ του άσσου")

if check_straight(player1):
    print("Ο παίχτης 1 έχει κέντα")
if check_straight(player2):
    print("Ο παίχτης 2 έχει κέντα")
