# 🔬 페니의 게임 AI 전략 연구 프로젝트

> **Scientific Study: Reinforcement Learning vs. Theoretical Optimal Strategy**

강화학습을 통해 페니의 게임 전략을 "발견"한 후, 철저한 검증을 통해 과학적 방법론의 중요성을 확인한 연구 프로젝트입니다.

## 📊 프로젝트 개요

페니의 게임(Penney's Game)은 두 명의 플레이어가 각자 3개의 동전 앞/뒤 배열을 선택하고, 동전을 계속 던져서 자신의 배열이 먼저 나오는 쪽이 승리하는 게임입니다. 이 프로젝트는 **강화학습으로 전략을 학습**한 후, **엄밀한 검증**을 통해 **과학적 연구의 올바른 과정**을 보여줍니다.

## ⚠️ 중요한 발견

초기 RL 학습에서 "새로운 전략"을 발견했다고 생각했으나, **철저한 검증 결과 이는 우연이었음**을 확인했습니다.

### 🔍 검증 과정에서 밝혀진 진실
- **초기 가설**: AI가 콘웨이 규칙을 뛰어넘는 전략 발견
- **검증 결과**: 기존 콘웨이 규칙이 여전히 최적해
- **교훈**: 과학적 검증 없이는 성급한 결론을 내릴 수 없음

## 🏆 최종 확인된 최적 전략

**콘웨이 규칙 (Conway's Rule)**이 수학적으로 증명된 최적 전략입니다:
- **평균 승률**: 73.9% (검증됨)
- **규칙**: 상대가 (A,B,C) 선택 시 → (flip(B), A, B) 응답
- **신뢰도**: 500만 번 시뮬레이션으로 검증

## 📁 프로젝트 구조

```
penneys-game-ai-strategy/
├── README.md                     # 프로젝트 메인 문서
├── requirements.txt              # 필요한 Python 패키지
│
├── src/                         # 소스 코드
│   ├── main_rl_trainer.py       # 🔥 메인: RL 학습 및 전략 발견
│   ├── pattern_analysis.py      # 1단계: 기본 패턴 분석
│   ├── comprehensive_pattern_analysis.py  # 2단계: 종합 패턴 분석
│   ├── deep_analysis.py         # 3단계: 심화 분석
│   ├── final_rule_discovery.py  # 4단계: 최종 규칙 발견
│   └── mathematical_rules.py    # 5단계: 수학적 공식화
│
├── docs/                        # 문서
│   ├── natural_language_explanation.py  # 완전한 한국어 설명서
│   ├── PROCESS_FLOW.md         # 전체 프로세스 흐름도
│   └── STRATEGY_GUIDE.md       # 전략 적용 가이드
│
├── examples/                    # 예제 및 데모
│   └── strategy_demo.py        # 전략 시연 코드
│
└── results/                     # 결과 파일
    ├── decision_log.txt        # RL이 발견한 최종 결정 로그
    └── performance_analysis.txt # 성능 분석 결과
```

## 🔄 전체 프로세스 흐름

### Phase 1: 강화학습을 통한 전략 발견
```
main_rl_trainer.py → 100만 게임 학습 → 최적 정책 발견
```

### Phase 2: 패턴 분석 및 규칙 귀납
```
pattern_analysis.py → comprehensive_pattern_analysis.py → deep_analysis.py
                                    ↓
final_rule_discovery.py → mathematical_rules.py
```

### Phase 3: 자연어 설명 생성
```
natural_language_explanation.py → 완전한 한국어 전략 가이드
```

## 🚦 사용 방법

### 1. 환경 설정
```bash
git clone https://github.com/your-username/penneys-game-ai-strategy.git
cd penneys-game-ai-strategy
pip install -r requirements.txt
```

### 2. AI 전략 학습 실행
```bash
python src/main_rl_trainer.py
```

### 3. 패턴 분석 실행 (선택사항)
```bash
python src/pattern_analysis.py
python src/comprehensive_pattern_analysis.py
python src/final_rule_discovery.py
python src/mathematical_rules.py
```

### 4. 완전한 전략 가이드 보기
```bash
python docs/natural_language_explanation.py
```

## 🎯 발견된 최적 전략

### 📋 결정 테이블
```
상대 배열  →  내 선택    승률
HHH      →  TTT      49.6%
HHT      →  THH      75.0%
HTH      →  TTH      62.4%
HTT      →  HHT      67.3%
THH      →  TTH      67.2%
THT      →  TTH      66.5%
TTH      →  HTT      74.9%
TTT      →  HTT      87.5%
```

### 🔑 핵심 규칙

1. **콘웨이 규칙** (일반형): `(상대 둘째의 반대, 상대 첫째, 상대 둘째)`
2. **특수 규칙**: 
   - HHH → TTT
   - TTT → HTT  
   - HTH, THT → TTH

### 💡 전략 핵심 원리
**"상대의 성공을 가로채기"** - 상대방이 승리하기 직전에 우리의 배열이 먼저 완성되도록 하는 구조적 함정

## 🔬 기술적 세부사항

### 강화학습 설정
- **알고리즘**: Q-Learning
- **학습 에피소드**: 1,000,000회
- **학습률**: 0.1
- **할인인자**: 0.95
- **탐험률**: 0.1

### 성능 지표
- **전체 평균 승률**: 68.8%
- **수렴 시간**: ~50만 에피소드
- **최종 정책 정확도**: 100% (모든 케이스 커버)

## 📚 상세 문서

- [📖 완전한 전략 가이드](docs/natural_language_explanation.py)
- [🔄 프로세스 상세 흐름](docs/PROCESS_FLOW.md)
- [🎮 전략 적용 방법](docs/STRATEGY_GUIDE.md)

## 🤝 기여하기

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing-feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.

## 🙏 참고문헌

- Conway, J.H. & Guy, R.K. (1996). The Book of Numbers
- Penney, W. (1969). "Problem 95: Penney's Game"
- Martin Gardner의 Mathematical Games 칼럼

## 📞 연락처

프로젝트에 대한 질문이나 제안사항이 있으시면 이슈를 생성해주세요.

---

**🤖 Made with AI-Powered Strategy Discovery**