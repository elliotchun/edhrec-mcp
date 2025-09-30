from mcp.server.fastmcp import FastMCP
from api_provider import edhrec
import parser as parser

mcp = FastMCP("EDHREC MCP")

@mcp.tool()
def get_card_details(card_name: str):
	"""
	Get relevant information about any Magic: the Gathering card by using EDHREC.com.
	"""
	details = edhrec.get_card_details(parser.sanitize_card_name(card_name))
	return parser.parse_details(details)

@mcp.tool()
def get_card_combos(card_name: str):
	"""
	Get a list of the popular combos included in decks that use {card_name} as a commander from EDHREC.com.
	"""
	combos = edhrec.get_card_combos(parser.sanitize_card_name(card_name))['container']['json_dict']['cardlists']
	return [{
		'rank': combo['combo']['rank'],
		'results': combo['combo']['results'],
		'cards': [parser.parse_card(card) for card in combo['cardviews']],
		'prevalence': combo['combo']['percentage']
	} for combo in combos]

@mcp.tool()
def get_similar_commanders(card_name: str):
	"""
	Get commanders similar to {card_name} from EDHREC.com.
	"""
	similar = edhrec.get_commander_data(parser.sanitize_card_name(card_name))['similar']
	return [parser.parse_card(card) for card in similar]

@mcp.tool()
def get_commanders_average_deck(card_name: str):
	"""
	Get the average decklist for decks that use {card_name} as a commander from EDHREC.com.
	"""
	return edhrec.get_commanders_average_deck(parser.sanitize_card_name(card_name))['decklist']

@mcp.tool()
def get_new_cards(card_name: str):
	"""
	Get recently released cards that have a high inclusion rate in decks that use {card_name} as a commander from EDHREC.com.
	"""
	return [parser.parse_card_with_inclusion(card) for card in edhrec.get_new_cards(parser.sanitize_card_name(card_name))['New Cards']]

@mcp.tool()
def get_high_synergy_cards(card_name: str):
	"""
	Get cards with high synergy in decks that use {card_name} as a commander from EDHREC.com.
	Synergy is calculated as [% of decks including the card for decks using {card_name} as a commander] - [% of decks including the card for all decks it can be included in].
	"""
	return [parser.parse_card_with_inclusion(card) for card in edhrec.get_high_synergy_cards(parser.sanitize_card_name(card_name))['High Synergy Cards']]

@mcp.tool()
def get_top_cards(card_name: str):
	"""
	Get the cards with the highest rate of inclusion in decks that use {card_name} as a commander from EDHREC.com.
	Excludes game changers, new cards and high synergy cards.
	"""
	return [parser.parse_card_with_inclusion(card) for card in edhrec.get_top_cards(parser.sanitize_card_name(card_name))['Top Cards']]

@mcp.tool()
def get_top_creatures(card_name: str):
	"""
	Get the creatures with the highest rate of inclusion in decks that use {card_name} as a commander from EDHREC.com.
	Excludes game changers, new cards, high synergy cards, and cards that have a high rate of inclusion in decks that use {card_name} as a commander.
	"""
	return [parser.parse_card_with_inclusion(card) for card in edhrec.get_top_creatures(parser.sanitize_card_name(card_name))['Creatures']]

@mcp.tool()
def get_top_instants(card_name: str):
	"""
	Get the instants with the highest rate of inclusion in decks that use {card_name} as a commander from EDHREC.com.
	Excludes game changers, new cards, high synergy cards, and cards that have a high rate of inclusion in decks that use {card_name} as a commander.
	"""
	return [parser.parse_card_with_inclusion(card) for card in edhrec.get_top_instants(parser.sanitize_card_name(card_name))['Instants']]

@mcp.tool()
def get_top_sorceries(card_name: str):
	"""
	Get the sorceries with the highest rate of inclusion in decks that use {card_name} as a commander from EDHREC.com.
	Excludes game changers, new cards, high synergy cards, and cards that have a high rate of inclusion in decks that use {card_name} as a commander.
	"""
	return [parser.parse_card_with_inclusion(card) for card in edhrec.get_top_sorceries(parser.sanitize_card_name(card_name))['Sorceries']]

@mcp.tool()
def get_top_enchantments(card_name: str):
	"""
	Get the enchantments with the highest rate of inclusion in decks that use {card_name} as a commander from EDHREC.com.
	Excludes game changers, new cards, high synergy cards, and cards that have a high rate of inclusion in decks that use {card_name} as a commander.
	"""
	return [parser.parse_card_with_inclusion(card) for card in edhrec.get_top_enchantments(parser.sanitize_card_name(card_name))['Enchantments']]

@mcp.tool()
def get_top_artifacts(card_name: str):
	"""
	Get the artifacts with the highest rate of inclusion in decks that use {card_name} as a commander from EDHREC.com.
	Excludes game changers, new cards, high synergy cards, mana-producing artifacts ("mana rocks") and cards that have a high rate of inclusion in decks that use {card_name} as a commander.
	"""
	return [parser.parse_card_with_inclusion(card) for card in edhrec.get_top_artifacts(parser.sanitize_card_name(card_name))['Artifacts']]

@mcp.tool()
def get_top_mana_artifacts(card_name: str):
	"""
	Get the mana-producing artifacts ("mana rocks") with the highest rate of inclusion in decks that use {card_name} as a commander from EDHREC.com.
	Excludes game changers, new cards, high synergy cards, and cards that have a high rate of inclusion in decks that use {card_name} as a commander.
	"""
	return [parser.parse_card_with_inclusion(card) for card in edhrec.get_top_mana_artifacts(parser.sanitize_card_name(card_name))['Mana Artifacts']]

@mcp.tool()
def get_top_battles(card_name: str):
	"""
	Get the battles with the highest rate of inclusion in decks that use {card_name} as a commander from EDHREC.com.
	Excludes game changers, new cards, high synergy cards, and cards that have a high rate of inclusion in decks that use {card_name} as a commander.
	"""
	return [parser.parse_card_with_inclusion(card) for card in edhrec.get_top_battles(parser.sanitize_card_name(card_name))['Battles']]

@mcp.tool()
def get_top_planeswalkers(card_name: str):
	"""
	Get the planeswalkers with the highest rate of inclusion in decks that use {card_name} as a commander from EDHREC.com.
	Excludes game changers, new cards, high synergy cards, and cards that have a high rate of inclusion in decks that use {card_name} as a commander.
	"""
	return [parser.parse_card_with_inclusion(card) for card in edhrec.get_top_planeswalkers(parser.sanitize_card_name(card_name))['Planeswalkers']]

@mcp.tool()
def get_top_utility_lands(card_name: str):
	"""
	Get the utility lands with the highest rate of inclusion in decks that use {card_name} as a commander from EDHREC.com.
	Excludes game changers, new cards, high synergy cards, and cards that have a high rate of inclusion in decks that use {card_name} as a commander.
	"""
	return [parser.parse_card_with_inclusion(card) for card in edhrec.get_top_utility_lands(parser.sanitize_card_name(card_name))['Utility Lands']]

@mcp.tool()
def get_top_lands(card_name: str):
	"""
	Get the lands with the highest rate of inclusion in decks that use {card_name} as a commander from EDHREC.com.
	Excludes game changers, new cards, high synergy cards, utility lands, and cards that have a high rate of inclusion in decks that use {card_name} as a commander.
	"""
	return [parser.parse_card_with_inclusion(card) for card in edhrec.get_top_lands(parser.sanitize_card_name(card_name))['Lands']]