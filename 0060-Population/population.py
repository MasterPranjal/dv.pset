#The country A has 50M inhabitants, and its population grows 3% per year.
#The country B,70M and grows 2% per year. Tell in how many
#years A will surpass B.

country_A = 50000000
country_B = 70000000

growth = 0

def population(country_A, country_B):
    while(country_B >country_A):
        countryA = countryA + (countryA/100)*3
        countryB = countryB +(countryB/100)*2
        growth += 1

    print()
    
population(country_A, country_B)
