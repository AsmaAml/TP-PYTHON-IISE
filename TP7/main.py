import conversion
if __name__ == "__main__":
    dollars = 100
    dirhams = conversion.dollars_to_dirhams(dollars)
    print(f"{dollars} dollars = {dirhams} dirhams")

    meters = 1500
    kilometers = conversion.meters_to_kilometers(meters)
    print(f"{meters} mètres = {kilometers} kilomètres")
try : 
    conversion.dollars_to_dirhams(-233)
except ValueError :
    print("error")

try : 
    conversion.meters_to_kilometers(-23)
except ValueError :
    print("error")