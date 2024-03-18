import random

def flip_coins():
    """
    Flip three coins six times to determine the hexagram.
    Each flip can result in a value of 2 (heads) or 3 (tails).
    """
    flips = [sum(random.choices([2, 3], k=3)) for _ in range(6)]
    return flips

def determine_hexagram(flips):
    """
    Determine the hexagram based on the coin flips.
    Each flip total determines the type of line in the hexagram (6, 7, 8, 9).
    """
    hexagram_lines = []

    for flip in flips:
        if flip == 6:
            hexagram_lines.append('--- x ---')  # Old Yin
        elif flip == 7:
            hexagram_lines.append('---------')  # Young Yang
        elif flip == 8:
            hexagram_lines.append('---   ---')  # Young Yin
        elif flip == 9:
            hexagram_lines.append('--- o ---')  # Old Yang

    hexagram_number = calculate_hexagram_number(hexagram_lines)
    return hexagram_number, hexagram_lines

def calculate_hexagram_number(lines):
    """
    Calculate the hexagram number based on its lines.
    Each line is converted to a binary digit (0 for Yin, 1 for Yang), 
    and the resulting binary number is converted to decimal.
    """
    binary = ''.join(['0' if 'x' in line or ' ' in line else '1' for line in lines])
    return int(binary, 2)

def interpret_hexagram(number):
    """
    Provide a basic interpretation of the hexagram based on its number.
    This is a simplified interpretation.
    """
    interpretations = {
   1: "Hexagram 1 - The Creative: Symbolizes the force of creation, strong action, and leadership. It's a sign of success through strength and perseverance.",
    2: "Hexagram 2 - The Receptive: Represents earth, suggesting a time of receptiveness, nurturing, and support. Advises patience and care.",
    3: "Hexagram 3 - Difficulty at the Beginning: Indicates challenges when starting new ventures. It suggests the need for perseverance and preparation.",
    4: "Hexagram 4 - Youthful Folly: Implies inexperience and the need for guidance. It's a time for learning and seeking knowledge.",
    5: "Hexagram 5 - Waiting: Symbolizes a period of waiting or anticipation. Suggests the need for patience and readiness.",
    6: "Hexagram 6 - Conflict: Indicates a period of conflict or dispute. Advises caution in choosing battles and seeking resolution.",
    7: "Hexagram 7 - The Army: Represents organization and discipline. Suggests the need for order and structured leadership.",
    8: "Hexagram 8 - Holding Together: Emphasizes the importance of unity and alliances. Advises building trust and mutual support.",
    9: "Hexagram 9 - The Taming Power of the Small: Suggests influencing through gentle action. Small things can bring about change.",
    10: "Hexagram 10 - Treading: Indicates proceeding with caution. It's about carefully moving forward without provoking conflict.",
    11: "Hexagram 11 - Peace: Denotes a time of harmony and stability. Everything is in its proper place.",
    12: "Hexagram 12 - Standstill: Signifies a period of stagnation or lack of progress. Advises reassessment of situations.",
    13: "Hexagram 13 - Fellowship with Men: Stresses the importance of camaraderie and cooperation. It's about building harmonious relationships.",
    14: "Hexagram 14 - Possession in Great Measure: Signifies abundance and success. It's a time of great achievement and wealth.",
    15: "Hexagram 15 - Modesty: Advocates humility and modesty. Success comes through being grounded and unassuming.",
    16: "Hexagram 16 - Enthusiasm: Suggests the power of enthusiasm and motivation. It's a time to inspire others and take action.",
    17: "Hexagram 17 - Following: Implies a time to follow others or trends. Suggests adaptation and the willingness to be led.",
    18: "Hexagram 18 - Work on What Has Been Spoiled: Indicates a need to fix or rectify past mistakes. It's about healing and improvement.",
    19: "Hexagram 19 - Approach: Represents a time of gradual progress and advancement. Encourages approaching situations with care and tact.",
    20: "Hexagram 20 - Contemplation: Suggests a period for reflection and gaining perspective. It's about observing and understanding.",
    21: "Hexagram 21 - Biting Through: Indicates a need to confront issues directly. It's about overcoming obstacles through determination.",
    22: "Hexagram 22 - Grace: Focuses on beauty and outer appearances. Suggests the importance of aesthetics and elegance.",
    23: "Hexagram 23 - Splitting Apart: Signifies a time of breakdown or decline. It's a warning to let go of what no longer serves.",
    24: "Hexagram 24 - Return: Symbolizes a return or revival. It's about cycles, renewal, and coming back to your origins.",
    25: "Hexagram 25 - Innocence: Advocates for spontaneous, natural behavior. Suggests acting without ulterior motives.",
    26: "Hexagram 26 - The Taming Power of the Great: Represents controlled strength. Advises restraint and accumulating power wisely.",
    27: "Hexagram 27 - Nourishment: Focuses on seeking sustenance and nourishment, whether physical or spiritual. Advises being mindful of what you take in.",
    28: "Hexagram 28 - Preponderance of the Great: Indicates a situation of excess. Advises addressing imbalances and avoiding excesses.",
    29: "Hexagram 29 - The Abysmal: Symbolizes danger and challenge. Advises caution and persistence through difficult times.",
    30: "Hexagram 30 - The Clinging, Fire: Represents light, clarity, and dependence. Suggests holding on to what illuminates your life.",
    31: "Hexagram 31 - Influence: Suggests a period of attraction and persuasion. It's about influencing others gently.",
    32: "Hexagram 32 - Duration: Emphasizes the importance of perseverance and stability. It's about maintaining consistent effort.",
    33: "Hexagram 33 - Retreat: Advises a strategic withdrawal or stepping back. It's about knowing when to disengage.",
    34: "Hexagram 34 - The Power of the Great: Indicates great strength and determination. It's a time to assert yourself confidently.",
    35: "Hexagram 35 - Progress: Suggests gradual and steady advancement. It's a positive sign for growth and improvement.",
    36: "Hexagram 36 - Darkening of the Light: Indicates a period of obscurity or hardship. Advises protecting your inner light in difficult times.",
    37: "Hexagram 37 - The Family: Emphasizes family values and relationships. Suggests nurturing family ties and responsibilities.",
    38: "Hexagram 38 - Opposition: Highlights conflicts or differences. Advises finding common ground and resolving disagreements.",
    39: "Hexagram 39 - Obstruction: Suggests encountering obstacles. It's about facing challenges and finding alternative paths.",
    40: "Hexagram 40 - Deliverance: Indicates relief or liberation from difficulties. It's a time of resolving problems and finding freedom.",
    41: "Hexagram 41 - Decrease: Suggests a time of conservation and reduction. It's about prioritizing and letting go of the unnecessary.",
    42: "Hexagram 42 - Increase: Indicates growth and expansion. Advises seizing opportunities for development and abundance.",
    43: "Hexagram 43 - Breakthrough: Symbolizes a decisive action or breakthrough. It's about overcoming obstacles and making significant progress.",
    44: "Hexagram 44 - Coming to Meet: Implies an encounter, often with something or someone significant. Advises caution in dealings.",
    45: "Hexagram 45 - Gathering Together: Represents coming together for a common purpose. Suggests unity and collaboration.",
    46: "Hexagram 46 - Pushing Upward: Indicates upward movement or progress. It's about steady growth and effort.",
    47: "Hexagram 47 - Oppression: Suggests a time of hardship or restriction. Advises endurance and finding inner strength.",
    48: "Hexagram 48 - The Well: Symbolizes nourishment and replenishment. Advises drawing from deep resources and wisdom.",
    49: "Hexagram 49 - Revolution: Suggests major change or transformation. It's about upheaval and embracing new beginnings.",
    50: "Hexagram 50 - The Caldron: Represents nourishment and transformation. Suggests synthesizing elements to create something new.",
    51: "Hexagram 51 - The Arousing (Shock): Implies a sudden disturbance or awakening. Advises readiness for change and adapting quickly.",
    52: "Hexagram 52 - Keeping Still: Emphasizes stillness and meditation. Suggests pausing to reflect and finding clarity.",
    53: "Hexagram 53 - Development: Indicates gradual progress and growth. It's about moving forward with care and persistence.",
    54: "Hexagram 54 - The Marrying Maiden: Represents a situation of transition or subordination. Advises adapting to circumstances.",
    55: "Hexagram 55 - Abundance: Indicates a period of great abundance and prosperity. Advises enjoying success but remaining aware of potential decline.",
    56: "Hexagram 56 - The Wanderer: Suggests travel or transition. It's about being adaptable and self-reliant in changing circumstances.",
    57: "Hexagram 57 - The Gentle: Indicates gentle influence or persuasion. Suggests achieving goals through softness and persistence.",
    58: "Hexagram 58 - The Joyous: Symbolizes happiness and pleasure. Advises embracing joy and being open to pleasure.",
    59: "Hexagram 59 - Dispersion: Suggests dispersal or dissolving barriers. It's about spreading out and resolving separations.",
    60: "Hexagram 60 - Limitation: Indicates a need for setting limits or boundaries. Advises moderation and defining limits wisely.",
    61: "Hexagram 61 - Inner Truth: Emphasizes honesty and sincerity. Suggests acting from your inner truth and integrity.",
    62: "Hexagram 62 - Preponderance of the Small: Advises focusing on small matters. It's about attention to detail and not overreaching.",
    63: "Hexagram 63 - After Completion: Represents achievement or completion. Advises maintaining order and not becoming complacent.",
    64: "Hexagram 64 - Before Completion: Suggests being on the cusp of achievement."
    }
    return interpretations.get(number, "Interpretation not available.")

