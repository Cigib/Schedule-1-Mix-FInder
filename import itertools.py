import itertools

customers = {
    "Austin Steiner": ["Calorie-Dense", "Euphoric", "Munchies"],
    "Beth Penn": ["Schizophrenic", "Lethal", "Seizure-Inducing"],
    "Chloe Bowers": ["Euphoric", "Shrinking", "Munchies"],
    "Donna Martin": ["Refreshing", "Lethal", "Munchies"],
    "Geraldine Poon": ["Balding", "Long Faced", "Sedating"],
    "Jessi Waters": ["Energizing", "Paranoia", "Sneaky"],
    "Kathy Henderson": ["Athletic", "Energizing", "Focused"],
    "Kyle Cooley": ["Calming", "Munchies", "Smelly"],
    "Ludwig Meyer": ["Euphoric", "Refreshing", "Energizing"],
    "Mick Lubbin": ["Euphoric", "Bright-Eyed", "Sneaky"],
    "Mrs. Ming": ["Gingeritis", "Shrinking", "Electrifying"],
    "Peggy Myers": ["Bright-Eyed", "Refreshing", "Energizing"],
    "Peter File": ["Focused", "Refreshing", "Sneaky"],
    "Sam Thompson": ["Munchies", "Athletic", "Smelly"],
    "Charles Rowland": ["Sedating", "Disorienting", "Foggy"],
    "Dean Webster": ["Glowing", "Laxative", "Spicy"],
    "Doris Lubbin": ["Spicy", "Tropic Thunder", "Balding"],
    "George Greene": ["Energizing", "Focused", "Thought-Provoking"],
    "Jerry Montero": ["Gingeritis", "Smelly", "Thought-Provoking"],
    "Joyce Ball": ["Euphoric", "Thought-Provoking", "Calorie-Dense"],
    "Keith Wagner": ["Slippery", "Sneaky", "Tropic Thunder"],
    "Kim Delaney": ["Shrinking", "Jennerising", "Focused"],
    "Meg Cooley": ["Sneaky", "Slippery", "Thought-Provoking"],
    "Trent Sherman": ["Athletic", "Balding", "Calorie-Dense"],
    "Elizabeth Homley": ["Sedating", "Tropic Thunder", "Toxic"],
    "Eugene Buckley": ["Schizophrenic", "Toxic", "Calming"],
    "Greg Figgle": ["Euphoric", "Tropic Thunder", "Toxic"],
    "Jeff Gilmore": ["Sedating", "Long Faced", "Laxative"],
    "Jennifer Rivera": ["Shrinking", "Slippery", "Toxic"],
    "Louis Fourier": ["Shrinking", "Seizure-Inducing", "Paranoia"],
    "Lucy Pennington": ["Calorie-Dense", "Euphoric", "Glowing"],
    "Philip Wentworth": ["Refreshing", "Shrinking", "Foggy"],
    "Anna Chesterfield": ["Refreshing", "Thought-Provoking", "Euphoric"],
    "Billy Kramer": ["Spicy", "Schizophrenic", "Long Faced"],
    "Cranky Frank": ["Laxative", "Toxic", "Tropic Thunder"],
    "Genghis Barn": ["Electrifying", "Gingeritis", "Athletic"],
    "Lisa Gardener": ["Laxative", "Schizophrenic", "Anti-Gravity"],
    "Mac Cooper": ["Focused", "Spicy", "Long Faced"],
    "Marco Barone": ["Sneaky", "Long Faced", "Refreshing"],
    "Melissa Wood": ["Anti-Gravity", "Refreshing", "Slippery"],
    "Carl Bundy": ["Glowing", "Athletic", "Disorienting"],
    "Chris Sullivan": ["Sneaky", "Euphoric", "Electrifying"],
    "Dennis Kennedy": ["Athletic", "Focused", "Bright-Eyed"],
    "Hank Stevenson": ["Sneaky", "Toxic", "Schizophrenic"],
    "Harold Colt": ["Foggy", "Spicy", "Jennerising"],
    "Jack Knight": ["Shrinking", "Thought-Provoking", "Lethal"],
    "Jeremy Wilkinson": ["Balding", "Slippery", "Calorie-Dense"],
    "Fiona Hancock": ["Lethal", "Thought-Provoking", "Tropic Thunder"],
    "Herbert Bleuball": ["Slippery", "Foggy", "Explosive"],
    "Jen Heard": ["Disorienting", "Energizing", "Sneaky"],
    "Michael Boog": ["Jennerising", "Calming", "Schizophrenic"],
    "Pearl Moore": ["Schizophrenic", "Gingeritis", "Explosive"],
    "Tobas Wentworth": ["Lethal", "Disorienting", "Spicy"],
    "Walter Cussler": ["Schizophrenic", "Calming", "Balding"]
}

