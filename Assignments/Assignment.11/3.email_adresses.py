def get_names_and_domains(email_list):
    result_list = []
    for address in email_list:
        name, domain = address.split("@")
        result_list.append((name, domain))

    return result_list

def get_emails():
    email_list = []
    done = False
    while not done:
        email = input("Email adress: ")
        if email == "q":
            done = True
        else:
            email_list.append(email)

    return email_list
# Main program starts here - DO NOT change it

email_list = get_emails()
print(email_list)
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)