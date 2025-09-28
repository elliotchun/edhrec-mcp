from mcp.server.fastmcp import FastMCP
from pyedhrec import EDHRec 

mcp = FastMCP("EDHREC MCP")
edhrec = EDHRec()

@mcp.tool()
def get_card_details(card_name: str):
    return edhrec.get_card_details(card_name)    

@mcp.tool()
def get_card_list(card_name: str):
    return edhrec.get_card_list(card_name)

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