replacement_rules = {
    "Cuke": {
        "Euphoric": "Laxative",
        "Foggy": "Cyclopean",
        "Gingeritis": "Thought-Provoking",
        "Munchies": "Athletic",
        "Slippery": "Munchies",
        "Sneaky": "Paranoia",
        "Toxic": "Euphoric"
    },
    "Flu Medicine": {
        "Athletic": "Munchies",
        "Calming": "Bright-Eyed",
        "Cyclopean": "Foggy",
        "Electrifying": "Refreshing",
        "Euphoric": "Toxic",
        "Focused": "Calming",
        "Laxative": "Euphoric",
        "Munchies": "Slippery",
        "Shrinking": "Paranoia",
        "Thought-Provoking": "Gingeritis"
    },
    "Gasoline": {
        "Disorienting": "Glowing",
        "Electrifying": "Disorienting",
        "Energizing": "Euphoric",
        "Euphoric": "Spicy",
        "Gingeritis": "Smelly",
        "Jennerising": "Sneaky",
        "Laxative": "Foggy",
        "Munchies": "Sedating",
        "Paranoia": "Calming",
        "Shrinking": "Focused",
        "Sneaky": "Tropic Thunder"
    },
    "Donut": {
        "Anti-Gravity": "Slippery",
        "Balding": "Sneaky",
        "Calorie-Dense": "Explosive",
        "Focused": "Euphoric",
        "Jennerising": "Gingeritis",
        "Munchies": "Calming",
        "Shrinking": "Energizing"
    },
    "Energy Drink": {
        "Disorienting": "Electrifying",
        "Euphoric": "Energizing",
        "Focused": "Shrinking",
        "Foggy": "Laxative",
        "Glowing": "Disorienting",
        "Schizophrenia": "Balding",
        "Sedating": "Munchies",
        "Spicy": "Euphoric",
        "Tropic Thunder": "Sneaky"
    },
    "Mouth Wash": {
        "Calming": "Anti-Gravity",
        "Calorie-Dense": "Sneaky",
        "Explosive": "Sedating",
        "Focused": "Jennerising"
    },
    "Motor Oil": {
        "Energizing": "Munchies",
        "Euphoric": "Sedating",
        "Foggy": "Toxic",
        "Munchies": "Schizophrenia",
        "Paranoia": "Anti-Gravity"
    },
    "Banana": {
        "Calming": "Sneaky",
        "Cyclopean": "Energizing",
        "Disorienting": "Focused",
        "Energizing": "Thought-Provoking",
        "Focused": "Seizure-Inducing",
        "Long Faced": "Refreshing",
        "Paranoia": "Jennerising",
        "Smelly": "Anti-Gravity",
        "Toxic": "Smelly"
    },
    "Chili": {
        "Anti-Gravity": "Tropic Thunder",
        "Athletic": "Euphoric",
        "Laxative": "Long Faced",
        "Munchies": "Toxic",
        "Shrinking": "Refreshing",
        "Sneaky": "Bright-Eyed"
    },
    "Iodine": {
        "Calming": "Balding",
        "Calorie-Dense": "Gingeritis",
        "Euphoric": "Seizure-Inducing",
        "Foggy": "Paranoia",
        "Refreshing": "Thought-Provoking",
        "Toxic": "Sneaky"
    },
    "Paracetamol": {
        "Calming": "Slippery",
        "Electrifying": "Athletic",
        "Energizing": "Paranoia",
        "Focused": "Gingeritis",
        "Foggy": "Calming",
        "Glowing": "Toxic",
        "Munchies": "Anti-Gravity",
        "Paranoia": "Balding",
        "Spicy": "Bright-Eyed",
        "Toxic": "Tropic Thunder"
    },
    "Viagra": {
        "Athletic": "Sneaky",
        "Disorienting": "Toxic",
        "Euphoric": "Bright-Eyed",
        "Laxative": "Calming",
        "Shrinking": "Gingeritis"
    },
    "Horse Semen": {
        "Anti-Gravity": "Calming",
        "Gingeritis": "Refreshing",
        "Seizure-Inducing": "Energizing",
        "Thought-Provoking": "Electrifying"
    },
    "Mega Bean": {
        "Athletic": "Laxative",
        "Calming": "Glowing",
        "Energizing": "Cyclopean",
        "Focused": "Disorienting",
        "Jennerising": "Paranoia",
        "Seizure-Inducing": "Focused",
        "Shrinking": "Electrifying",
        "Slippery": "Toxic",
        "Sneaky": "Calming",
        "Thought-Provoking": "Energizing"
    },
    "Addy": {
        "Explosive": "Euphoric",
        "Foggy": "Energizing",
        "Glowing": "Refreshing",
        "Long Faced": "Electrifying",
        "Sedating": "Gingeritis"
    },
    "Battery": {
        "Cyclopean": "Glowing",
        "Electrifying": "Euphoric",
        "Euphoric": "Zombifying",
        "Laxative": "Calorie-Dense",
        "Munchies": "Tropic Thunder",
        "Shrinking": "Munchies"
    }
}

