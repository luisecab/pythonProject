email1 = 'pawel.rubach@sgh.waw.pl'
email2 = '@sgh.waw.pl'
email3 = 'pawel@sgh.waw'
email4 = 'pawesgh.waw'
email5 = 'pawesgh.waw.@'
email6 = 'pawel@.pl'

email_list = [email1, email2, email3, email4, email5, email6]


def validate_email(email):
    # TODO - verify email ......
    #if email[-1] == '.' or email[-1] == '@':
    if email[-1] in ['.', '@']:
        return False
    #email[-1]

    return True

print(email1[-7])

for em in email_list:
    print('{}: {}'.format(em, validate_email(em)))

print(validate_email(email1))