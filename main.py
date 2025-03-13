VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

facecard_value = {'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


def blackjack_score(hand):
    if len(hand) < 3 or len(hand) > 5:
        return "Invalid Cards"
     
    if not all(card in VALID_CARDS for card in hand):
        return "Invalid Cards"
    
    score = 0
    ace_count = 0

    for card in hand:
        if isinstance(card, int):
            score += card
        elif card in facecard_value:
            if card == "Ace":
                ace_count += 1
            score += facecard_value[card]
     
    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -=1

    
    if score > 21:
        return "Bust"

    return score