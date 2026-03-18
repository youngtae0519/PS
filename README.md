# 🧩 PS (Problem Solving)

> 백준 문제풀이 저장소 — 자동 AI 코드 리뷰 시스템 포함

## 📌 소개

알고리즘 문제풀이 코드를 기록하고, **GitHub Actions + Gemini AI**를 활용해 커밋 시 자동으로 코드 리뷰 Issue를 생성하는 저장소입니다.

## ⚙️ 자동 AI 리뷰 시스템

### 동작 흐름

```
코드 작성 (BaekjoonHub 자동 커밋)
    ↓
GitHub Actions 트리거 (main 브랜치 .py 파일 push)
    ↓
Solved.ac API → 난이도 & 알고리즘 태그 조회
    ↓
BOJ 크롤링 → 시간/메모리 제한, 입력 제약 수집
    ↓
Gemini 2.5 Flash → AI 코드 리뷰 생성
    ↓
GitHub Issue 자동 생성 (티어 라벨 + 알고리즘 태그 포함)
```

### AI 리뷰 항목

| 항목 | 내용 |
|------|------|
| 📋 문제 요약 | 핵심 요구사항과 제약 조건 한 줄 요약 |
| 📊 복잡도 분석 | 실제 제한 대비 시간/공간 복잡도 ($O$ 표기법) |
| 🔧 개선할 점 | 성능 병목 지점 및 파이썬 최적화 기법 제안 |
| ⚠️ 반례 (Edge Case) | 실패 가능한 경계값 및 특수 상황 |

### Issue 구성

- **제목**: `[날짜] AI 리뷰: 문제번호.문제명`
- **본문**: 제출 코드 + Gemini AI 분석 결과
- **라벨**: Solved.ac 티어 (색상 자동 적용) + 알고리즘 분류 태그
- **댓글**: 복기 템플릿 자동 첨부 (핵심 로직 / 시행착오 / 새로 배운 팁)

## 🗂️ 폴더 구조

```
PS/
├── .github/
│   └── workflows/
│       └── ai_review.yml       # AI 자동 리뷰 워크플로우
└── {문제번호}.{문제명}/
    └── {문제번호}.py           # 풀이 코드 (BaekjoonHub 자동 커밋)
```

## 🚀 시작하기

### 사전 준비

1. **[BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub)** 크롬 익스텐션 설치 후 이 레포와 연동
2. **Google AI Studio**에서 Gemini API 키 발급
3. GitHub 레포 Settings → Secrets에 아래 값 추가

```
GEMINI_API_KEY=발급받은_API_키
```

### GitHub Actions 권한 설정

레포 Settings → Actions → General → Workflow permissions에서  
**Read and write permissions** 활성화

<br>

## 🏷️ 티어 라벨

Solved.ac 기준 난이도가 Issue 라벨로 자동 생성됩니다.

| 티어 | 색상 |
|------|------|
| 🟫 Bronze | `#ad5600` |
| 🩶 Silver | `#435f7a` |
| 🟡 Gold | `#ec9a00` |
| 🩵 Platinum | `#27e2a4` |
| 💎 Diamond | `#00b4fc` |
| 🔴 Ruby | `#ff0062` |

## 🛠️ 사용 기술

- **[BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub)** — 백준 제출 시 자동 커밋
- **[Solved.ac API](https://solvedac.github.io/unofficial-documentation/)** — 문제 난이도 및 태그 조회
- **[Gemini 2.5 Flash](https://ai.google.dev/)** — AI 코드 리뷰 생성
- **GitHub Actions** — CI/CD 자동화
- **GitHub Issues** — 리뷰 결과 기록
