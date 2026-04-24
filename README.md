# 🧩 PS (Problem Solving)
> 프로그래머스 문제풀이 저장소 — 자동 AI 코드 리뷰 시스템 포함

## 📌 소개
알고리즘 문제풀이 코드를 기록하고, **GitHub Actions + Groq AI**를 활용해 커밋 시 자동으로 코드 리뷰 Issue를 생성하는 저장소입니다.

## ⚙️ 자동 AI 리뷰 시스템

### 동작 흐름
```
코드 작성 (BaekjoonHub 자동 커밋)
    ↓
GitHub Actions 트리거 (main 브랜치 .py 파일 push)
    ↓
같은 디렉토리의 README.md 읽기 (문제 설명 + 제약 조건)
    ↓
Groq API (Llama 3.3 70B) → AI 코드 리뷰 생성
    ↓
GitHub Issue 자동 생성 (난이도 라벨 포함)
```

### AI 리뷰 항목
| 항목 | 내용 |
|------|------|
| 🔍 내 코드 알고리즘 | 제출 코드가 사용한 알고리즘/자료구조 한 줄 요약 |
| ✅ 최적 알고리즘 | 이 문제의 가장 효율적인 알고리즘 (내 코드와 비교) |
| 📊 복잡도 분석 | 실제 제한 대비 시간/공간 복잡도 ($O$ 표기법) |
| 🔧 개선할 수 있었던 부분 | 우선순위 기반 개선 제안 (내용 / 이유 / 동작 방식) |
| 💡 개선 적용 코드 | 개선 사항을 반영한 전체 파이썬 코드 |

### 개선 제안 우선순위
1. 시간복잡도 개선 (더 효율적인 알고리즘/자료구조로 대체 가능한 경우)
2. 파이썬 내장 자료구조 활용 (Counter, defaultdict, heapq 등)
3. 코드 간결성 (list comprehension 등)

### Issue 구성
- **제목**: `[날짜] AI 리뷰: 문제이름 (Lv.N)`
- **본문**: 제출 코드 + AI 분석 결과
- **라벨**: 난이도 (Lv.0~5)
- **댓글**: 복기 템플릿 자동 첨부

### 복기 템플릿
| 항목 | 내용 |
|------|------|
| 📝 풀이 | 핵심 로직을 독자에게 설명하듯 기록 |
| 🚧 막힌 부분 | 어디서 막혔고 어떻게 해결했는지 |
| 💡 리뷰 후 배운 점 | 내 코드와 개선 코드의 핵심 차이, 다음에 쓸 패턴 |

## 🗂️ 폴더 구조
```
PS/
├── .github/
│   └── workflows/
│       └── programmers-review.yml  # AI 자동 리뷰 워크플로우
└── 프로그래머스/
    └── {레벨}/
        └── {문제번호}. {문제이름}/
            ├── solution.py         # 풀이 코드 (BaekjoonHub 자동 커밋)
            └── README.md           # 문제 설명 + 제약 조건 (BaekjoonHub 자동 생성)
```

## 🚀 시작하기

### 사전 준비
1. **[BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub)** 크롬 익스텐션 설치 후 이 레포와 연동
2. **[Groq Console](https://console.groq.com)** 에서 API 키 발급 (무료, 신용카드 불필요)
3. GitHub 레포 Settings → Secrets에 아래 값 추가
```
GROQ_API_KEY=발급받은_API_키
```

### GitHub Actions 권한 설정
레포 Settings → Actions → General → Workflow permissions에서
**Read and write permissions** 활성화

### 수동 재실행
Actions 탭 → `Programmers Code Review` → `Run workflow` → 파일 경로 입력
```
예) 프로그래머스/2/131533. 상품 별 오프라인 매출 구하기/solution.py
```

## 🏷️ 난이도 라벨
프로그래머스 기준 난이도가 Issue 라벨로 자동 생성됩니다.

| 레벨 | 색상 |
|------|------|
| Lv.0 | `#c2e0c6` |
| Lv.1 | `#f9d0c4` |
| Lv.2 | `#fef2c0` |
| Lv.3 | `#d4c5f9` |
| Lv.4 | `#bfd4f2` |
| Lv.5 | `#c5def5` |

## 🛠️ 사용 기술
- **[BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub)** — 프로그래머스 제출 시 자동 커밋
- **[Groq API](https://console.groq.com)** — AI 코드 리뷰 생성 (Llama 3.3 70B, 무료)
- **GitHub Actions** — CI/CD 자동화
- **GitHub Issues** — 리뷰 결과 및 복기 기록
