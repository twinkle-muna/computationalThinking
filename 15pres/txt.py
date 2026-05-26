import os

# 사용자에게 폴더 경로 입력받기
folder_path = input("폴더 경로를 입력하세요: ")

# 폴더와 하위 폴더 탐색
for root, dirs, files in os.walk(folder_path):

    # 현재 폴더 안의 파일 하나씩 확인
    for file in files:

        # 파일이 .txt 로 끝나는지 확인
        if file.endswith(".txt"):

            # 전체 경로 만들기
            full_path = os.path.join(root, file)

            # 출력
            print(full_path)
