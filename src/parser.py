def parse_card(card):
	return {
		'scryfall_id': card['id'],
		'name': card['name']
	}

def parse_details(card):
	return {
		'scryfall_id': card['id'],
		'name': card['name'],
		'mana_cost': card['mana_cost'],
		'type': card['type'],
		'oracle_text': card['oracle_text'],
		'legal_commander': card['legal_commander'],
		'is_banned': card['banned']
	}

def parse_card_with_inclusion(card):
	return {
		'scryfall_id': card['id'],
		'name': card['name'],
		'synergy': card['synergy'],
		'included_decks': card['num_decks'],
		'potential_decks': card['potential_decks'],
	}

def sanitize_card_name(card_name: str):
	return card_name.strip().replace('.', '')