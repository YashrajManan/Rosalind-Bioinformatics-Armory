with open("/mnt/d/Workspace/Python/BIOINFORMATICS_ARMORY/problem1data.txt", "r") as file: 
    dna = file.read().strip() 

freq = {
    "A":0,
    "T":0,
    "G":0,
    "C":0
}

for ch in dna: 
    freq[ch]+=1 

print(freq["A"], freq["C"], freq["G"], freq["T"])

