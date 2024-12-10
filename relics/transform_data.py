import json

# Load the Cavern Relic data
file_path = "./relics/data/cavern_relic_data.json"
with open(file_path, 'r') as file:
    cavern_relics_raw = json.load(file)

# Function to convert the raw bonuses text into structured data
def parse_bonuses(bonuses_text):
    effects = []
    lines = bonuses_text.split('\n')
    for line in lines:
        if line.startswith("2 Piece:"):
            effects.append({
                "description": line.replace("2 Piece: ", ""),
                "effects": []  # Actual effects need to be extracted later
            })
        elif line.startswith("4 Piece:"):
            effects.append({
                "description": line.replace("4 Piece: ", ""),
                "effects": []  # Actual effects need to be extracted later
            })
    return effects

# Transform the raw data
cavern_relics = {}
cavern_relics_bonus = {}
for relic in cavern_relics_raw:
    name_key = relic["name"].lower().replace(" ", "_")
    two_piece_bonus = parse_bonuses(relic["bonuses"])[0]
    four_piece_bonus = parse_bonuses(relic["bonuses"])[1]
    cavern_relics[name_key] = {
        "name": relic["name"],
        "set_icon_url": relic["iconurl"],
        "head_icon_url": relic["head"],
        "hands_icon_url": relic["hand"],
        "body_icon_url": relic["body"],
        "feet_icon_url": relic["feet"],
        "two_piece_bonus": two_piece_bonus,
        "four_piece_bonus": four_piece_bonus,
    }
    cavern_relics_bonus[name_key] = {
        "name": relic["name"],
        "two_piece_bonus": two_piece_bonus,
        "four_piece_bonus": four_piece_bonus,
    }

# Save the transformed data for review
output_path_relics = './relics/data/cavern_relics_transformed.json'
with open(output_path_relics, 'w') as file:
    json.dump(cavern_relics, file, indent=4)

# Save only the Bonus descriptions
output_path_bonus = './relics/data/cavern_relics_transformed_bonus.json'
with open(output_path_bonus, 'w') as file:
    json.dump(cavern_relics_bonus, file, indent=4)

print("done!")