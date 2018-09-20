# This can be solved in a number of ways
# One way is to use one loop to generate one male and one female name and loop that twice (= 4 names)
length_of_surnames = len(SURNAMES)
length_of_females  = len(FEMALE_NAMES)
length_of_males    = len(MALE_NAMES)
for i in range(2):
    index_surname_male = random.randint(0, length_of_surnames)
    index_surname_female = random.randint(0, length_of_surnames)
    index_male    = random.randint(0, length_of_males)
    index_female  = random.randint(0, length_of_females)
    female_name = FEMALE_NAMES[index_female] + ' ' + SURNAMES[index_surname_female]
    male_name   = MALE_NAMES[index_male] + ' ' + SURNAMES[index_surname_male]
    print(female_name)
    print(male_name)    
    
# Another slightly smarter way is to use the random.choice method
for i in range(2):
    female_surname = random.choice(SURNAMES)
    female_name    = random.choice(FEMALE_NAMES)
    male_surname   = random.choice(SURNAMES)
    male_name      = random.choice(MALE_NAMES)
    female_name = female_name + ' ' + female_surname
    male_name   = male_name + ' ' + male_surname
    print(female_name)
    print(male_name)   
   
# And finally, you can randomize the gender, so you don't have to create two names per loop
for i in range(4):
    is_male = random.randint(0, 1)
    if is_male: # Male name
        first_name = random.choice(MALE_NAMES)
    else: # Female name
        first_name = random.choice(FEMALE_NAMES)
    surname = random.choice(SURNAMES)
    print(first_name + ' ' + surname)        
    
    
# Last, trick: The if statement can be written closer to the english "do this if male, otherwise do this"
# Now we're down to 5 lines of code!
for i in range(4):
    is_male = random.randint(0, 1)
    first_name = random.choice(MALE_NAMES) if is_male else random.choice(FEMALE_NAMES)
    surname = random.choice(SURNAMES)
    print(first_name + ' ' + surname) 