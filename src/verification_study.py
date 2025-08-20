import numpy as np
import random
from collections import defaultdict
import matplotlib.pyplot as plt

class PenneysGameVerification:
    """페니의 게임 전략 검증을 위한 클래스"""
    
    def __init__(self):
        self.sequences = ['HHH', 'HHT', 'HTH', 'HTT', 'THH', 'THT', 'TTH', 'TTT']
        
    def simulate_single_game(self, seq1, seq2):
        """단일 게임 시뮬레이션 (더 정확한 구현)"""
        if seq1 == seq2:
            return random.choice([1, 2])
        
        coin_sequence = ""
        max_length = 10000  # 무한 루프 방지
        
        for _ in range(max_length):
            coin_sequence += random.choice(['H', 'T'])
            if len(coin_sequence) >= 3:
                recent = coin_sequence[-3:]
                if recent == seq1:
                    return 1
                elif recent == seq2:
                    return 2
                    
                # 더 긴 패턴도 체크 (겹치는 경우)
                if len(coin_sequence) >= 4:
                    recent_4 = coin_sequence[-4:]
                    if recent_4[-3:] == seq1 and recent_4[:-1] != seq2:
                        return 1
                    elif recent_4[:-1] == seq2 and recent_4[-3:] != seq1:
                        return 2
        
        return random.choice([1, 2])  # 극히 드문 경우

class MultipleTrainingVerification:
    """여러 번의 독립적 RL 훈련을 통한 검증"""
    
    def __init__(self):
        self.env = PenneysGameVerification()
        
    def run_independent_training(self, episodes=100000):
        """독립적인 Q-러닝 훈련 실행"""
        q_table = defaultdict(lambda: np.zeros(8))
        learning_rate = 0.1
        epsilon = 0.1
        
        for episode in range(episodes):
            # 상태 (Player 1의 선택)
            state = random.randint(0, 7)
            player1_seq = self.env.sequences[state]
            
            # 행동 선택 (epsilon-greedy)
            if random.random() < epsilon:
                action = random.randint(0, 7)
            else:
                action = np.argmax(q_table[state])
            
            player2_seq = self.env.sequences[action]
            
            # 게임 시뮬레이션
            winner = self.env.simulate_single_game(player1_seq, player2_seq)
            reward = 1 if winner == 2 else -1
            
            # Q-테이블 업데이트
            q_table[state][action] += learning_rate * (reward - q_table[state][action])
        
        # 최종 정책 추출
        policy = {}
        for state in range(8):
            best_action = np.argmax(q_table[state])
            policy[self.env.sequences[state]] = self.env.sequences[best_action]
        
        return policy
    
    def verify_consistency(self, num_runs=5):
        """여러 번의 독립적 훈련으로 일관성 검증"""
        print("🔬 여러 번의 독립적 RL 훈련을 통한 검증")
        print("=" * 60)
        
        all_policies = []
        
        for run in range(num_runs):
            print(f"훈련 실행 {run+1}/{num_runs}...")
            policy = self.run_independent_training()
            all_policies.append(policy)
        
        # 일관성 분석
        print(f"\n📊 {num_runs}번 독립 훈련 결과 비교")
        print("-" * 60)
        print("상대 배열 |", end="")
        for i in range(num_runs):
            print(f" 훈련{i+1} |", end="")
        print(" 일관성")
        print("-" * 60)
        
        consistency_count = 0
        total_cases = len(self.env.sequences)
        
        for opponent in self.env.sequences:
            responses = [policy[opponent] for policy in all_policies]
            is_consistent = len(set(responses)) == 1
            
            print(f"   {opponent}   |", end="")
            for response in responses:
                print(f"  {response} |", end="")
            
            if is_consistent:
                print(" ✓ 일관됨")
                consistency_count += 1
            else:
                print(" ✗ 불일치")
        
        consistency_rate = consistency_count / total_cases * 100
        print("-" * 60)
        print(f"전체 일관성: {consistency_count}/{total_cases} = {consistency_rate:.1f}%")
        
        return all_policies, consistency_rate

