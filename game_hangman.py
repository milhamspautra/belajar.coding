import random
bulan = ["Januari","Februari","Maret",
        "April","Mei","Juni","Juli",
        "Agustus","September","Oktober",
        "November","Desember"]
word = random.choice(bulan)
name = input("Please enter the players name? ")

print("Welcome to Hangman!")
print("I am thinking of a word that is 5 letters long")
print("You have 6 guesses left")

tebakan = ""
lanjut = True 
while lanjut :
    jawab=input("Please guess a letter: ") 
    if len(jawab)==1:
        if jawab in word :
            for letter in word :
                if jawab == letter :
                    print(jawab)
                    tebakan += letter
                    for letter in tebakan :
                        print(letter)
                else :
                    print("_")

