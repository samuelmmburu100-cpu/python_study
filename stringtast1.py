name="JOhN."
clean_name=name.strip().lower()
print(clean_name) #->"john"

sentence_one="Breed is German Shepherd"
sentence_two="Clinton is in forces"
print(sentence_one[9:15]) #->"German"
print(sentence_two[9:16]) #->"Clinton"

data= "apple;banna;cherry"
parts=data.split(";")
print(len(parts)) #->3

first_name="john"
last_name="doe"
first_clean=first_name.strip().capitalize() #->"John"
last_clean=last_name.strip().capitalize() #->"Doe"
full_name=first_clean + " " + last_clean
print(full_name) #->"John Doe"

lettrs={"E", "W", "C"}
joined="..join(letters)"
print(joined) #->"EWC"