class TheoreticalProbabilityAnalysis:
    """이론적 확률 분석"""
    
    def __init__(self):
        pass
    
    def calculate_exact_probability(self, seq1, seq2, num_simulations=1000000):
        """정확한 확률 계산 (대규모 시뮬레이션)"""
        if seq1 == seq2:
            return 0.5
        
        wins = 0
        env = PenneysGameVerification()
        
        for _ in range(num_simulations):
            winner = env.simulate_single_game(seq1, seq2)
            if winner == 2:  # seq2 승리
                wins += 1
        
        return wins / num_simulations
    
    def analyze_disputed_cases(self):
        """논란이 있는 케이스들에 대한 정밀 분석"""
        print("\n🎯 논란 케이스 정밀 확률 분석")
        print("=" * 50)
        
        # 논란이 있는 케이스들
        disputed_cases = [
            ('HHH', 'TTT'),  # AI 선택
            ('HHH', 'THH'),  # 콘웨이 선택
            ('HTH', 'TTH'),  # AI 선택  
            ('HTH', 'HHT'),  # 콘웨이 선택
        ]
        
        results = {}
        
        for seq1, seq2 in disputed_cases:
            print(f"\n분석 중: {seq1} vs {seq2}...")
            prob = self.calculate_exact_probability(seq1, seq2)
            results[(seq1, seq2)] = prob
            print(f"{seq1} vs {seq2}: {seq2} 승률 = {prob:.4f} ({prob*100:.2f}%)")
        
        print(f"\n🔍 HHH 케이스 비교:")
        ttt_prob = results[('HHH', 'TTT')]
        thh_prob = results[('HHH', 'THH')]
        print(f"  HHH vs TTT (AI): TTT 승률 = {ttt_prob:.4f} ({ttt_prob*100:.2f}%)")
        print(f"  HHH vs THH (콘웨이): THH 승률 = {thh_prob:.4f} ({thh_prob*100:.2f}%)")
        
        if thh_prob > ttt_prob:
            print(f"  🏆 결론: 콘웨이가 {(thh_prob-ttt_prob)*100:.2f}%p 더 우수!")
        else:
            print(f"  🏆 결론: AI가 {(ttt_prob-thh_prob)*100:.2f}%p 더 우수!")
        
        print(f"\n🔍 HTH 케이스 비교:")
        tth_prob = results[('HTH', 'TTH')]
        hht_prob = results[('HTH', 'HHT')]
        print(f"  HTH vs TTH (AI): TTH 승률 = {tth_prob:.4f} ({tth_prob*100:.2f}%)")
        print(f"  HTH vs HHT (콘웨이): HHT 승률 = {hht_prob:.4f} ({hht_prob*100:.2f}%)")
        
        if tth_prob > hht_prob:
            print(f"  🏆 결론: AI가 {(tth_prob-hht_prob)*100:.2f}%p 더 우수!")
        else:
            print(f"  🏆 결론: 콘웨이가 {(hht_prob-tth_prob)*100:.2f}%p 더 우수!")
        
        return results

