
phone = ['380963!610573', '66389490', '2(345)15678', '56_464_35',' 06(3193404)8', '380983864330', '36364 46656', ]

codes_operators ={'067','098', '063', '097', '096', }

def sanitize_phone(phone:str)-> str:
    new_phone = (phone.strip()
                 .replace('!', '')
                 .replace('_', '')
                 .replace(' ', '')
                 .replace('(', '')
                 .replase(')', '')
                 )
    return print(new_phone)


phone = ['380963!610573', ' 66389490', '2(345)15678', ' 56_464_35',' 06(3193404)8', '380983864330', '36364 46656']

codes_operators = {'067', '098', '063', '097', '096'}

def sanitize_phone(phone:str)-> str:
    new_phone = (phone.strip()
                 .replace('!', '')
                 .replace('_', '')
                 .replace(' ', '')
                 .replace('(', '')
                 .replace(')', '')
                 )
    return new_phone


def is_valid_phone(phone:str)-> bool:
    def is_valid_operator(phone:str)->bool:
        if phone[:3] in codes_operators:
            return True
        return False
    if phone.isdigit():
        if len(phone) == 12:
            if phone[:2] == '38':
                return is_valid_operator(phone[2:])





