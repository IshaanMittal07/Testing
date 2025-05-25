def analyze_situation(situation):
    evt_keywords = ["unexpected", "surprising", "violation", "shock", "broke the rule", "unusual"]
    mvt_keywords = ["rewarding", "punishment", "motivated", "discouraged", "goal", "effort", "positive", "negative"]

    evt_score = 0
    mvt_score = 0

    lower_situation = situation.lower()

    for word in evt_keywords:
        if word in lower_situation:
            evt_score += 1

    for word in mvt_keywords:
        if word in lower_situation:
            mvt_score += 1

    print("\n--- Analysis Result ---")
    print(f"EVT score: {evt_score}")
    print(f"MVT score: {mvt_score}")

    if evt_score > mvt_score:
        print("\nThis situation is best explained by **Expectancy Violation Theory (EVT)**.")
        print("Explanation: There is a violation of expectations or social norms, which triggers a reaction.")
    elif mvt_score > evt_score:
        print("\nThis situation is best explained by **Motivational Valence Theory (MVT)**.")
        print("Explanation: The focus is on how rewards or punishments affect motivation.")
    elif evt_score == 0 and mvt_score == 0:
        print("\nCould not detect strong elements of EVT or MVT. Please describe the situation more clearly.")
    else:
        print("\nBoth theories are relevant.")
        print("Explanation: The situation includes both an expectancy violation and motivational cues.")

# Example usage
if __name__ == "__main__":
    print("📘 EVT and MVT Analyzer")
    situation = input("Describe the situation: ")
    analyze_situation(situation)
