import numpy as np
import random
from collections import defaultdict
import matplotlib.pyplot as plt

class PenneysGameEnvironment:
    def __init__(self):
        self.sequences = ['HHH', 'HHT', 'HTH', 'HTT', 'THH', 'THT', 'TTH', 'TTT']
        self.sequence_to_idx = {seq: i for i, seq in enumerate(self.sequences)}
        self.idx_to_sequence = {i: seq for i, seq in enumerate(self.sequences)}
        
    def simulate_game(self, seq1, seq2):
        """Simulate a single game between two sequences. Returns 1 if seq1 wins, 2 if seq2 wins."""
        if seq1 == seq2:
            return random.choice([1, 2])
        
        coin_sequence = ""
        while True:
            coin_sequence += random.choice(['H', 'T'])
            if len(coin_sequence) >= 3:
                recent = coin_sequence[-3:]
                if recent == seq1:
                    return 1
                elif recent == seq2:
                    return 2

class QLearningAgent:
    def __init__(self, learning_rate=0.1, discount_factor=0.95, epsilon=0.1):
        self.q_table = defaultdict(lambda: np.zeros(8))  # 8 possible actions (sequences)
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.sequences = ['HHH', 'HHT', 'HTH', 'HTT', 'THH', 'THT', 'TTH', 'TTT']
        
    def choose_action(self, state):
        """Choose action using epsilon-greedy policy"""
        if random.random() < self.epsilon:
            return random.randint(0, 7)  # Random action
        else:
            return np.argmax(self.q_table[state])  # Best action
    
    def update_q_table(self, state, action, reward):
        """Update Q-table based on experience"""
        self.q_table[state][action] += self.learning_rate * (reward - self.q_table[state][action])
    
    def get_best_action(self, state):
        """Get the best action for a given state (greedy)"""
        return np.argmax(self.q_table[state])

class PenneysRLTrainer:
    def __init__(self):
        self.env = PenneysGameEnvironment()
        self.agent = QLearningAgent()
        self.win_rates = []
        
    def train(self, episodes=1000000):
        """Train the agent for specified number of episodes"""
        wins = 0
        total_games = 0
        
        for episode in range(episodes):
            # Player 1 chooses random sequence
            player1_seq_idx = random.randint(0, 7)
            player1_seq = self.env.sequences[player1_seq_idx]
            
            # Agent (Player 2) chooses action based on Player 1's choice
            action = self.agent.choose_action(player1_seq_idx)
            player2_seq = self.env.sequences[action]
            
            # Simulate game
            winner = self.env.simulate_game(player1_seq, player2_seq)
            
            # Calculate reward
            reward = 1 if winner == 2 else -1
            if winner == 2:
                wins += 1
            total_games += 1
            
            # Update Q-table
            self.agent.update_q_table(player1_seq_idx, action, reward)
            
            # Track win rate every 10000 episodes
            if episode % 10000 == 0 and episode > 0:
                win_rate = wins / total_games
                self.win_rates.append(win_rate)
                print(f"Episode {episode}, Win Rate: {win_rate:.3f}")
                
                # Reset counters for next window
                wins = 0
                total_games = 0
                
        print("Training completed!")
    
    def evaluate_policy(self, test_games=100000):
        """Evaluate the learned policy"""
        wins = 0
        results = {}
        
        for player1_seq_idx in range(8):
            player1_seq = self.env.sequences[player1_seq_idx]
            seq_wins = 0
            
            for _ in range(test_games // 8):
                action = self.agent.get_best_action(player1_seq_idx)
                player2_seq = self.env.sequences[action]
                
                winner = self.env.simulate_game(player1_seq, player2_seq)
                if winner == 2:
                    seq_wins += 1
                    wins += 1
            
            win_rate = seq_wins / (test_games // 8)
            results[player1_seq] = {
                'best_response': self.env.sequences[action],
                'win_rate': win_rate
            }
        
        overall_win_rate = wins / test_games
        return results, overall_win_rate
    
    def get_decision_log(self):
        """Extract the final policy as a decision log"""
        decision_log = {}
        for player1_seq_idx in range(8):
            player1_seq = self.env.sequences[player1_seq_idx]
            best_action = self.agent.get_best_action(player1_seq_idx)
            player2_seq = self.env.sequences[best_action]
            decision_log[player1_seq] = player2_seq
        return decision_log

def main():
    print("Starting Penney's Game RL Training...")
    trainer = PenneysRLTrainer()
    
    # Train the agent
    trainer.train(episodes=1000000)
    
    # Evaluate the learned policy
    print("\nEvaluating learned policy...")
    results, overall_win_rate = trainer.evaluate_policy()
    
    print(f"\nOverall win rate: {overall_win_rate:.3f}")
    print("\nDetailed results:")
    for player1_seq, result in results.items():
        print(f"Against {player1_seq}: Choose {result['best_response']} (Win rate: {result['win_rate']:.3f})")
    
    # Get decision log
    decision_log = trainer.get_decision_log()
    print("\nDecision Log (Final Policy):")
    for opponent, response in decision_log.items():
        print(f"Input: {opponent} -> Output: {response}")
    
    return decision_log, results

if __name__ == "__main__":
    decision_log, results = main()