
print("Generation des pastilles 'Particularite'")
with open("runnerParticularites.py") as f:
    exec(f.read())

print("Generation des pastilles 'Enjeux'")
with open("runnerEnjeux.py") as f:
    exec(f.read())

print("Generation des images 'Point d'Intérêt'")
with open("runnerPointsOfInteret.py") as f:
    exec(f.read())

print("Generation des images 'Biomes'")
with open("runnerBiomes.py") as f:
    exec(f.read())

print("Generation des images 'Items'")
with open("runnerItems.py") as f:
    exec(f.read())

