# Made this script to know how many of the transcripts had at least one GO id, how many GO ids were retrived
# and creating a file with all of the GO ids.

# Retrieving the .tsv generated with hmmer2go with the transcript ids and GO ids
mainFile = open("table_with_GO_ids_per_transcript.tsv")
lines = mainFile.readlines()
mainFile.close()

# Declaring count and array variables
countGO = 0
arrayGO = []

# Looping through the file
for i in range(0, len(lines)):
    # Selecting the GO ids in the file
    goIds = lines[i].split("\t")
    goIds = goIds[1].strip()
    goIds = goIds.split(",")
    # Counting the first GO id and adding it to the array
    countGO += 1
    arrayGO.append(goIds[0])
    # Checking if there are multiple GO ids and then couting them and adding it to the array
    if len(goIds) > 1:
        for j in range(1, len(goIds)):
            countGO += j
            arrayGO.append(goIds[j])

# Printing how many GO ids were retrieved
print("%i GO ids were retrieved from %i transcripts." % (countGO, len(lines)))

# Creating result file and writing the GO ids' array on it
resultFile = open("goIds.csv", "w")
resultFile.writelines(arrayGO)
resultFile.close()
