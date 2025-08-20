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
├── README.md                     # 🌟 업데이트된 프로젝트 문서
├── LICENSE                       # MIT 라이선스
├── .gitignore                   # Git 제외 파일 목록
├── requirements.txt              # Python 의존성 (numpy, matplotlib, scipy)
│
├── src/                         # 🔬 핵심 소스 코드
│   ├── main_rl_trainer.py       # 🔥 초기 RL 학습 (문제 있던 버전)
│   ├── pattern_analysis.py      # 1단계: 기본 패턴 분석
│   ├── comprehensive_pattern_analysis.py  # 2단계: 종합 분석
│   ├── deep_analysis.py         # 3단계: 심화 분석
│   ├── final_rule_discovery.py  # 4단계: 최종 규칙 발견
│   ├── mathematical_rules.py    # 5단계: 수학적 공식화
│   ├── verification_study.py    # 🔬 검증 연구 (핵심!)
│   ├── deep_verification.py     # 🎯 결정적 검증
│   └── corrected_strategy.py    # ✅ 올바른 전략 구현
│
├── docs/                        # 📚 문서
│   ├── SCIENTIFIC_PROCESS.md    # 🔬 과학적 검증 과정
│   ├── LESSONS_LEARNED.md       # 📖 교훈과 통찰
│   ├── CORRECTED_STRATEGY.md    # ✅ 올바른 전략 가이드
│   ├── PROCESS_FLOW.md         # 전체 프로세스 흐름도
│   └── natural_language_explanation.py  # 한국어 설명서
│
├── examples/                    # 🎮 예제 및 데모
│   ├── corrected_demo.py       # ✅ 올바른 전략 시연
│   └── strategy_demo.py        # 🚫 원래 시연 (참고용)
│
└── results/                     # 📊 결과 파일
    ├── initial_findings.txt    # 🚫 초기 잘못된 결과
    ├── verification_results.txt # 🔬 검증 결과
    └── final_corrected_analysis.txt # ✅ 최종 올바른 분석
```

## 🔄 연구 과정 요약

### Phase 1: 초기 가설 (잘못됨)
```
main_rl_trainer.py → 100만 게임 학습 → "AI 독창적 전략 발견"
```

### Phase 2: 의심과 검증
```
verification_study.py → 재현성 테스트 → 일관성 부족 발견
deep_verification.py → 500만 시뮬레이션 → 콘웨이 규칙이 우수함 확인
```

### Phase 3: 과학적 결론
```
corrected_strategy.py → 올바른 구현 → 콘웨이 규칙 = 최적해
```

## 🎯 핵심 발견사항

### ❌ 초기 잘못된 결과
```
HHH → TTT  (50.0% 승률)
HTH → TTH  (62.4% 승률)
전체 평균: 68.8%
```

### ✅ 검증된 올바른 전략
```
HHH → THH  (87.5% 승률) 🔥
HTH → HHT  (66.6% 승률)
전체 평균: 73.9%
```

### 📊 성능 차이
- **콘웨이 규칙**: 73.9% (검증됨)
- **초기 AI 결과**: 68.8% (잘못됨)
- **성능 차이**: 5.1%p (상당한 차이!)

## 🔬 과학적 교훈

### 1. 재현성의 중요성
- 여러 번의 독립적 실험 필요
- 일관성 부족 시 의심해야 함

### 2. 충분한 검증
- 놀라운 결과일수록 더 엄밀한 검증
- 이론과의 체계적 비교 필수

### 3. 통계적 유의성
- 신뢰구간과 함께 결과 제시
- 충분한 샘플 수 확보

### 4. 겸손한 과학자 정신
- 틀릴 수 있음을 인정
- 검증을 통한 자기 수정

## 🚦 사용 방법

### 1. 환경 설정
```bash
git clone https://github.com/your-username/penneys-game-ai-strategy.git
cd penneys-game-ai-strategy
pip install -r requirements.txt
```

### 2. 올바른 전략 확인
```bash
python src/corrected_strategy.py
```

### 3. 검증 과정 재현
```bash
python src/verification_study.py
python src/deep_verification.py
```

### 4. 올바른 전략 시연
```bash
python examples/corrected_demo.py
```

## 🎯 올바른 페니의 게임 전략

### 📋 완전한 결정 테이블
```
상대 배열  →  내 선택    승률 (검증됨)
HHH      →  THH      87.5% 🔥 최고
HHT      →  THH      75.0% 
HTH      →  HHT      66.6%
HTT      →  HHT      66.8%
THH      →  TTH      66.6%
THT      →  TTH      66.7%
TTH      →  HTT      75.0%
TTT      →  HTT      87.4% 🔥 최고
```

### 🔑 콘웨이 규칙
**공식**: 상대가 (A, B, C) 선택 → 나는 (flip(B), A, B) 선택
- flip(H) = T, flip(T) = H

### 💡 핵심 원리
상대방의 성공 패턴을 가로채는 구조적 우위를 만드는 전략

## 🤝 기여하기

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/verification-improvement`)
3. Commit your changes (`git commit -m 'Add rigorous verification method'`)
4. Push to the branch (`git push origin feature/verification-improvement`)
5. Open a Pull Request

## 📚 상세 문서

- [🔬 과학적 검증 과정](docs/SCIENTIFIC_PROCESS.md)
- [📖 얻은 교훈들](docs/LESSONS_LEARNED.md)
- [✅ 올바른 전략 가이드](docs/CORRECTED_STRATEGY.md)
- [🔄 전체 프로세스 흐름](docs/PROCESS_FLOW.md)

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.

## 🙏 참고문헌

- Conway, J.H. & Guy, R.K. (1996). The Book of Numbers
- Penney, W. (1969). "Problem 95: Penney's Game"
- Martin Gardner's Mathematical Games Column
- Scientific Method and Reproducibility in AI Research

## 📞 연락처

이 연구에 대한 질문이나 개선 제안이 있으시면 이슈를 생성해주세요.

---

**🔬 과학적 검증의 중요성을 보여주는 사례 연구**

> "첫 번째 결과를 믿지 마라. 두 번째 결과도 의심하라. 세 번째 결과가 일관될 때 비로소 신뢰할 수 있다."