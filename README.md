# 🔬 페니의 게임 AI 전략 연구

강화학습으로 전략을 "발견"했지만, 검증 결과 기존 콘웨이 규칙이 여전히 최적임을 확인한 연구.

## ⚠️ 핵심 발견

- **초기 가설**: AI가 콘웨이 규칙을 뛰어넘는 전략 발견
- **검증 결과**: 콘웨이 규칙이 여전히 최적 (73.9% vs 68.8%)
- **교훈**: 과학적 검증 없이는 성급한 결론 금물

## 🏆 검증된 최적 전략 (콘웨이 규칙)

상대가 (A,B,C) 선택 → 나는 (flip(B), A, B) 선택

```
상대 → 나의선택  승률
HHH → THH      87.5%
HHT → THH      75.0%
HTH → HHT      66.6%
HTT → HHT      66.8%
THH → TTH      66.6%
THT → TTH      66.7%
TTH → HTT      75.0%
TTT → HTT      87.4%

평균: 73.9%
```

## 🚦 사용법

```bash
git clone https://github.com/ahnsc00/penneys-game-ai-strategy.git
cd penneys-game-ai-strategy
pip install -r requirements.txt

# 올바른 전략 확인
python src/corrected_strategy.py

# 검증 과정 재현
python src/verification_study.py

# 대화형 시연
python examples/corrected_demo.py
```

## 📁 구조

```
src/
├── main_rl_trainer.py       # 초기 RL (문제 있던 버전)
├── verification_study.py    # 재현성 검증
├── deep_verification.py     # 500만 시뮬레이션 검증
└── corrected_strategy.py    # 올바른 전략

docs/
├── SCIENTIFIC_PROCESS.md    # 검증 과정
├── LESSONS_LEARNED.md       # 교훈
└── CORRECTED_STRATEGY.md    # 전략 가이드
```

## 🔬 검증 과정

1. **재현성 테스트**: 50% 일관성 → 신뢰성 부족 발견
2. **500만 시뮬레이션**: 정밀한 확률 계산
3. **직접 대결**: AI vs 콘웨이 전면 비교

### 주요 차이점

- **HHH 케이스**: AI 50.0% vs 콘웨이 87.5% (37.5%p 차이)
- **HTH 케이스**: AI 62.4% vs 콘웨이 66.6% (4.2%p 차이)

## 🎓 교훈

- 놀라운 결과일수록 더 엄격한 검증 필요
- 재현성이 과학의 기본
- 실패를 인정하고 수정하는 것이 진정한 과학

---

**과학적 검증의 중요성을 보여주는 교육적 사례**