
print("Generation des pastilles 'Particularite'")
with open("runnerParticularite.py") as f:
    exec(f.read())

print("Generation des pastilles 'Enjeux'")
with open("runnerEnjeu.py") as f:
    exec(f.read())

print("Generation des images 'Point d'Intérêt'")
with open("runnerPointOfInteret.py") as f:
    exec(f.read())

print("Generation des images 'Biomes'")
with open("runnerBiomes.py") as f:
    exec(f.read())

