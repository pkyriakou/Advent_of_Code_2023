def scratchcards_worth(input_path):
    with open(input_path) as input_text:
        cards = input_text.read().split("\n")
        overall_worth = 0
        for card in cards:
            winning_nums = card.split(":")[1].split("|")[0].split()
            player_nums = card.split(":")[1].split("|")[1].split()
            hits = 0
            for number in player_nums:
                if number in winning_nums:
                    hits += 1
            overall_worth += 2**(hits-1) if hits else 0
    return overall_worth

def collect_scatchcards(input_path):
    with open(input_path) as input_text:
        cards = input_text.read().split("\n")
        cards_collected = {}
        card_info = {}
        for index, card in enumerate(cards):
            cards_collected, card_info = collect_from_card(cards_collected, index, cards, card_info)

        return cards_collected, sum(cards_collected.values())

def collect_from_card(collection, index, cards, card_info):
    card = cards[index]
    card_id = card.split(":")[0]

    if card_id in collection:
        collection[card_id] += 1
    else:
        collection[card_id] = 1

    if card_id not in card_info:
        winning_nums = card.split(":")[1].split("|")[0].split()
        player_nums = card.split(":")[1].split("|")[1].split()
        hits = sum([1 for number in player_nums if number in winning_nums])
        card_info[card_id] = hits
    else:
        hits = card_info[card_id]

    for next_index in range(1, hits+1):
        if next_index < len(cards):
            collection, card_info = collect_from_card(collection, index+next_index, cards, card_info)

    return collection, card_info


print(scratchcards_worth("day_4/input_4_ex.txt"))
print(scratchcards_worth("day_4/input_4.txt"))
print(collect_scatchcards("day_4/input_4_ex.txt"))
print(collect_scatchcards("day_4/input_4.txt"))
