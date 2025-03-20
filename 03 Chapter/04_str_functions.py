name = "Rockstar Hello"

print(len(name)) # Length of String

print(name.endswith("ar"))
print(name.startswith("Roc"))

Cap = name.upper()
print(Cap)

low = name.lower()
print(low)

new = low.title()
print(new)

new = low.capitalize() # Capital First Letter of First Word in String
print(new)

index = name.find("star") # Return Index Form where it found
print(index)

new = name.replace("Hello","Hey")
print(new)