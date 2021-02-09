class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


def name_length_check(email):
    username = email.split('@')[0]
    if len(username) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")


def symbol_check(email):
    if '@' not in email:
        raise MustContainAtSymbolError('Email must contain @')


def domain_validator(email, valid_domains):
    domain = email.split('.')[1]
    if domain not in valid_domains:
        raise InvalidDomainError('"Domain must be one of the following: .com, .bg, .org, .net"')


while True:
    email = input()
    if email == 'End':
        break
    valid_domains = ('com', 'bg', 'org', 'net')
    name_length_check(email)
    symbol_check(email)
    domain_validator(email, valid_domains)

    print('Email is valid')



