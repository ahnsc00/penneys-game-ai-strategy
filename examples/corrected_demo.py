#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
올바른 페니의 게임 전략 시연 프로그램
검증된 콘웨이 규칙을 사용하는 대화형 프로그램
"""

import random
import sys
import os

# 부모 디렉토리의 src 모듈 import를 위한 경로 추가
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

try:
    from corrected_strategy import ConwaysOptimalStrategy
except ImportError:
    # 독립 실행을 위한 fallback
    class ConwaysOptimalStrategy:
        def __init__(self):
            self.optimal_strategy = {
                'HHH': 'THH', 'HHT': 'THH', 'HTH': 'HHT', 'HTT': 'HHT',
                'THH': 'TTH', 'THT': 'TTH', 'TTH': 'HTT', 'TTT': 'HTT'
            }
            self.verified_win_rates = {
                'HHH': 87.51, 'HHT': 74.94, 'HTH': 66.62, 'HTT': 66.75,
                'THH': 66.64, 'THT': 66.71, 'TTH': 74.97, 'TTT': 87.43
            }
        
        def get_optimal_response(self, seq):
            return self.optimal_strategy[seq]
        
        def get_expected_win_rate(self, seq):
            return self.verified_win_rates[seq]


def display_welcome():
    """환영 메시지"""
    print("="*70)
    print("🏆 올바른 페니의 게임 최적 전략 시연")
    print("="*70)
    print("✅ 검증된 콘웨이 규칙 (Conway's Rule)")
    print("📊 평균 승률 73.9% 보장")
    print("🔬 500만 번 시뮬레이션으로 검증됨")
    print("="*70)
    print()


def display_quick_reference():
    """빠른 참조표"""
    strategy = ConwaysOptimalStrategy()
    
    print("📋 빠른 참조표")
    print("-"*50)
    print("상대 → 나의선택  승률   성능등급")
    print("-"*50)
    
    for opponent in sorted(strategy.optimal_strategy.keys()):
        response = strategy.get_optimal_response(opponent)
        win_rate = strategy.get_expected_win_rate(opponent)
        
        if win_rate >= 85:
            grade = "🔥 최고"
        elif win_rate >= 75:
            grade = "💪 우수"
        else:
            grade = "👍 양호"
        
        print(f" {opponent} →  {response}   {win_rate:5.1f}%  {grade}")
    
    avg_rate = sum(strategy.verified_win_rates.values()) / 8
    print("-"*50)
    print(f"평균 승률: {avg_rate:.1f}%")
    print()


def explain_conway_rule():
    """콘웨이 규칙 설명"""
    print("🔑 콘웨이 규칙 설명")
    print("-"*30)
    print("📐 공식: 상대가 (A, B, C) 선택")
    print("       → 나는 (flip(B), A, B) 선택")
    print()
    print("🔄 flip 함수:")
    print("   flip(H) = T")
    print("   flip(T) = H")
    print()
    
    examples = [
        ("HHT", "H", "H", "T"),
        ("TTH", "T", "T", "H"),
        ("HTH", "H", "T", "H")
    ]
    
    print("📝 적용 예시:")
    for seq, A, B, C in examples:
        flip_B = 'T' if B == 'H' else 'H'
        result = flip_B + A + B
        print(f"   {seq}: ({A},{B},{C}) → (flip({B}),{A},{B}) = ({flip_B},{A},{B}) = {result}")
    print()


def interactive_session():
    """대화형 세션"""
    strategy = ConwaysOptimalStrategy()
    game_count = 0
    wins = 0
    
    print("🎮 대화형 전략 시연 시작!")
    print("💡 상대방의 3글자 배열을 입력하면 최적 응답을 알려드립니다.")
    print("💡 'help'로 도움말, 'quit'로 종료")
    print()
    
    while True:
        user_input = input("👤 상대방 선택 >> ").strip().upper()
        
        if user_input == 'QUIT':
            break
        elif user_input == 'HELP':
            explain_conway_rule()
            continue
        elif user_input == 'SCORE':
            if game_count > 0:
                print(f"📊 현재 기록: {wins}/{game_count} = {wins/game_count*100:.1f}%")
            else:
                print("📊 아직 게임 기록이 없습니다.")
            continue
        
        if len(user_input) != 3:
            print("❌ 3글자로 입력해주세요! (예: HHT, TTH)")
            continue
        
        if not all(c in 'HT' for c in user_input):
            print("❌ H(앞면) 또는 T(뒷면)만 사용하세요!")
            continue
        
        try:
            # 전략 적용
            response = strategy.get_optimal_response(user_input)
            win_rate = strategy.get_expected_win_rate(user_input)
            
            # 결과 출력
            print()
            print("🎯"*20)
            print(f"👤 상대방: {user_input}")
            print(f"🤖 최적응답: {response}")
            print(f"📊 예상승률: {win_rate:.1f}%")
            
            # 규칙 설명
            A, B, C = user_input[0], user_input[1], user_input[2]
            flip_B = 'T' if B == 'H' else 'H'
            print(f"⚙️  규칙: ({A},{B},{C}) → (flip({B}),{A},{B}) = ({flip_B},{A},{B})")
            
            # 승률별 메시지
            if win_rate >= 85:
                print("🔥 압도적 우위! 거의 확실한 승리입니다!")
            elif win_rate >= 75:
                print("💪 높은 승률! 자신있게 승부하세요!")
            else:
                print("👍 안정적 우위! 여전히 우리가 유리합니다!")
            
            print("🎯"*20)
            
            # 실제 게임 시뮬레이션 (선택사항)
            print("\n실제 게임을 시뮬레이션해볼까요? (y/n)")
            if input().strip().lower() == 'y':
                # 간단한 게임 시뮬레이션
                game_count += 1
                simulated_win = random.random() * 100 < win_rate
                
                if simulated_win:
                    wins += 1
                    print("🏆 승리! 예상대로입니다!")
                else:
                    print("😅 이번엔 졌지만, 장기적으로는 우리가 유리해요!")
                
                print(f"📊 현재 기록: {wins}/{game_count} = {wins/game_count*100:.1f}%")
            
        except Exception as e:
            print(f"❌ 오류: {e}")
        
        print("\n" + "-"*50)
    
    # 세션 종료
    if game_count > 0:
        final_rate = wins / game_count * 100
        print(f"\n🎯 최종 기록: {wins}/{game_count} = {final_rate:.1f}%")
        
        if final_rate >= 70:
            print("🎉 예상대로 높은 승률을 달성했습니다!")
        elif final_rate >= 50:
            print("👍 양호한 성과입니다. 더 많은 게임에서 진가를 발휘할 것입니다!")
        else:
            print("📊 단기적 변동입니다. 장기적으로는 73.9% 승률이 보장됩니다!")
    
    print("\n🏆 콘웨이 규칙으로 승리하세요! 👋")


def demo_mode_selection():
    """데모 모드 선택"""
    while True:
        print("🎮 모드를 선택하세요:")
        print("1. 빠른 참조표 보기")
        print("2. 콘웨이 규칙 설명")  
        print("3. 대화형 전략 시연")
        print("4. 종료")
        
        choice = input("\n선택 (1-4) >> ").strip()
        
        if choice == '1':
            display_quick_reference()
        elif choice == '2':
            explain_conway_rule()
        elif choice == '3':
            interactive_session()
        elif choice == '4':
            print("\n👋 페니의 게임에서 승리하세요!")
            break
        else:
            print("❌ 1-4 중에서 선택해주세요!")
        
        print()


def main():
    """메인 함수"""
    display_welcome()
    demo_mode_selection()


if __name__ == "__main__":
    main()