import pandas as pd

LOData = pd.read_csv('main_data_filled.csv')

def recommend_menu_for_30_days():
    # 음식 카테고리 매핑
    food_categories = {'밥': [], '김치': [], '반찬': [], '후식': [], '국': []}
    
    # 카테고리별 음식 필터링
    for index, row in LOData.iterrows():
        if '밥' in row['TYPE']:
            food_categories['밥'].append(row['FOOD_NM'])
        elif '김치' in row['TYPE']:
            food_categories['김치'].append(row['FOOD_NM'])
        elif '반찬' in row['TYPE']:
            food_categories['반찬'].append(row['FOOD_NM'])
        elif '후식' in row['TYPE']:
            food_categories['후식'].append(row['FOOD_NM'])
        elif '국' in row['TYPE']:
            food_categories['국'].append(row['FOOD_NM'])
    
    # 잔반량 기준으로 정렬
    for category in food_categories.keys():
        foods = food_categories[category]
        category_foods = LOData[LOData['FOOD_NM'].isin(foods)].sort_values(by='Quantity')
        food_categories[category] = list(category_foods['FOOD_NM'])

    # 30일치 메뉴 생성
    menus = []
    for day in range(30):
        daily_menu = {}
        for category, foods in food_categories.items():
            if category == '반찬':
                if len(foods) > 1:
                    selected_foods = [foods.pop(0), foods.pop(0)]
                    daily_menu[category] = selected_foods
            else:
                if len(foods) > 0:
                    selected_food = foods.pop(0)
                    daily_menu[category] = selected_food
        menus.append(daily_menu)

        # 만약 특정 카테고리의 음식이 모두 사용된 경우, 초기 상태로 되돌림
        for category in food_categories.keys():
            if len(food_categories[category]) == 0:
                foods = food_categories[category]
                category_foods = LOData[LOData['FOOD_NM'].isin(foods)].sort_values(by='Quantity')
                food_categories[category] = list(category_foods['FOOD_NM'])

    return menus

def convert_menus_to_text(menus):
    menu_texts = []
    for i, menu in enumerate(menus):
        menu_text = f"Day {i+1} Menu:\n"
        for category, food in menu.items():
            if category == '반찬':
                menu_text += f"{category}: {', '.join(food)}\n"
            else:
                menu_text += f"{category}: {food}\n"
        menu_texts.append(menu_text)
    return "\n".join(menu_texts)

def save_menus_to_text_file(menus_text, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(menus_text)


# 30일치 추천 메뉴 생성
recommended_menus = recommend_menu_for_30_days()

# 추천 메뉴 텍스트로 변환
recommended_menus_text = convert_menus_to_text(recommended_menus)

# 텍스트 파일로 저장
text_file_path = 'menu_for_30_days.txt'
save_menus_to_text_file(recommended_menus_text, text_file_path)


