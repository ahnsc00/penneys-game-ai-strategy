def comprehensive_pattern_analysis():
    """Comprehensive analysis to find the exact pattern"""
    
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
    
    print("=== COMPREHENSIVE PATTERN ANALYSIS ===")
    
    flip = lambda x: 'T' if x == 'H' else 'H'
    
    # Test multiple potential patterns
    patterns_to_test = [
        ("(flip(o2), o1, o2)", lambda o: flip(o[1]) + o[0] + o[1]),
        ("(flip(o3), o1, o2)", lambda o: flip(o[2]) + o[0] + o[1]),
        ("(flip(o1), o2, o3)", lambda o: flip(o[0]) + o[1] + o[2]),
        ("(o3, o1, flip(o2))", lambda o: o[2] + o[0] + flip(o[1])),
        ("(flip(o1), flip(o2), o1)", lambda o: flip(o[0]) + flip(o[1]) + o[0]),
        ("(flip(o2), flip(o1), o2)", lambda o: flip(o[1]) + flip(o[0]) + o[1]),
        ("Conway's rule: prepend flip(o2) to o1+o2", lambda o: flip(o[1]) + o[0] + o[1]),
    ]
    
    best_pattern = None
    best_score = 0
    
    for pattern_name, pattern_func in patterns_to_test:
        matches = 0
        total = len(decision_log)
        
        print(f"\nTesting pattern: {pattern_name}")
        for opponent, actual in decision_log.items():
            predicted = pattern_func(opponent)
            match = predicted == actual
            if match:
                matches += 1
            print(f"  {opponent} -> {actual} (predicted: {predicted}) {'✓' if match else '✗'}")
        
        score = matches / total
        print(f"  Score: {matches}/{total} = {score:.1%}")
        
        if score > best_score:
            best_score = score
            best_pattern = pattern_name
    
    print(f"\n=== BEST PATTERN FOUND ===")
    print(f"Pattern: {best_pattern}")
    print(f"Accuracy: {best_score:.1%}")
    
    # Let's also check for known theoretical optimal strategies
    print(f"\n=== CHECKING KNOWN OPTIMAL STRATEGIES ===")
    
    # Conway's strategy: Given opponent ABC, respond with (flip(B), A, B)
    print("Testing Conway's optimal strategy:")
    conway_matches = 0
    for opponent, actual in decision_log.items():
        A, B, C = opponent[0], opponent[1], opponent[2]
        conway_response = flip(B) + A + B
        match = conway_response == actual
        if match:
            conway_matches += 1
        print(f"  {opponent} -> {actual} (Conway: {conway_response}) {'✓' if match else '✗'}")
    
    conway_score = conway_matches / len(decision_log)
    print(f"Conway strategy accuracy: {conway_matches}/{len(decision_log)} = {conway_score:.1%}")
    
    return best_pattern, best_score

def analyze_exceptions():
    """Analyze cases that don't follow the main pattern"""
    print("\n=== ANALYZING EXCEPTIONS ===")
    
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
    
    flip = lambda x: 'T' if x == 'H' else 'H'
    
    exceptions = []
    for opponent, actual in decision_log.items():
        conway_prediction = flip(opponent[1]) + opponent[0] + opponent[1]
        if conway_prediction != actual:
            exceptions.append((opponent, actual, conway_prediction))
    
    print("Cases that don't follow Conway's rule:")
    for opponent, actual, predicted in exceptions:
        print(f"  {opponent}: actual={actual}, Conway={predicted}")
        
        # Analyze these special cases
        if opponent in ['HHH', 'TTT']:
            print(f"    -> {opponent} is all same coin, special case")
        elif opponent == 'HTH':
            print(f"    -> {opponent} has pattern XYX, might need different rule")

if __name__ == "__main__":
    best_pattern, score = comprehensive_pattern_analysis()
    analyze_exceptions()