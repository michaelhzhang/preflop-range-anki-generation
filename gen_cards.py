import genanki

CARDS = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
SUITED_TYPES = ['o','s']
DECK_ID  = 1301972725
MODEL_ID = 1373012850
PACKAGE_NAME = 'preflop_rfi_range.apkg'
DECK_NAME =  'Upswing Preflop RFI Hand Ranges'
POSITION_RANGE_MAP = {
    '9 Person Table, UTG ': [
        'AA',
        'AKs',
        'AQs',
        'AJs',
        'ATs',
        'A5s',
        'AKo',
        'AQo'
        'KK',
        'KQs',
        'KJs',
        'KTs',
        'QQ',
        'QJs',
        'QTs',
        'JJ',
        'JTs',
        'J9s',
        'TT',
        'T9s',
        '99',
        '98s',
        '88',
        '77'
    ],
    '9 Person Table, LoJack / 6 person table UTG': [
        'AA',
        'AKs',
        'AQs',
        'AJs',
        'ATs',
        'A9s',
        'A8s',
        'A7s',
        'A6s',
        'A5s',
        'A4s'
        'A3s',
        'A2s',
        'AKo',
        'AQo',
        'AJo',
        'KK',
        'KQs',
        'KJs',
        'KTs',
        'K9s',
        'KQo',
        'QQ',
        'QJs',
        'QTs',
        'Q9s',
        'JJ',
        'JTs',
        'J9s',
        'TT',
        'T9s',
        'T8s',
        '99',
        '98s',
        '88',
        '87s',
        '77',
        '76s',
        '66',
        '55'
    ],
    'Cutoff': [
        'AA',
        'AKs',
        'AQs',
        'AJs',
        'ATs',
        'A9s',
        'A8s',
        'A7s',
        'A6s',
        'A5s',
        'A4s'
        'A3s',
        'A2s',
        'AKo',
        'AQo',
        'AJo',
        'ATo',
        'KK',
        'KQs',
        'KJs',
        'KTs',
        'K9s',
        'K8s',
        'KQo',
        'KJo',
        'KTo',
        'QQ',
        'QJs',
        'QTs',
        'Q9s',
        'Q8s',
        'QJo',
        'QTo',
        'JJ',
        'JTs',
        'J9s',
        'J8s',
        'JTo',
        'TT',
        'T9s',
        'T8s',
        '99',
        '98s',
        '97s',
        '88',
        '87s',
        '86s',
        '77',
        '76s',
        '66',
        '65s',
        '55',
        '54s',
        '44',
        '33',
        '22'
    ],
    'Button': [
        'AA',
        'AKs',
        'AQs',
        'AJs',
        'ATs',
        'A9s',
        'A8s',
        'A7s',
        'A6s',
        'A5s',
        'A4s'
        'A3s',
        'A2s',
        'AKo',
        'AQo',
        'AJo',
        'ATo',
        'A9o',
        'A8o',
        'A7o',
        'A6o',
        'A5o',
        'A4o',
        'A3o',
        'A2o',
        'KK',
        'KQs',
        'KJs',
        'KTs',
        'K9s',
        'K8s',
        'K7s',
        'K6s',
        'K5s',
        'K4s',
        'K3s',
        'KQo',
        'KJo',
        'KTo',
        'K9o',
        'QQ',
        'QJs',
        'QTs',
        'Q9s',
        'Q8s',
        'Q7s',
        'Q6s',
        'Q5s',
        'QJo',
        'QTo',
        'Q9o',
        'JJ',
        'JTs',
        'J9s',
        'J8s',
        'J7s',
        'J6s',
        'JTo',
        'J9o',
        'TT',
        'T9s',
        'T8s',
        'T7s',
        'T6s',
        'T9o',
        '99',
        '98s',
        '97s',
        '96s',
        '88',
        '87s',
        '86s',
        '85s',
        '77',
        '76s',
        '75s',
        '66',
        '65s',
        '64s',
        '55',
        '54s',
        '44',
        '43s',
        '33',
        '22'
    ],
}

def get_all_hands():
    hands  = []
    for i in range(len(CARDS)):
        for j in range(i, len(CARDS)):
            card1 = CARDS[i]
            card2 = CARDS[j]

            if card1 == card2:
                hands.append(card1 + card2)
            else:
                for suit in SUITED_TYPES:
                    hands.append(card1 + card2 + suit)
    return hands

def get_model():
    my_model = genanki.Model(
      MODEL_ID,
      'Simple Model',
      fields=[
              {'name': 'Question'},
              {'name': 'Answer'},
            ],
      templates=[
              {
                        'name': 'Card 1',
                        'qfmt': '{{Question}}',
                        'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
                      },
            ])
    return my_model

def get_deck():
    deck = genanki.Deck(
        DECK_ID,
        DECK_NAME)
    return deck

def gen_anki_cards(raise_range, position, model, deck):
    hands = get_all_hands()
    for hand in hands:
        question = position + ': ' + hand
        if hand in raise_range:
            answer = 'raise first in'
        else:
            answer = 'no raise first in'
        note = genanki.Note(
            model = model,
            fields = [question, answer])
        deck.add_note(note)

def gen_deck():
    deck = get_deck()
    model = get_model()
    for position, raise_range in POSITION_RANGE_MAP.items():
        gen_anki_cards(raise_range, position, model, deck)
    genanki.Package(deck).write_to_file(PACKAGE_NAME)

if __name__ == "__main__":
    gen_deck()