class HeadToHeadTournament:
    """AI 전략 vs 콘웨이 전략 직접 대결"""
    
    def __init__(self):
        self.env = PenneysGameVerification()
        
        # AI 발견 전략
        self.ai_strategy = {
            'HHH': 'TTT', 'HHT': 'THH', 'HTH': 'TTH', 'HTT': 'HHT',
            'THH': 'TTH', 'THT': 'TTH', 'TTH': 'HTT', 'TTT': 'HTT'
        }
        
        # 순수 콘웨이 전략
        self.conway_strategy = {}
        for opponent in self.env.sequences:
            flip = lambda x: 'T' if x == 'H' else 'H'
            o1, o2, o3 = opponent[0], opponent[1], opponent[2]
            self.conway_strategy[opponent] = flip(o2) + o1 + o2
    
    def tournament(self, games_per_case=100000):
        """전면적 토너먼트"""
        print("\n⚔️  AI 전략 vs 콘웨이 전략 직접 대결")
        print("=" * 60)
        
        ai_total_wins = 0
        conway_total_wins = 0
        total_games = 0
        
        print("상대 선택 | AI 응답 | 콘웨이 응답 | AI 승률 | 콘웨이 승률 | 승자")
        print("-" * 70)
        
        for opponent in self.env.sequences:
            ai_response = self.ai_strategy[opponent]
            conway_response = self.conway_strategy[opponent]
            
            # AI 전략 테스트
            ai_wins = 0
            for _ in range(games_per_case):
                winner = self.env.simulate_single_game(opponent, ai_response)
                if winner == 2:
                    ai_wins += 1
            
            # 콘웨이 전략 테스트  
            conway_wins = 0
            for _ in range(games_per_case):
                winner = self.env.simulate_single_game(opponent, conway_response)
                if winner == 2:
                    conway_wins += 1
            
            ai_winrate = ai_wins / games_per_case
            conway_winrate = conway_wins / games_per_case
            
            ai_total_wins += ai_wins
            conway_total_wins += conway_wins
            total_games += games_per_case * 2
            
            # 승자 결정
            if ai_winrate > conway_winrate:
                winner_mark = "🔥 AI"
            elif conway_winrate > ai_winrate:
                winner_mark = "⭐ 콘웨이"
            else:
                winner_mark = "🤝 동점"
            
            print(f"   {opponent}   |  {ai_response}  |   {conway_response}   | {ai_winrate:.3f} | {conway_winrate:.3f} | {winner_mark}")
        
        # 전체 결과
        overall_ai = ai_total_wins / (games_per_case * len(self.env.sequences))
        overall_conway = conway_total_wins / (games_per_case * len(self.env.sequences))
        
        print("-" * 70)
        print(f"전체 평균 | {'':7} | {'':9} | {overall_ai:.3f} | {overall_conway:.3f} |", end="")
        
        if overall_ai > overall_conway:
            print(" 🏆 AI 승리!")
        elif overall_conway > overall_ai:
            print(" 🏆 콘웨이 승리!")
        else:
            print(" 🤝 동점!")
        
        return overall_ai, overall_conway

def main():
    """메인 검증 실행"""
    print("🔬 페니의 게임 AI 전략 철저 검증")
    print("=" * 80)
    
    # 1단계: 여러 번의 독립적 훈련으로 일관성 검증
    verification = MultipleTrainingVerification()
    policies, consistency = verification.verify_consistency(num_runs=3)
    
    # 2단계: 이론적 확률 분석
    theory_analysis = TheoreticalProbabilityAnalysis()
    probability_results = theory_analysis.analyze_disputed_cases()
    
    # 3단계: 직접 대결 토너먼트
    tournament = HeadToHeadTournament()
    ai_performance, conway_performance = tournament.tournament()
    
    # 최종 결론
    print(f"\n" + "🎯" * 30)
    print("🔬 최종 검증 결과")
    print("🎯" * 30)
    
    print(f"1️⃣  RL 훈련 일관성: {consistency:.1f}%")
    if consistency >= 80:
        print("   ✅ 높은 일관성 - AI 발견이 우연이 아님을 시사")
    else:
        print("   ⚠️  낮은 일관성 - 추가 검토 필요")
    
    print(f"2️⃣  이론적 확률 분석: 완료")
    print("   📊 정밀한 시뮬레이션으로 실제 승률 측정")
    
    print(f"3️⃣  직접 대결 결과:")
    print(f"   🤖 AI 전략 평균 승률: {ai_performance:.3f}")
    print(f"   📚 콘웨이 전략 평균 승률: {conway_performance:.3f}")
    
    if ai_performance > conway_performance:
        print("   🏆 결론: AI 전략이 실제로 더 우수함!")
    else:
        print("   🏆 결론: 콘웨이 전략이 더 우수함!")

if __name__ == "__main__":
    main()