# Theme Collection

Chrome, VS Code 등 앱별 독립 테마를 한 저장소에서 관리하기 위한 컬렉션

같은 테마를 여러 앱으로 변환하는 구조가 아니라 앱 아래에 서로 독립적인 테마를 배치하는 방식

## 구조

```text
theme-collection/
├── chrome/
│   └── <theme-id>/
├── vscode/
│   └── <theme-id>/
├── tools/
│   ├── chrome/
│   └── image-processing/
├── templates/
│   ├── chrome-theme/
│   └── vscode-theme/
└── dist/
```

## 현재 테마

| 앱 | 테마 | 버전 | 경로 |
| --- | --- | --- | --- |
| Chrome | BMO Pixel Night | 1.0.2 | `chrome/bmo-pixel-night` |

## Chrome 테마 검증

```bash
python3 tools/chrome/validate_theme.py chrome/bmo-pixel-night
```

검증과 ZIP 패키징은 Python 표준 라이브러리만 사용

이미지 리사이즈 도구를 사용할 때만 개발 의존성 설치 필요

```bash
python3 -m pip install -r requirements-dev.txt
```

## Chrome 테마 패키징

```bash
python3 tools/chrome/build_theme.py \
  chrome/bmo-pixel-night \
  --output dist/chrome/bmo-pixel-night-v1.0.2.zip
```

배포 파일은 `dist/`에 생성되며 Git 커밋 대상에서 제외

## 버전 및 태그 규칙

- 각 테마의 버전과 변경 이력은 해당 테마 폴더에서 독립 관리
- 릴리스 태그 형식은 `<app>-<theme-id>-v<version>` 사용
- 예시: `chrome-bmo-pixel-night-v1.0.2`

## 권리 및 배포

코드와 이미지의 권리 상태가 다를 수 있으므로 공개 전 [RIGHTS.md](RIGHTS.md) 확인 필요