# Weed strains native effects and prices (addictiveness ignored)
weed_strains = {
    "ogKush": {"price": 39, "native_effect": "Calming"},
    "sourDiesel": {"price": 40, "native_effect": "Refreshing"},
    "greenCrack": {"price": 43, "native_effect": "Energizing"},
    "granddaddyPurple": {"price": 44, "native_effect": "Sedating"}
}

# Other products base price
product_base_prices = {
    "meth": 70,
    "cocaine": 150
}

# Substance to trait mapping (exact substances & traits you provided)
substance_traits = {
    "Addy": "Thought-Provoking",
    "Banana": "Gingeritis",
    "Battery": "Bright-Eyed",
    "Chili": "Spicy",
    "Cuke": "Energizing",
    "Donut": "Calorie-Dense",
    "Energy Drink": "Athletic",
    "Flu Medicine": "Sedating",
    "Gasoline": "Toxic",
    "Horse Semen": "Long Faced",
    "Iodine": "Jennerising",
    "Mega Bean": "Foggy",
    "Motor Oil": "Slippery",
    "Mouthwash": "Balding",
    "Paracetamol": "Sneaky",
    "Viagra": "Tropic Thunder",
}

# Trait effect multipliers (your exact data)
trait_multipliers = {
    "Anti-Gravity": 0.54,
    "Athletic": 0.32,
    "Balding": 0.30,
    "Bright-Eyed": 0.40,
    "Calming": 0.10,
    "Calorie-Dense": 0.28,
    "Cyclopean": 0.56,
    "Disorienting": 0.00,
    "Electrifying": 0.50,
    "Energizing": 0.22,
    "Euphoric": 0.18,
    "Explosive": 0.00,
    "Focused": 0.16,
    "Foggy": 0.36,
    "Gingeritis": 0.20,
    "Glowing": 0.48,
    "Jennerising": 0.42,
    "Laxative": 0.00,
    "Long Faced": 0.52,
    "Munchies": 0.12,
    "Paranoia": 0.00,
    "Refreshing": 0.14,
    "Schizophrenia": 0.00,
    "Sedating": 0.26,
    "Seizure-Inducing": 0.00,
    "Shrinking": 0.60,
    "Slippery": 0.34,
    "Smelly": 0.00,
    "Sneaky": 0.24,
    "Spicy": 0.38,
    "Thought-Provoking": 0.44,
    "Toxic": 0.00,
    "Tropic Thunder": 0.46,
    "Zombifying": 0.58,
}

