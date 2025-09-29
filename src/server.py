from mcp.server.fastmcp import FastMCP
from pyedhrec import EDHRec 

mcp = FastMCP("EDHREC MCP")
edhrec = EDHRec()

@mcp.tool()
def get_card_details(card_name: str):
    """
    Get relevant information about any Magic: the Gathering card by using EDHREC.com.
    """
    details = edhrec.get_card_details(card_name)
	
    return {
        'scryfall_id': details['id'],
        'name': details['name'],
        'mana_cost': details['mana_cost'],
        'type': details['type'],
        'oracle_text': details['oracle_text'],
        'legal_commander': details['legal_commander'],
        'is_banned': details['banned']
	}

@mcp.tool()
def get_card_combos(card_name: str):
    return edhrec.get_card_combos(card_name)

@mcp.tool()
def get_commander_data(card_name: str):
    return edhrec.get_commander_data(card_name)

@mcp.tool()
def get_commander_cards(card_name: str):
    return edhrec.get_commander_cards(card_name)

@mcp.tool()
def get_commanders_average_deck(card_name: str):
    return edhrec.get_commanders_average_deck(card_name)

@mcp.tool()
def get_commander_decks(card_name: str):
    return edhrec.get_commander_decks(card_name)

@mcp.tool()
def get_new_cards(card_name: str):
    return edhrec.get_new_cards(card_name)

@mcp.tool()
def get_high_synergy_cards(card_name: str):
    return edhrec.get_high_synergy_cards(card_name)

@mcp.tool()
def get_top_cards(card_name: str):
    return edhrec.get_top_cards(card_name)

@mcp.tool()
def get_top_creatures(card_name: str):
    return edhrec.get_top_creatures(card_name)

@mcp.tool()
def get_top_instants(card_name: str):
    return edhrec.get_top_instants(card_name)

@mcp.tool()
def get_top_sorceries(card_name: str):
    return edhrec.get_top_sorceries(card_name)

@mcp.tool()
def get_top_enchantments(card_name: str):
    return edhrec.get_top_enchantments(card_name)

@mcp.tool()
def get_top_artifacts(card_name: str):
    return edhrec.get_top_artifacts(card_name)

@mcp.tool()
def get_top_mana_artifacts(card_name: str):
    return edhrec.get_top_mana_artifacts(card_name)

@mcp.tool()
def get_top_battles(card_name: str):
    return edhrec.get_top_battles(card_name)

@mcp.tool()
def get_top_planeswalkers(card_name: str):
    return edhrec.get_top_planeswalkers(card_name)

@mcp.tool()
def get_top_utility_lands(card_name: str):
    return edhrec.get_top_utility_lands(card_name)

@mcp.tool()
def get_top_lands(card_name: str):
    return edhrec.get_top_lands(card_name)