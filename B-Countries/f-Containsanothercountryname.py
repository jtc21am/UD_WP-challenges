'''Setting up storage to use during a for loop, including counters and arrays
There is at least one country name that contains another country name. Find all of these cases.'''
# We are comparing identical lists therefore I don't need to worry about upper/lower case (this is incorrect assumption)
# I will need to consider upper/lower -- case in point cat and Catskills

#create two variables to open the countries.txt file
#create an empty list to store the names which return True  -  modified to set to eliminate duplicates
#Create for loop to iterate through the names one by one (first variable)
#   Create a loop to iterate through the second variable
#     create an If statement to test whether the country name from the first variable is IN the second variable
#     AND if the country names do not match eachother
  
#     if True :Append the countrylist with the name of the country
#   reset 2nd country list to first element (seek method)
#print countrieslist


countries_file = open('countries.txt','r')
countries_file_2 = open('countries.txt','r')
country_container = set()

for country in countries_file:
    for country_2 in countries_file_2:
        if country.strip().upper() in country_2.strip().upper() and country != country_2:
            country_container.add(country.strip())
    countries_file_2.seek(0)

print(country_container)

# O(N**2)  -- N squared
countries_file.close()