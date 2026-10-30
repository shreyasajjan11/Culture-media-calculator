media={ 
    "nutrient broth" : 13.0,   #values on himedia product datasheet
    "nutrient agar" : 28.0,    #grams per litre
    "lb broth" : 25.0,
    }
mlperplate=20                   #approximate volume for 90mm mlperplate
def medium_g():
    print("Available media:",",".join(m.title() for m in media))   #asks the user for a medium and returns its name and g/lb
    while True:
        name=input("Which medium?").strip().lower()
        if name in media:
            return name, media[name]
        print("Medium not found. Try again")
def volume_g():
    while True:
        try:
            volume=float(input("Volume in ml:"))
            if volume>0:
                return volume
            print("Volume is greater than 0")
        except ValueError:
            print("Please enter a valid number.")
def calculate(gperl,volumeinml):
    grams=gperl*volumeinml/1000
    plates=volumeinml/mlperplate
    return grams,plates
def main():
    print("CULTURE MEDIA CALCULATOR")
    while True:
        name,gperl=medium_g()
        volume=volume_g()
        grams,plates=calculate(gperl,volume)
        print(f"\nWeigh {grams:.2f}g of {name.title()} powder.")
        print(f"Dissolve in {volume:.0f}ml distilled water and then autoclave")
        if "agar" in name:
            print(f"This pours about {plates:.0f} plates.")
            print()
        again=input("Calculate another? (yes or no):".strip().lower())
        if again!="yes":
            print("Done")
            break
main()
