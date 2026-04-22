# GEMINI.md - BizTalk 프로젝트 컨텍스트

## 프로젝트 개요
**BizTalk**은 일상적이거나 격식이 없는 업무 메시지를 수신자(상사, 동료, 고객 등)에 맞춰 전문적이고 상황에 적합한 비즈니스 언어로 변환해주는 AI 기반 서비스입니다. 이 프로젝트는 입문 개발자가 AI 연동을 포함한 풀스택 개발 사이클을 학습할 수 있도록 설계된 "원데이(One Day) 프로젝트"입니다.

### 핵심 기술 스택
- **프론트엔드**: HTML5, CSS3, Vanilla JavaScript (프레임워크 없음)
- **백엔드**: Python 3.11+, FastAPI
- **AI 엔진**: Upstage Solar-Pro2 (LangChain 활용)
- **배포**: Vercel (프론트엔드), FastAPI (백엔드)

## 디렉토리 구조 (구현 예정)
```
biztalk-gemini-cli/
├── backend/                # FastAPI 서버 (구현 예정)
│   ├── main.py             # 엔트리 포인트
│   ├── services/           # AI 변환 로직
│   └── .env                # API 키 (보안 관리)
├── frontend/               # 정적 웹 파일 (구현 예정)
│   ├── index.html
│   ├── style.css
│   └── app.js
├── PRD_BizTalk.md          # 제품 요구사항 명세서 (PRD)
├── 개요서_업무말투변환기.md   # 프로그램 개요서
└── .gitignore              # Git 제외 규칙
```

## 빌드 및 실행 방법
현재 프로젝트는 기획 단계에 있으며, PRD를 바탕으로 추론된 실행 방법은 다음과 같습니다.

### 백엔드 (구현 예정)
1. **환경 설정**:
   ```bash
   cd backend
   pip install fastapi uvicorn langchain langchain-upstage python-dotenv
   ```
2. **서버 실행**:
   ```bash
   uvicorn main:app --reload --port 8000
   ```

### 프론트엔드 (구현 예정)
1. 브라우저에서 `frontend/index.html` 파일을 직접 열거나, VS Code의 Live Server와 같은 로컬 개발 서버를 사용합니다.

## 개발 컨벤션
- **수술적 업데이트(Surgical Updates)**: 항상 코드베이스를 간결하게 유지합니다.
- **AI 우선(AI-First)**: 핵심 변환 로직에는 Upstage Solar-Pro2 모델을 적극 활용합니다.
- **엄격한 환경 변수 관리**: `.env` 파일은 절대 Git에 커밋하지 않습니다.
- **페르소나 기반 프롬프트**: 수신자에 따라 AI가 특정 페르소나를 갖도록 합니다.
    - `boss`: 격식 있고 공손한 어조
    - `colleague`: 전문적이고 협조적인 어조
    - `client`: 친절하고 신뢰감을 주는 어조
    - `team`: 간결하고 실무적인 어조

## 사용 방법
이 디렉토리는 현재 프로젝트 요구사항 및 환경 설정의 표준 정보를 제공합니다. 실제 구현 단계에서는 `PRD_BizTalk.md`를 주요 가이드로 활용하십시오.

### Git Commit 와 Push를 반드시 확인을 받고 수행하세요. 임의로 Remote Repository에 Push 하면 절대로 안됨.

