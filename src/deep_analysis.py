def deep_analysis_of_discovered_strategy():
    """Deep analysis of the RL-discovered strategy"""
    
    decision_log = {
        'HHH': 'TTT',
        'HHT': 'THH', 
        'HTH': 'TTH',
        'HTT': 'HHT',
        'THH': 'TTH',
        'THT': 'TTH', 
        'TTH': 'HTT',
        'TTT': 'HTT'
    }
    
    print("=== DEEP ANALYSIS OF RL-DISCOVERED STRATEGY ===")
    print()
    
    # Let's look for any other patterns
    print("Looking for alternative patterns...")
    
    # Group by response to see if there are patterns
    response_groups = {}
    for opponent, response in decision_log.items():
        if response not in response_groups:
            response_groups[response] = []
        response_groups[response].append(opponent)
    
    print("Grouping by response:")
    for response, opponents in response_groups.items():
        print(f"  {response} <- {opponents}")
    
    print()
    
    # Let's analyze position by position
    print("Position-by-position analysis:")
    
    flip = lambda x: 'T' if x == 'H' else 'H'
    
    for i, (opponent, response) in enumerate(decision_log.items()):
        o1, o2, o3 = opponent[0], opponent[1], opponent[2]
        r1, r2, r3 = response[0], response[1], response[2]
        
        print(f"{opponent} -> {response}")
        print(f"  Position 1: {o1} -> {r1}")
        print(f"  Position 2: {o2} -> {r2}")  
        print(f"  Position 3: {o3} -> {r3}")
        
        # Check relationships
        relationships = []
        if r1 == flip(o1): relationships.append("r1=flip(o1)")
        if r1 == flip(o2): relationships.append("r1=flip(o2)")
        if r1 == flip(o3): relationships.append("r1=flip(o3)")
        if r1 == o1: relationships.append("r1=o1")
        if r1 == o2: relationships.append("r1=o2")
        if r1 == o3: relationships.append("r1=o3")
        
        if r2 == flip(o1): relationships.append("r2=flip(o1)")
        if r2 == flip(o2): relationships.append("r2=flip(o2)")
        if r2 == flip(o3): relationships.append("r2=flip(o3)")
        if r2 == o1: relationships.append("r2=o1")
        if r2 == o2: relationships.append("r2=o2")
        if r2 == o3: relationships.append("r2=o3")
        
        if r3 == flip(o1): relationships.append("r3=flip(o1)")
        if r3 == flip(o2): relationships.append("r3=flip(o2)")
        if r3 == flip(o3): relationships.append("r3=flip(o3)")
        if r3 == o1: relationships.append("r3=o1")
        if r3 == o2: relationships.append("r3=o2")
        if r3 == o3: relationships.append("r3=o3")
        
        print(f"  Relationships: {relationships}")
        print()

def manual_rule_discovery():
    """Manually try to discover the rule by looking at actual win probabilities"""
    
    print("=== MANUAL RULE DISCOVERY ===")
    
    decision_log = {
        'HHH': 'TTT',
        'HHT': 'THH', 
        'HTH': 'TTH',
        'HTT': 'HHT',
        'THH': 'TTH',
        'THT': 'TTH', 
        'TTH': 'HTT',
        'TTT': 'HTT'
    }
    
    # The RL discovered this strategy, let's see if we can find simpler patterns
    print("Observed mappings:")
    for opp, resp in decision_log.items():
        print(f"  {opp} -> {resp}")
    
    # Look for cases where TTH is the response
    print("\nCases where response is TTH:")
    tth_cases = [(opp, resp) for opp, resp in decision_log.items() if resp == 'TTH']
    for opp, resp in tth_cases:
        print(f"  {opp} -> {resp}")
        
    # Look for cases where response is HTT  
    print("\nCases where response is HTT:")
    htt_cases = [(opp, resp) for opp, resp in decision_log.items() if resp == 'HTT']
    for opp, resp in htt_cases:
        print(f"  {opp} -> {resp}")
        
    print("\nPossible simplified rule:")
    print("The RL agent seems to have discovered a mixed strategy that's different from Conway's rule.")
    print("It might be maximizing expected payoff rather than following a single deterministic rule.")

def final_pattern_attempt():
    """One final attempt to find the exact pattern"""
    
    decision_log = {
        'HHH': 'TTT',
        'HHT': 'THH', 
        'HTH': 'TTH',
        'HTT': 'HHT',
        'THH': 'TTH',
        'THT': 'TTH', 
        'TTH': 'HTT',
        'TTT': 'HTT'
    }
    
    print("=== FINAL PATTERN ANALYSIS ===")
    
    # Maybe the rule is more complex, let's see if we can describe it case by case
    flip = lambda x: 'T' if x == 'H' else 'H'
    
    rules = []
    
    for opponent, response in decision_log.items():
        o1, o2, o3 = opponent[0], opponent[1], opponent[2]
        
        # Try to find the simplest description for each case
        if opponent == 'HHH':
            rules.append(f"HHH -> TTT (flip all)")
        elif opponent == 'TTT': 
            rules.append(f"TTT -> HTT (not flip all, but special)")
        elif opponent == 'HHT':
            rules.append(f"HHT -> THH (Conway: flip(H) + H + H = T + H + H)")
        elif opponent == 'HTT':
            rules.append(f"HTT -> HHT (Conway: flip(T) + H + T = H + H + T)")  
        elif opponent == 'THH':
            rules.append(f"THH -> TTH (Conway: flip(H) + T + H = T + T + H)")
        elif opponent == 'TTH':
            rules.append(f"TTH -> HTT (Conway: flip(T) + T + T = H + T + T)")
        else:
            # These are the exceptions
            rules.append(f"{opponent} -> {response} (exception to Conway)")
    
    print("Rule breakdown:")
    for rule in rules:
        print(f"  {rule}")
    
    print(f"\nThe strategy appears to be:")
    print(f"1. Use Conway's rule for most cases: (flip(o2), o1, o2)")
    print(f"2. Special exceptions:")
    print(f"   - HHH -> TTT (complete flip)")
    print(f"   - TTT -> HTT (partial flip)")  
    print(f"   - HTH -> TTH (special XYX case)")
    print(f"   - THT -> TTH (same as above)")

if __name__ == "__main__":
    deep_analysis_of_discovered_strategy()
    manual_rule_discovery() 
    final_pattern_attempt()