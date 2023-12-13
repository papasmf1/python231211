import os
import shutil

# 다운로드 폴더 경로
download_folder = r'C:\Users\Student\Downloads'

# 목적지 폴더 경로 설정
image_folder = os.path.join(download_folder, 'images')
data_folder = os.path.join(download_folder, 'data')
docs_folder = os.path.join(download_folder, 'docs')

# 폴더가 없다면 생성
for folder in [image_folder, data_folder, docs_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# 다운로드 폴더의 파일 목록 가져오기
downloaded_files = os.listdir(download_folder)

# 파일 이동 작업
for file in downloaded_files:
    source_path = os.path.join(download_folder, file)
    if file.lower().endswith(('.jpg', '.jpeg')):
        # 이미지 파일을 images 폴더로 이동
        destination_path = os.path.join(image_folder, file)
        shutil.move(source_path, destination_path)
    elif file.lower().endswith(('.csv', '.xlsx')):
        # CSV 또는 XLSX 파일을 data 폴더로 이동
        destination_path = os.path.join(data_folder, file)
        shutil.move(source_path, destination_path)
    elif file.lower().endswith('.pdf'):
        # PDF 파일을 docs 폴더로 이동
        destination_path = os.path.join(docs_folder, file)
        shutil.move(source_path, destination_path)

print("파일 이동이 완료되었습니다.")
