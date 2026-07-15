# 멀티 에이전트 구성

이 저장소는 공통 지침과 Agent Skills 표준을 중심으로 Codex, Claude Code, Google Antigravity를 함께 지원

## 지원 구조

| 도구 | 자동 로딩 지침 | 스킬 | 추가 구성 |
| --- | --- | --- | --- |
| Codex | `AGENTS.md` | `.agents/skills/theme-workflow/SKILL.md` | 저장소 지침의 상위·하위 범위 규칙 사용 |
| Claude Code | `CLAUDE.md` → `AGENTS.md` | `.claude/skills/theme-workflow/SKILL.md` | `.claude/settings.json`, `.claude/agents/theme-reviewer.md` |
| Antigravity | CLI의 `AGENTS.md`, IDE의 `.agents/rules/repository.md` → `AGENTS.md` | `.agents/skills/theme-workflow/SKILL.md` | `GEMINI.md` 라우팅, 워크플로와 사용자 정의 에이전트 |

## 단일 원본 원칙

- 저장소 공통 계약은 루트 `AGENTS.md`가 단일 원본
- `CLAUDE.md`와 `.agents/rules/repository.md`는 공통 계약을 가져오는 얇은 어댑터
- `GEMINI.md`는 CLI와 IDE 경로를 안내하며 중복 컨텍스트 방지를 위해 공통 계약을 다시 import하지 않음
- 공통 스킬 원본은 `.agents/skills/theme-workflow/SKILL.md`
- Claude Code 호환 복사본은 `.claude/skills/theme-workflow/SKILL.md`
- 현재 설치된 Claude Code가 `.agents/skills`를 프로젝트 스킬로 자동 탐색하지 않으므로 복사본 유지
- 심볼릭 링크 대신 저장소 검증기로 두 스킬 파일의 동일성을 보장해 운영체제와 Claude Code 버전 차이를 회피

## 제공 기능

- `theme-workflow`: 독립 테마 생성, 수정, 버전 동기화, 검증, 패키징, 릴리스 준비 절차
- `theme-reviewer`: 배포 전 검토 전용 에이전트. Claude Code에서는 `permissionMode: plan`으로 쓰기를 차단
- `/validate-theme`: Antigravity에서 호출하는 읽기 전용 검증 워크플로
- `.claude/settings.json`: 원격 Git 변경 재확인과 민감 경로에 대한 Claude `Read` 도구 차단 규칙

특정 모델 ID는 저장소에 고정하지 않음. Claude 검토 에이전트도 `model: inherit`를 사용해 실행 환경의 선택을 그대로 상속

Antigravity 사용자 정의 에이전트의 검토 전용 문구는 운영 계약이며 파일 자체가 프로젝트 권한을 강제하지는 않음. 실제 쓰기 차단이 필요한 검토는 Antigravity의 Planning 또는 Strict 권한 모드에서 실행 필요. 프로젝트 내부 쓰기는 기본 허용될 수 있으므로 프롬프트 지침만을 보안 경계로 간주하지 않음

Claude의 `Read(...)` deny도 Claude 파일 읽기 도구에 대한 규칙이며 모든 셸 명령을 차단하는 샌드박스는 아님. 민감 파일은 `.gitignore`로 Git 추적도 별도 차단

## 검증

에이전트 파일을 수정한 뒤 저장소 루트에서 실행

```bash
python3 tools/agents/validate_setup.py
```

검증 항목

- 모든 모델 진입 파일과 프로젝트 설정 존재 여부
- 어댑터의 `AGENTS.md` import와 실제 대상 경로
- 공통 스킬과 Claude 복사본의 바이트 단위 일치 여부
- 스킬과 사용자 정의 에이전트의 필수 frontmatter 값
- 두 검토 에이전트의 공통 본문과 Claude `plan` 권한
- Claude 프로젝트 설정 JSON 형식과 주요 안전 규칙
- `.gitignore`의 민감 파일 및 로컬 에이전트 상태 보호

설치된 CLI까지 확인하려면 smoke 검증 실행

```bash
python3 tools/agents/validate_setup.py --smoke
```

Smoke 검증은 설치된 Codex·Claude·Gemini CLI 버전을 확인하고, Gemini CLI가 저장소의 `theme-workflow` 스킬을 실제 발견하는지 검사

## 로컬 전용 설정

다음 파일은 개인 설정이므로 커밋하지 않음

- `CLAUDE.local.md`
- `.claude/settings.local.json`
- `.claude/agent-memory-local/`
- `.codex/` 또는 `.gemini/` 아래의 사용자 인증 정보와 로컬 상태

저장소에는 API 키, OAuth 토큰, 개인 MCP 인증, 모델별 개인 환경설정을 넣지 않음
