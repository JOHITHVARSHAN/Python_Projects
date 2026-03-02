#extracting the string using split.
message = "Your booking id is: BI12345. Thank you for booking."
bookingId = message.split(":")[1].split(".")[0].strip()
print(bookingId)


#Finding stirng using if condition.
promoCode = "Use Promo100 to get flat 100 Rs off on your order."
if "Promo100" in promoCode:
    print("Offer Applied")


#finding position of the string
FeedBack = "The class was going good and the style of mentoring is awesome."
print("Position is: ", FeedBack.find("good"))


#Extracting specific letter form the word.
name = "johith varshan"
initial = " ".join([word[0].upper() for word in name.split()])
print(initial)