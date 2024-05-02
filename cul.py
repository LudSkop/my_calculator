pay_system = {
    5 : 'MasterCard',
    4 : 'Visa',
    3 : 'American Express'
}
card_numbers = ['5553336668889994', '4444444488888888', '3333556677889908', '234567832ouy6789']

def is_valid_card(card:str)-> bool:
    return card.isdigit() and len(card) == 16

for card in card_numbers:
    string = 'Номер картки: {:<8}  платіжна система: {:^16} картка валідна: {:>16}'
    print(string.format(card, pay_system.get(int(card[0]), 'Unknown'), str(is_valid_card(card))))





