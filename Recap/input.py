import sys

if len(sys.argv) == 2:
    print("Usage: Give both first name and last name.")
    sys.exit()

firstName = sys.argv[1]
lastName = sys.argv[2:]

mailId = firstName.lower().replace(" ", ".") + lastName.lower().replace(" ", ".") + "@companyName.mail.com"

print(f"Fullname: {firstName} {lastName}")
print("Generated mail Id: ", mailId)