def get_opposite_hexagram(hexagram_number):
    # Represent contrasting but complementary energies or situations.
    binary = format(hexagram_number, '06b') 
    inverted_binary = ''.join(['1' if bit == '0' else '0' for bit in binary])
    opposite_number = int(inverted_binary, 2)
    return opposite_number

def get_nuclear_hexagram(hexagram_number):
    # Represents a deeper hidden core meaning of the original hexagram
    binary = format(hexagram_number, '06b')
    lower_nuclear = int(binary[1:4], 2)
    upper_nuclear = int(binary[2:], 2)
    return lower_nuclear, upper_nuclear

def get_mutual_hexagram(hexagram_number):
    # Represents a deeper connection between two hexagrams
    binary = format(hexagram_number, '06b')
    mutual_binary = binary[1:] + binary[0]
    mutual_number = int(mutual_binary, 2)
    return mutual_number

def get_hexagram_interpretation(hexagram_number):
    return interpret_hexagram(hexagram_number, "Interpretation not available.")

# Main execution
flips = flip_coins()
hexagram_number, hexagram_lines = determine_hexagram(flips)
interpretation = interpret_hexagram(hexagram_number)

print(f"Hexagram Number: {hexagram_number}")
print("Hexagram Lines:")
for line in hexagram_lines:
    print(line)
print("Interpretation:")
print(interpretation)
