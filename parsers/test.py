import random

adjectives = [
    "Vibrant", "Pastel", "Bold", "Soft", "Dark", "Bright", "Muted", "Electric",
    "Radiant", "Shimmering", "Glowing", "Warm", "Cool", "Deep", "Light",
    "Neon", "Rich", "Subtle", "Dynamic", "Gentle", "Lively", "Mellow",
    "Polished", "Brilliant", "Graceful", "Elegant", "Harmonious", "Magical",
    "Frosty", "Fiery", "Luminous", "Whimsical", "Mystical", "Dazzling",
    "Ethereal", "Lustrous", "Saturated", "Glossy", "Matte", "Blazing",
    "Serene", "Vivid", "Aesthetic", "Lucid", "Delicate", "Intense",
    "Mysterious", "Opulent", "Resplendent", "Translucent"
]

color_words = [
    "Sunset", "Forest", "Ocean", "Sky", "Flame", "Blossom", "Moonlight", "Dusk",
    "Twilight", "Rainbow", "Coral", "Peach", "Amber", "Emerald", "Azure",
    "Lavender", "Crimson", "Teal", "Mint", "Berry", "Rose", "Ivory",
    "Scarlet", "Violet", "Citrine", "Fuchsia", "Magenta", "Turquoise",
    "Sapphire", "Amethyst", "Jade", "Ruby", "Topaz", "Copper", "Bronze",
    "Gold", "Silver", "Charcoal", "Slate", "Obsidian", "Onyx", "Pearl",
    "Garnet", "Peridot", "Aquamarine", "Opal", "Quartz", "Sand", "Clay"
]

nouns = [
    "Horizon", "Whisper", "Dream", "Mist", "Wave", "Garden", "Grove", "Field",
    "Breeze", "Aurora", "Glade", "Stream", "Canyon", "Meadow", "Shore",
    "Echo", "Peak", "Valley", "Cascade", "Glimmer", "Spring", "Oasis",
    "Thicket", "Brook", "Gulf", "Cove", "Lighthouse", "Crescent", "Starlight",
    "Eclipse", "Sunrise", "Harbor", "Basin", "Cliff", "Summit", "Pine",
    "Palm", "Bluff", "Vista", "Haven", "Glen", "Pond", "Marsh", "Prairie",
    "Wilderness", "Woodland", "Lagoon", "Reef", "Fen"
]

# Function to generate cool palette names
def generate_palette_name():
    adj = random.choice(adjectives)
    color = random.choice(color_words)
    noun = random.choice(nouns)
    return f"{adj}_{color}_{noun}"

# Generate multiple palette names
for _ in range(20):
    print(generate_palette_name())
