from masks import get_mask_account, get_mask_card_number

def mask_account_card(data_acc_or_card: str) -> str:
    "Функция, маскирующая номер счета или номер карты"
    if data_acc_or_card.startswith("Счет") and len(data_acc_or_card) == 25:
        masked_data = get_mask_account(data_acc_or_card[5:])
    else:
        masked_data = get_mask_card_number(data_acc_or_card[-16:])
    return masked_data
# data_acc_or_card = "Счет 64686473678894779589"
data_acc_or_card = "MasterCard 7158300734726758"
# result = mask_account_card(data_acc_or_card)
result = data_acc_or_card[-16:]
print(result)