def discover_complete_rule():
    """Discover the complete rule including special cases"""
    
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
    
    print("=== COMPLETE RULE DISCOVERY ===")
    
    flip = lambda x: 'T' if x == 'H' else 'H'
    
    # Analyze each case individually
    print("Analyzing each case:")
    
    rules_found = {}
    
    for opponent, response in decision_log.items():
        o1, o2, o3 = opponent[0], opponent[1], opponent[2]
        r1, r2, r3 = response[0], response[1], response[2]
        
        print(f"\n{opponent} -> {response}")
        
        # Check if it's a special case
        if o1 == o2 == o3:  # All same
            rules_found[opponent] = f"All same case: {opponent} -> flip all -> {response}"
            print(f"  Rule: All same coin -> flip all")
            
        elif o1 == o3:  # Pattern XYX
            # For XYX patterns, what's the rule?
            if opponent == 'HTH' and response == 'TTH':
                rules_found[opponent] = f"XYX pattern: Take YYflip(X) -> {response}"
                print(f"  Rule: For XYX, take YY + flip(X)")
            
        else:  # Normal Conway rule
            conway = flip(o2) + o1 + o2
            if response == conway:
                rules_found[opponent] = f"Conway rule: (flip({o2}), {o1}, {o2}) -> {response}"
                print(f"  Rule: Conway rule - (flip(middle), first, middle)")
            else:
                print(f"  Rule: Unknown - doesn't match Conway")
    
    print(f"\n=== TESTING COMPLETE RULE SET ===")
    
    def apply_complete_rule(opponent):
        """Apply the discovered complete rule"""
        o1, o2, o3 = opponent[0], opponent[1], opponent[2]
        
        if o1 == o2 == o3:  # All same coins
            return flip(o1) + flip(o2) + flip(o3)
        elif o1 == o3:  # XYX pattern
            return o2 + o2 + flip(o1)
        else:  # Conway rule
            return flip(o2) + o1 + o2
    
    correct_predictions = 0
    total = len(decision_log)
    
    for opponent, actual in decision_log.items():
        predicted = apply_complete_rule(opponent)
        correct = predicted == actual
        if correct:
            correct_predictions += 1
        
        print(f"{opponent} -> {actual} (predicted: {predicted}) {'✓' if correct else '✗'}")
    
    accuracy = correct_predictions / total
    print(f"\nComplete rule accuracy: {correct_predictions}/{total} = {accuracy:.1%}")
    
    return accuracy

def formulate_final_rules():
    """Formulate the final mathematical rules"""
    print("\n=== FINAL RULE FORMULATION ===")
    
    print("DISCOVERED OPTIMAL STRATEGY FOR PENNEY'S GAME:")
    print()
    print("Given opponent's sequence O = (o1, o2, o3), choose your sequence M = (m1, m2, m3) as follows:")
    print()
    print("Rule 1: If o1 = o2 = o3 (all same coin)")
    print("        M = (flip(o1), flip(o2), flip(o3)) = (flip(o1), flip(o1), flip(o1))")
    print("        Example: HHH -> TTT, TTT -> HHH")
    print()
    print("Rule 2: If o1 = o3 ≠ o2 (XYX pattern)")
    print("        M = (o2, o2, flip(o1))")
    print("        Example: HTH -> TTH")
    print()
    print("Rule 3: Otherwise (Conway's rule)")
    print("        M = (flip(o2), o1, o2)")
    print("        Example: HHT -> THH, TTH -> HTT")
    print()
    print("Where flip(H) = T and flip(T) = H")

if __name__ == "__main__":
    accuracy = discover_complete_rule()
    if accuracy == 1.0:
        formulate_final_rules()