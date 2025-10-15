 # Life Expectancy Data Analysis Project
# By: Nkiru Madeleine Anagha


# Step 1: Ask user for a year
year_of_interest = input("Enter the year of interest: ")

# Step 2: Initialize tracking variables
overall_min = 9999
overall_max = 0
overall_min_country = ""
overall_max_country = ""
overall_min_year = ""
overall_max_year = ""

# Variables for user-specified year
year_total = 0
year_count = 0
year_min = 9999
year_max = 0
year_min_country = ""
year_max_country = ""


# Step 3: Open the file and read line by line
with open("life-expectancy.csv") as file:
    # This skips the header line
    next(file)  # Skip header line

    for line in file:
        parts = line.strip().split(",")
        country = parts[0]
        year = parts[2]
        life_expectancy = float(parts[3])


        # Track overall min and max
        if life_expectancy < overall_min:
            overall_min = life_expectancy
            overall_min_country = country
            overall_min_year = year

        if life_expectancy > overall_max:
            overall_max = life_expectancy
            overall_max_country = country
            overall_max_year = year


        # For the specific year entered by user
        if year == year_of_interest:
            year_total += life_expectancy
            year_count += 1

            if life_expectancy < year_min:
                year_min = life_expectancy
                year_min_country = country

            if life_expectancy > year_max:
                year_max = life_expectancy
                year_max_country = country


# Step 4: Display results
print(f"\nThe overall max life expectancy is: {overall_max:.3f} from {overall_max_country} in {overall_max_year}")
print(f"The overall min life expectancy is: {overall_min:.3f} from {overall_min_country} in {overall_min_year}")

if year_count > 0:
    year_average = year_total / year_count
    print(f"\nFor the year {year_of_interest}:")
    print(f"The average life expectancy across all countries was {year_average:.2f}")
    print(f"The max life expectancy was in {year_max_country} with {year_max:.3f}")
    print(f"The min life expectancy was in {year_min_country} with {year_min:.3f}")
else:
    print(f"\nNo data found for the year {year_of_interest}.")