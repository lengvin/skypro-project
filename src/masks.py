import logging


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
    filename="../logs/masks.log",
    filemode="w",
)
module_logger = logging.getLogger(__name__)


def get_mask_card_number(card_number: int) -> str:
    """
    создание маски по номеру карты
    номер карты должен состоять из 16 цифр
    """
    str_card_number = str(card_number)

    if len(str_card_number) != 16:
        module_logger.error("Ошибка, номер карты состоит НЕ из 16 цифр")
        raise ValueError("Номер карты должен состоять из 16 цифр")

    list_number = []
    for i in range(4):
        list_number.append(str_card_number[i * 4: (i * 4) + 4])

    list_number[2] = "****"
    list_number[1] = list_number[1][0:2] + "**"
    result = " ".join(list_number)

    module_logger.info("Создание маски номера карты")

    return result


def get_mask_account(check_number: int) -> str:
    """
    создание маски по номеру счёта
    номер счёта долже состоять из 20 цифр
    """
    str_check_number = str(check_number)

    if len(str_check_number) != 20:
        module_logger.error("Ошибка, номер счёта состоит НЕ из 20 цифр")
        raise ValueError("Номер счёта должен состоять из 20 цифр")

    last_digits = str_check_number[-4::]
    result = "**" + last_digits

    module_logger.info("Создание маски счёта")

    return result
