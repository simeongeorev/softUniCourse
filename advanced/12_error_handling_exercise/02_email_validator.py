class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


valid_domains = ["com", "bg", "net", "org"]

while (email := input()) != "End":
    # validate if email contains '@'
    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    name, domain = email.split("@")

    # validate the email's length
    if len(name) < 5:
        raise NameTooShortError("Name must be more than 4 characters")

    # extra check outside the task's description
    if "." not in domain:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    extension_domain = domain.split(".")[-1]

    # validate the email's domain
    if extension_domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    # print a valid email
    print("Email is valid")
