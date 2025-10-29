from flask import Flask, render_template, request
import json
import os

# 创建全局 Flask 应用（Vercel 必需）
app = Flask(__name__)

# 食物名称到博客ID的映射
food_to_blog_id = {
    "Adzuki Beans": 9,
    "Almond Milk": 10,
    "Almonds": 11,
    "Aloe Vera Juice": 12,
    "Apples": 13,
    "Arugula": 14,
    "Asparagus": 15,
    "Avocado": 16,
    "Bananas": 17,
    "Barley": 18,
    "Bean Sprouts": 19,
    "Beef": 20,
    "Beets": 21,
    "Bitter Greens": 22,
    "Bitter Melon": 23,
    "Black Beans": 24,
    "Black Rice": 25,
    "Black Sesame Seeds": 26,
    "Blackberries": 27,
    "Blueberries": 28,
    "Bok Choy": 29,
    "Bone Broth": 30,
    "Broccoli": 31,
    "Brown Rice": 32,
    "Brussels Sprouts": 33,
    "Butternut Squash": 34,
    "Cabbage": 35,
    "Cantaloupe": 36,
    "Carp": 37,
    "Carrots": 38,
    "Cauliflower": 39,
    "Celery": 40,
    "Chamomile Tea": 41,
    "Chia Seeds": 42,
    "Chicken Breast": 43,
    "Chicken Liver": 44,
    "Chrysanthemum Tea": 45,
    "Cinnamon": 46,
    "Clams": 47,
    "Coconut": 48,
    "Coconut Water": 49,
    "Cod": 50,
    "Cornmeal": 51,
    "Cranberries": 52,
    "Cucumber": 53,
    "Dandelion Greens": 54,
    "Dandelion Tea": 55,
    "Dried Tangerine Peel": 56,
    "Duck": 57,
    "Egg Whites": 58,
    "Eggs": 59,
    "Fennel Seeds": 60,
    "Figs": 61,
    "Flaxseeds": 62,
    "Gardenia Tea": 63,
    "Ginger": 64,
    "Goji Berries": 65,
    "Grapes": 66,
    "Green Beans": 67,
    "Green Onions": 68,
    "Green Tea": 69,
    "Grilled Chicken": 70,
    "Honey": 71,
    "Honeydew": 72,
    "Honeysuckle Tea": 73,
    "Kale": 74,
    "Kiwi": 75,
    "Lamb": 76,
    "Leeks": 77,
    "Lemon": 78,
    "Lentils": 79,
    "Lettuce": 80,
    "Licorice Root Tea": 81,
    "Lily Bulbs": 82,
    "Lime": 83,
    "Lotus Leaf Tea": 84,
    "Millet": 85,
    "Mint": 86,
    "Mulberries": 87,
    "Mung Beans": 88,
    "Mushrooms": 89,
    "Nettle Tea": 90,
    "Oats": 91,
    "Papaya": 92,
    "Parsnips": 93,
    "Pears": 94,
    "Peppermint Tea": 95,
    "Persimmons": 96,
    "Pineapple": 97,
    "Plums": 98,
    "Pomegranates": 99,
    "Pork": 100,
    "Pumpkin": 101,
    "Quinoa": 102,
    "Radish": 103,
    "Red Beans": 104,
    "Red Dates": 105,
    "Rice": 106,
    "Rice Noodles": 107,
    "Romaine Lettuce": 108,
    "Rooibos Tea": 109,
    "Rose Tea": 110,
    "Salmon": 111,
    "Seaweed": 112,
    "Sesame Oil": 113,
    "Shrimp": 114,
    "Spinach": 115,
    "Strawberries": 116,
    "Sweet Potato": 117,
    "Tilapia": 118,
    "Tofu": 119,
    "Tomatoes": 120,
    "Tremella": 121,
    "Turkey": 122,
    "Turnips": 123,
    "Walnuts": 124,
    "Watercress": 125,
    "Watermelon": 126,
    "Winter Melon": 127,
    "Zucchini": 128
}

# 加载 diet.json（带错误处理）
json_path = 'data/diet.json'
if os.path.exists(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        diet_data = json.load(f)
else:
    diet_data = {}
    print(f"Warning: {json_path} not found in {os.getcwd()}")

# 根路径路由：同时支持 GET（显示表单）和 POST（提交查询）
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        element = request.form.get('element')
        season = request.form.get('season')

        # 查找匹配的饮食建议
        for s in diet_data.get('seasons', []):
            if s.get('name') == season:
                for t in s.get('types', []):
                    if t.get('element') == element:
                        result = {
                            'season': season,
                            'element': element,
                            'focus': t.get('focus'),
                            'principle': s.get('principle'),
                            'foods': t.get('foods', [])
                        }
                        break
                break

        if not result:
            result = {"error": "Invalid element or season selected."}

    return render_template('diet.html', result=result, food_to_blog_id=food_to_blog_id)

# 可选：保留 /five-elements-diet 路径（兼容旧链接）
@app.route('/five-elements-diet', methods=['GET', 'POST'])
def five_elements_diet():
    return index()  # 直接复用上面的逻辑

# Vercel 要求：必须暴露 `app` 作为 WSGI 应用
# （不需要 if __name__ == '__main__' 块）