# Base prices for products (example prices)
product_base_prices = {
    "ogKush": 39,
    "sourDiesel": 40,
    "greenCrack": 43,
    "granddaddyPurple": 44,
    "meth": 70.0,
    "cocaine": 150.0,
}

# Control how many substances to select in heuristic
NUM_SUBSTANCES = 8
# Single line to select base product (change this to switch)
BASE_PRODUCT = "meth"  # options: ogKush, sourDiesel, greenCrack, granddaddyPurple, meth, cocaine
# Control how important coverage is compared to a higher sell price. value 0-100. 
# A value of zero means to ignore coverage and only go for a higher sell price. a value of 100 means to ignore sell price and focus on coverage
IMPORTANCE = 100


def apply_replacements(initial_effects, substances):
    current_effects = set(initial_effects)
    for substance in substances:
        if substance not in replacement_rules:
            continue
        rules = replacement_rules[substance]
        new_effects = set()
        for effect in current_effects:
            if effect in rules:
                new_effects.add(rules[effect])
            else:
                new_effects.add(effect)
        current_effects = new_effects
        if substance in substance_traits:
            current_effects.add(substance_traits[substance])
    return current_effects

def compute_final_price(base_product, substances):
    base_price = product_base_prices[base_product]
    initial_effects = set()
    if base_product in weed_strains:
        initial_effects.add(weed_strains[base_product]["native_effect"])
    final_effects = apply_replacements(initial_effects, substances)
    total_multiplier = sum(trait_multipliers.get(effect, 0) for effect in final_effects)
    final_price = base_price * (1 + total_multiplier)
    return final_price, final_effects

def coverage_score(effects):
    # Count how many customers have at least one preferred effect in the mix effects
    covered_customers = 0
    for prefs in customers.values():
        if any(effect in effects for effect in prefs):
            covered_customers += 1
    return covered_customers

# Main search loop
def find_best_mix(base_product, num_substances=NUM_SUBSTANCES, importance=IMPORTANCE):
    all_substances = list(substance_traits.keys())
    best_mix = None
    best_score = -1

    # Try all combinations of substances of given length
    for substances_combo in itertools.permutations(all_substances, num_substances):
        final_price, final_effects = compute_final_price(base_product, substances_combo)
        coverage = coverage_score(final_effects)

        # Weighted score (scale coverage to percentage, price normalized?)
        # For simplicity, scale coverage and price to comparable ranges:
        max_price = max(product_base_prices.values()) * 3  # rough max price guess
        price_score = final_price / max_price
        coverage_score_norm = coverage / len(customers)

        score = (importance / 100) * coverage_score_norm + ((100 - importance) / 100) * price_score

        if score > best_score:
            best_score = score
            best_mix = (substances_combo, final_price, final_effects, coverage)

    return best_mix, best_score

# Example usage
best_mix_result, best_mix_score = find_best_mix(BASE_PRODUCT, NUM_SUBSTANCES, IMPORTANCE)

if best_mix_result:
    substances_used, final_price, final_effects, coverage = best_mix_result
    print(f"Best mix substances in order: {substances_used}")
    print(f"Final price: ${final_price:.2f}")
    print(f"Final effects: {final_effects}")
    print(f"Customer coverage: {coverage} out of {len(customers)}")
    print(f"Combined score (importance-weighted): {best_mix_score:.4f}")
else:
    print("No mix found.")
