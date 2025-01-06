import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import mean_squared_error
from catboost import CatBoostRegressor

# 데이터 로딩
main_data = pd.read_csv('main_data.csv')

# 데이터 탐색
print(main_data.head())
print(main_data.describe())
plt.figure(figsize=(12, 6))
sns.histplot(main_data['Quantity'].dropna(), kde=True)
plt.title('Distribution of Quantity')
plt.xlabel('Quantity')
plt.ylabel('Frequency')
plt.show()

# 결측치가 있는 데이터와 없는 데이터 나누기
data_with_quantity = main_data.dropna(subset=['Quantity'])
data_missing_quantity = main_data[main_data['Quantity'].isnull()]

# 특성 및 레이블 정의
X = data_with_quantity[['FOOD_NM', 'INGREDIENTS', 'TYPE']]
y = data_with_quantity['Quantity']
X_missing = data_missing_quantity[['FOOD_NM', 'INGREDIENTS', 'TYPE']]

# TF-IDF 벡터화
tfidf_vectorizer = TfidfVectorizer()
X_ingredients_tfidf = tfidf_vectorizer.fit_transform(data_with_quantity['INGREDIENTS'])
X_ingredients_tfidf_missing = tfidf_vectorizer.transform(data_missing_quantity['INGREDIENTS'])

# One-hot Encoding
X_food_type = pd.get_dummies(data_with_quantity[['FOOD_NM', 'TYPE']])
X_food_type_missing = pd.get_dummies(data_missing_quantity[['FOOD_NM', 'TYPE']])

# 결합
X = pd.concat([pd.DataFrame(X_ingredients_tfidf.toarray()), X_food_type.reset_index(drop=True)], axis=1)
X_missing = pd.concat([pd.DataFrame(X_ingredients_tfidf_missing.toarray()), X_food_type_missing.reset_index(drop=True)], axis=1)

# 피처 집합 일치시키기
X, X_missing = X.align(X_missing, join='left', axis=1, fill_value=0)

# 컬럼 이름을 문자열로 변환
X.columns = X.columns.astype(str)
X_missing.columns = X_missing.columns.astype(str)

# 스케일링
scaler = MinMaxScaler()
X = scaler.fit_transform(X)
X_missing = scaler.transform(X_missing)

# 레이블과 특성 데이터 나누기
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 최적의 하이퍼파라미터를 사용한 CatBoost 모델 설정
best_model_catboost = CatBoostRegressor(
    iterations=500,
    learning_rate=0.07764260483213357,
    depth=12,
    l2_leaf_reg=12,
    border_count=32,
    bagging_temperature=0,
    random_state=42,
    verbose=0,
    early_stopping_rounds=50
)

# 모델 훈련
best_model_catboost.fit(X_train, y_train)

# 테스트 데이터에 대해 예측
y_pred_catboost = best_model_catboost.predict(X_test)
mse_catboost = mean_squared_error(y_test, y_pred_catboost)
print(f"CatBoost Mean Squared Error: {mse_catboost}")

# 전체 데이터에 대해 예측
quantity_predicted = best_model_catboost.predict(X_missing)

# 경고 해결을 위해 .loc 사용
data_missing_quantity.loc[:, 'Quantity'] = quantity_predicted

# 결측치가 없는 데이터와 결측치가 예측된 데이터를 합칩니다.
main_data_filled = pd.concat([data_with_quantity, data_missing_quantity])

# 결과 저장
main_data_filled.to_csv('main_data_filled.csv', index=False)
