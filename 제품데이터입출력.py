import sqlite3
import random

# SQLite 데이터베이스 연결 및 테이블 생성
conn = sqlite3.connect('electronics.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS electronic_products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price REAL
    )
''')
conn.commit()

# 전자 제품 데이터 클래스 정의
class ElectronicsProduct:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def insert_product(self):
        cursor.execute('INSERT INTO electronic_products (name, price) VALUES (?, ?)', (self.name, self.price))
        conn.commit()

    def update_product(self, new_name, new_price):
        cursor.execute('UPDATE electronic_products SET name=?, price=? WHERE name=?', (new_name, new_price, self.name))
        conn.commit()
        self.name = new_name
        self.price = new_price

    def delete_product(self):
        cursor.execute('DELETE FROM electronic_products WHERE name=?', (self.name,))
        conn.commit()
        self.name = None
        self.price = None

    @staticmethod
    def get_all_products():
        cursor.execute('SELECT * FROM electronic_products')
        products = cursor.fetchall()
        return products

# 다양한 제품명 생성
product_names = []
adjectives = ["강력한", "고품질", "신속한", "편리한", "혁신적인", "스마트", "화려한", "효율적인", "휴대용", "고속", "무선", "디지털", "안전한", "환경 친화적인"]
nouns = ["노트북", "스마트폰", "태블릿", "카메라", "스마트워치", "이어폰", "게임 콘솔", "드론", "냉장고", "세탁기", "에어컨", "로봇 청소기", "스피커", "헤드폰"]

for _ in range(100):
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    product_name = f"{adjective} {noun}"
    product_names.append(product_name)

# 샘플 데이터 추가
for product_name in product_names:
    price = round(random.uniform(100, 2000), 2)  # 가격을 100부터 2000까지 무작위로 생성
    product = ElectronicsProduct(product_name, price)
    product.insert_product()

# 모든 전자 제품 조회
all_products = ElectronicsProduct.get_all_products()
for product in all_products:
    print(f"제품 ID: {product[0]}, 제품명: {product[1]}, 가격: {product[2]}")

# 데이터베이스 연결 종료
conn.close()
