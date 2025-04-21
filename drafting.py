# Brawl Stars Drafting Guide - Power League Style
import random

# Define a basic map with top brawlers and typical bans
map_data = {
    "Canal Grande": {
        "mode": "Bounty",
        "top_brawlers": ["Piper", "Nani", "Tick", "Leon", "Bo"],
        "common_bans": ["Piper", "Tick"]
    },
    "Super Beach": {
        "mode": "Brawl Ball",
        "top_brawlers": ["Meg", "Janet", "Buster", "Surge", "Sam"],
        "common_bans": ["Buster", "Meg"]
    },
    "Layer Cake": {
        "mode": "Bounty",
        "top_brawlers": ["Brock", "Piper", "Nani", "Tick", "Mandy"],
        "common_bans": ["Piper", "Tick"]
    },
    # Add more maps as needed
}

# Counter & synergy database (super simplified)
counters = {
    "Piper": ["Leon", "Crow"],
    "Tick": ["Stu", "Buzz"],
    "Buster": ["Belle", "R-T"],
    "Sam": ["Spike", "Shelly"]
}

synergies = {
    "Piper": ["Bo"],
    "Sam": ["Buster"],
    "Janet": ["Bonnie"],
    "Surge": ["Max"]
}

def recommend_ban(map_name):
    return map_data[map_name]["common_bans"]

def suggest_top_brawlers(map_name):
    return map_data[map_name]["top_brawlers"]

def suggest_counter(brawler):
    return counters.get(brawler, ["No specific counter"])

def suggest_synergy(brawler):
    return synergies.get(brawler, ["No major synergy"])

def drafting_guide():
    print("📌 Brawl Stars Ranked Drafting Guide")
    map_name = input("Enter map name (e.g., 'Canal Grande'): ")

    if map_name not in map_data:
        print("❌ Map not found in database.")
        return

    print(f"\n🎮 Mode: {map_data[map_name]['mode']}")
    print(f"🔥 Suggested Bans: {', '.join(recommend_ban(map_name))}")
    print(f"✅ Top Brawlers: {', '.join(suggest_top_brawlers(map_name))}")

    your_team = []
    enemy_team = []

    # Simulate a draft phase
    while len(your_team) < 3 or len(enemy_team) < 3:
        if len(your_team) < 3:
            pick = input(f"\nYour Pick #{len(your_team)+1}: ")
            your_team.append(pick)
            print(f"💡 Synergy Picks for {pick}: {', '.join(suggest_synergy(pick))}")
        if len(enemy_team) < 3:
            pick = input(f"Enemy Pick #{len(enemy_team)+1}: ")
            enemy_team.append(pick)
            print(f"⚔️ Counter Picks for {pick}: {', '.join(suggest_counter(pick))}")

    print("\n📊 Final Teams:")
    print(f"Your Team: {', '.join(your_team)}")
    print(f"Enemy Team: {', '.join(enemy_team)}")

# Run the guide
if __name__ == "__main__":
    drafting_guide()
