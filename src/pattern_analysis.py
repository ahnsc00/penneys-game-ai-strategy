def analyze_penney_strategy():
    """Analyze the patterns discovered by RL to find the underlying rule"""
    
    # Decision log from RL training
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
    
    print("=== PATTERN ANALYSIS ===")
    print("Decision Log:")
    for opponent, response in decision_log.items():
        print(f"  {opponent} -> {response}")
    
    print("\n=== DETAILED PATTERN ANALYSIS ===")
    
    # Let's analyze each mapping
    patterns = []
    for opponent, response in decision_log.items():
        o1, o2, o3 = opponent[0], opponent[1], opponent[2]
        r1, r2, r3 = response[0], response[1], response[2]
        
        # Check various potential patterns
        flip = lambda x: 'T' if x == 'H' else 'H'
        
        pattern_found = False
        
        # Pattern 1: (flip(o2), o1, o2)
        if r1 == flip(o2) and r2 == o1 and r3 == o2:
            patterns.append(f"{opponent} -> {response}: (flip({o2}), {o1}, {o2}) = ({r1}, {r2}, {r3})")
            pattern_found = True
        
        # Pattern 2: (flip(o3), o2, o3) 
        elif r1 == flip(o3) and r2 == o2 and r3 == o3:
            patterns.append(f"{opponent} -> {response}: (flip({o3}), {o2}, {o3}) = ({r1}, {r2}, {r3})")
            pattern_found = True
            
        # Pattern 3: (flip(o1), o2, o1)
        elif r1 == flip(o1) and r2 == o2 and r3 == o1:
            patterns.append(f"{opponent} -> {response}: (flip({o1}), {o2}, {o1}) = ({r1}, {r2}, {r3})")
            pattern_found = True
        
        if not pattern_found:
            patterns.append(f"{opponent} -> {response}: No clear pattern found")
    
    for pattern in patterns:
        print(f"  {pattern}")
    
    # Test the (flip(o2), o1, o2) pattern systematically
    print("\n=== TESTING PATTERN: (flip(o2), o1, o2) ===")
    pattern_matches = 0
    total = len(decision_log)
    
    for opponent, actual_response in decision_log.items():
        o1, o2, o3 = opponent[0], opponent[1], opponent[2]
        flip = lambda x: 'T' if x == 'H' else 'H'
        
        predicted_response = flip(o2) + o1 + o2
        
        if predicted_response == actual_response:
            print(f"  ✓ {opponent} -> {actual_response} (predicted: {predicted_response})")
            pattern_matches += 1
        else:
            print(f"  ✗ {opponent} -> {actual_response} (predicted: {predicted_response})")
    
    print(f"\nPattern match rate: {pattern_matches}/{total} = {pattern_matches/total:.1%}")
    
    if pattern_matches == total:
        print("\n🎉 PATTERN DISCOVERED!")
        print("RULE: My_sequence = (flip(opponent_2nd), opponent_1st, opponent_2nd)")
        print("Where flip(H) = T and flip(T) = H")
        return True
    
    return False

def verify_pattern_examples():
    """Verify the pattern with specific examples"""
    print("\n=== PATTERN VERIFICATION WITH EXAMPLES ===")
    
    examples = [
        ('HHT', 'THH'),
        ('TTH', 'HTT'), 
        ('HTH', 'TTH'),
        ('THT', 'TTH')
    ]
    
    for opponent, expected in examples:
        o1, o2, o3 = opponent[0], opponent[1], opponent[2]
        flip = lambda x: 'T' if x == 'H' else 'H'
        
        predicted = flip(o2) + o1 + o2
        
        print(f"Opponent: {opponent}")
        print(f"  1st: {o1}, 2nd: {o2}, 3rd: {o3}")
        print(f"  Rule application: (flip({o2}), {o1}, {o2}) = ({flip(o2)}, {o1}, {o2}) = {predicted}")
        print(f"  Expected: {expected}, Predicted: {predicted} {'✓' if predicted == expected else '✗'}")
        print()

if __name__ == "__main__":
    pattern_found = analyze_penney_strategy()
    if pattern_found:
        verify_pattern_examples()