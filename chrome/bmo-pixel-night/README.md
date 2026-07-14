# BMO Pixel Night

BMO에서 영감을 받아 제작한 비공식 2D 픽셀아트 Chrome 팬 테마

## 현재 버전

`1.0.2`

## 주요 설정

- 새 탭 배경 `2560×1440` RGB PNG
- 하단 중앙 정렬
- 배경 반복 없음
- 네이비 프레임과 BMO 민트 포인트 색상
- 매니페스트에 선언된 `128×128` 스토어 아이콘
- 스크립트, 권한, 데이터 수집 없음

## 폴더

- `assets/source`: 최초 생성 이미지
- `images`: Chrome 테마가 실제로 참조하는 이미지
- `store-assets`: 웹 스토어 아이콘, 캡처화면, 프로모션 타일
- `listing`: 웹 스토어 등록 문구

## 검증

저장소 루트에서 실행

```bash
python3 tools/chrome/validate_theme.py chrome/bmo-pixel-night
```

## 패키징

```bash
python3 tools/chrome/build_theme.py \
  chrome/bmo-pixel-night \
  --output dist/chrome/bmo-pixel-night-v1.0.2.zip
```

## 표시 제약

Chrome 웹 스토어 테마 배경은 브라우저에서 `size: initial`로 표시되므로 창 크기와 확대 수준에 따라 보이는 범위가 달라질 수 있음
