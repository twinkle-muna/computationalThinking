import os
import hashlib


def make_hash(path):
    # 파일 해시 생성 함수
    hash_object = hashlib.sha256()

    with open(path, "rb") as file:
        chunk = file.read(4096)

        while chunk:
            hash_object.update(chunk)
            chunk = file.read(4096)

    return hash_object.hexdigest()


def collect_files(folder):
    # 폴더 안 파일 정보 저장
    result = {}

    for current_path, folder_names, file_names in os.walk(folder):

        for name in file_names:
            absolute_path = os.path.join(current_path, name)

            # 상대 경로 구하기
            relative = os.path.relpath(absolute_path, folder)

            result[relative] = {
                "size": os.path.getsize(absolute_path),
                "hash": make_hash(absolute_path)
            }

    return result


def check_directories(folder1, folder2):

    data1 = collect_files(folder1)
    data2 = collect_files(folder2)

    # 파일 수 비교
    if len(data1) == len(data2):
        print("파일 개수가 같습니다.")
    else:
        print("파일 개수가 다릅니다.")
        print(f"{folder1}: {len(data1)}개")
        print(f"{folder2}: {len(data2)}개")
        return

    # 파일 목록 비교
    files1 = set(data1.keys())
    files2 = set(data2.keys())

    if files1 != files2:

        print("파일 구조 또는 파일명이 다릅니다.")

        diff1 = files1 - files2
        diff2 = files2 - files1

        if diff1:
            print(f"\n{folder1}에만 존재하는 파일")
            for file in sorted(diff1):
                print(file)

        if diff2:
            print(f"\n{folder2}에만 존재하는 파일")
            for file in sorted(diff2):
                print(file)

        return

    print("파일 구조가 동일합니다.")

    same = True

    # 파일 내용 비교
    for file in sorted(files1):

        size_a = data1[file]["size"]
        size_b = data2[file]["size"]

        hash_a = data1[file]["hash"]
        hash_b = data2[file]["hash"]

        if size_a != size_b:
            print(f"\n[파일 크기 다름] {file}")
            same = False

        elif hash_a != hash_b:
            print(f"\n[파일 내용 다름] {file}")
            same = False

    if same:
        print("\n두 폴더는 완전히 같습니다.")
    else:
        print("\n차이가 있는 파일이 존재합니다.")


if __name__ == "__main__":

    folder1 = input("첫 번째 폴더 입력: ").strip()
    folder2 = input("두 번째 폴더 입력: ").strip()

    if not os.path.exists(folder1):
        print("첫 번째 폴더가 존재하지 않습니다.")

    elif not os.path.exists(folder2):
        print("두 번째 폴더가 존재하지 않습니다.")

    else:
        check_directories(folder1, folder2)
