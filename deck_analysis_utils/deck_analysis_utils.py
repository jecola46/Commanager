def is_missing_shock(deck_collection, deck_id, colors):
    if "W" in colors and "U" in colors:
        if deck_collection.deck_does_not_have(deck_id, "Hallowed Fountain"):
            return True
    if "W" in colors and "B" in colors:
        if deck_collection.deck_does_not_have(deck_id, "Godless Shrine"):
            return True
    if "W" in colors and "R" in colors:
        if deck_collection.deck_does_not_have(deck_id, "Sacred Foundry"):
            return True
    if "W" in colors and "G" in colors:
        if deck_collection.deck_does_not_have(deck_id, "Temple Garden"):
            return True
    if "U" in colors and "B" in colors:
        if deck_collection.deck_does_not_have(deck_id, "Watery Grave"):
            return True
    if "U" in colors and "R" in colors:
        if deck_collection.deck_does_not_have(deck_id, "Steam Vents"):
            return True
    if "U" in colors and "G" in colors:
        if deck_collection.deck_does_not_have(deck_id, "Breeding Pool"):
            return True
    if "B" in colors and "R" in colors:
        if deck_collection.deck_does_not_have(deck_id, "Blood Crypt"):
            return True
    if "B" in colors and "G" in colors:
        if deck_collection.deck_does_not_have(deck_id, "Overgrown Tomb"):
            return True
    if "R" in colors and "G" in colors:
        if deck_collection.deck_does_not_have(deck_id, "Stomping Ground"):
            return True
    return False

def is_missing_command_tower(deck_collection, deck_id, colors):
    if len(colors) > 1 and deck_collection.deck_does_not_have(deck_id, "Command Tower"):
        return True

    return False