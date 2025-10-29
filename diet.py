from flask import Blueprint, render_template, request, Flask
import json

diet = Blueprint('diet', __name__)

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

# 加载 diet.json
with open('data/diet.json', 'r', encoding='utf-8') as f:
    diet_data = json.load(f)

@diet.route('/five-elements-diet', methods=['GET', 'POST'])
def five_elements_diet():
    result = None
    if request.method == 'POST':
        element = request.form.get('element')
        season = request.form.get('season')
        
        # 查找对应季节和体质的食物
        for s in diet_data['seasons']:
            if s['name'] == season:
                for t in s['types']:
                    if t['element'] == element:
                        result = {
                            'season': season,
                            'element': element,
                            'focus': t['focus'],
                            'principle': s['principle'],
                            'foods': t['foods']
                        }
                        break
                break
        
        if not result:
            result = {"error": "Invalid element or season selected."}
    
    return render_template('diet.html', result=result, food_to_blog_id=food_to_blog_id)

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(diet)
    app.run(debug=True)
