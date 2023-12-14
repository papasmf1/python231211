import openpyxl
import random
from openpyxl import Workbook

# 무작위 제품 데이터 생성
product_data = []
for i in range(100):
    product_id = i + 1
    product_name = f"제품{i + 1}"
    quantity = random.randint(1, 10)
    price = round(random.uniform(10, 1000), 2)
    product_data.append((product_id, product_name, quantity, price))

# Excel 워크북 생성
workbook = Workbook()
worksheet = workbook.active
worksheet.title = "제품 판매 데이터"

# 열 제목 추가
worksheet.append(["제품ID", "제품명", "수량", "가격"])

# 데이터 추가
for product in product_data:
    worksheet.append(product)

# Excel 파일 저장
file_path = "c:\\work\\products.xlsx"
workbook.save(file_path)
print(f"Excel 파일이 {file_path}에 저장되었습니다.")
