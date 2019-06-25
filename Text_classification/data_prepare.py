import zipfile

DATA_IN_PATH = './Text_classification/data/' #데이터가 저장된 경로

file_list = ['labeledTrainData.tsv.zip', 'unlabeledTrainData.tsv.zip', 'testData.tsv.zip']
# 압축을 풀고자 하는 파일의 이름들을 리스트로 지정

for file in file_list:
    zipRef = zipfile.ZipFile(DATA_IN_PATH + file, 'r')
    # zipfile.ZipFile(파일의 경로, 파일 모드 옵션(파일을 읽어 들여 압축한 파일을 내놓는 방식이므로 읽기모드인 r)
    zipRef.extractall(DATA_IN_PATH)
    # extractall(압축을 풀고자 하는 경로) 함수를 사용해 압축을 푼다.
    zipRef.close()
    # 파일 처리를 마치기 위한 close() 함수
