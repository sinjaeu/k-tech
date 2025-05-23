# 학교 급식 메뉴 추천 및 잔반 예측 프로젝트

## 프로젝트 개요
이 프로젝트는 학교 급식 데이터를 기반으로 잔반량(남은 음식의 양)을 예측하고, 이를 바탕으로 30일치 급식 메뉴를 추천하는 시스템입니다. 머신러닝(CatBoost) 모델을 활용하여 결측된 잔반량을 예측하고, 예측 결과를 바탕으로 다양한 카테고리(밥, 국, 반찬, 김치, 후식)별로 균형 잡힌 급식 메뉴를 자동으로 생성합니다.

## 데이터 설명
- **main_data.csv**: 음식명(FOOD_NM), 재료(INGREDIENTS), 종류(TYPE), 잔반량(Quantity) 정보를 포함한 주요 데이터셋입니다. 일부 잔반량은 결측치로 존재하며, 모델을 통해 예측됩니다.
- **food1.csv ~ food6.csv, LOData1.csv ~ LOData5.csv, school_grad_1.csv ~ school_grad_3.csv 등**: 원본 데이터 및 전처리용 데이터 파일입니다.
- **main_data_filled.csv**: 결측치가 채워진 최종 데이터셋입니다.
- **menu_for_30_days.txt**: 추천된 30일치 급식 메뉴가 저장된 텍스트 파일입니다.

## 주요 코드 설명
- **main.py**: 
  - 데이터 전처리 및 탐색(결측치 분리, 시각화)
  - TF-IDF, One-hot encoding 등 피처 엔지니어링
  - CatBoostRegressor를 활용한 잔반량 예측 및 결측치 채우기
  - 예측 결과를 main_data_filled.csv로 저장

- **model.py**:
  - main_data_filled.csv를 불러와 음식 카테고리별로 분류
  - 잔반량이 적은 음식 위주로 30일치 급식 메뉴 추천
  - 추천 결과를 menu_for_30_days.txt로 저장

- **test.py**:
  - 원본 데이터 병합 및 전처리, main_data.csv 생성
  - 데이터 구조 및 병합 결과 확인

## 실행 방법
1. **필수 패키지 설치**
   ```bash
   pip install numpy pandas matplotlib seaborn scikit-learn catboost
   ```
2. **데이터 전처리 및 잔반 예측**
   ```bash
   python test.py   # main_data.csv 생성
   python main.py   # 결측치 예측 및 main_data_filled.csv 생성
   ```
3. **30일치 급식 메뉴 추천**
   ```bash
   python model.py  # menu_for_30_days.txt 생성
   ```

## 결과물 예시
menu_for_30_days.txt 파일에는 다음과 같이 30일치 추천 메뉴가 저장됩니다:

```
Day 1 Menu:
밥: 찰기장밥
김치: 깍두기
반찬: 삼색햄달걀말이, 코다리떡강정
국: 오징어무국
후식: 수박
...
```

## 파일 구조
- main.py: 잔반 예측 및 데이터 저장
- model.py: 메뉴 추천 및 결과 저장
- test.py: 데이터 병합 및 전처리
- *.csv: 데이터셋 파일
- menu_for_30_days.txt: 추천 메뉴 결과

## 참고 사항
- 데이터 파일(.csv)은 프로젝트 루트에 위치해야 하며, 파일명은 코드와 일치해야 합니다.
- CatBoost 설치가 필요하므로, 설치가 안 될 경우 공식 문서를 참고하세요.
- 데이터 및 결과 파일의 경로, 이름이 다를 경우 코드에서 직접 수정해 주세요.

## 문의
추가 문의사항은 프로젝트 관리자에게 연락 바랍니다. 
