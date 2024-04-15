text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO

print("".join([str(len(w.strip(",").strip("."))) for w in text.split()]))

