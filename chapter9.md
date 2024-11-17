## 1장
- [x] anaconda 설치
- [x] colab 접속 및 런타임 유형 GPU 세팅

## 9장 - 워드 임베딩
### 이론
- word2vec (워드투벡터): 단어 간 유의미한 유사도를 반영하도록 나온 방법.
  - cbow: 예측해야 하는 단어를 주변단어로부터 파악하는 것
  - skip-gram: 중심단어로부터 주변단어 예측
 
- NNLM 과의 차이점은, NNLM에 비해 word2vec 이 단어 간 유사도 파악에 집중된 모델이며, 성능도 이에 특화되어 빠르다는 점.

### word2vec 실습
- 네이버 영화 리뷰
  - `urllib.request.urlretrieve("https://raw.githubusercontent.com/e9t/nsmc/master/ratings.txt", filename="ratings.txt")`: 파이썬의 urllib 라이브러리 이용하여 url 내 파일 받아오기
  - `pd.read_table('ratings.txt')`: pandas 라이브러리에서 파일을 테이블 형태로 받아오는 행위.
    - 궁금증: read_csv 가 더 빠르고 좋을 것 같은데, 굳이 read_table 로 한 이유가 있을까?
  - `dropna(how = 'any')`: pandas 에서 행 단위로 null (naN) 하나라도 있으면 제거. (axis 를 명시하면 행위를 바꿀 수 있음. 참고: https://yeko90.tistory.com/entry/%ED%8C%90%EB%8B%A4%EC%8A%A4-%EA%B8%B0%EC%B4%88-dropna%EB%A5%BC-%ED%86%B5%ED%95%B4-%EA%B2%B0%EC%B8%A1%EC%B9%98%EA%B0%80-%EC%9E%88%EB%8A%94-%ED%96%89%EC%97%B4-%EC%A0%9C%EA%B1%B0)
  - okt: 형태소 토큰화
    - 한국어는 띄어쓰기 단위로 토큰화하면 안됨. 교착어이기 떄문이다. `나는제이온이좋아요` 와 같은 문장도, 띄어쓰기 없어도 이해가 잘된다. 형태소 토큰화를 위해선 `okt.morphs()` 함수 사용할 것!
      - 참고: https://m.blog.naver.com/j7youngh/222875104191  
    - `stem=true` 를 사용해서 어간 추출이 됨. 참고: https://soyoung-new-challenge.tistory.com/31
  - `Word2Vec(sentences = tokenized_data, vector_size = 100, window = 5, min_count = 5, workers = 4, sg = 0)`
    - vector_size = 워드 벡터의 특징 값. 즉, 임베딩 된 벡터의 차원.
    - window = 컨텍스트 윈도우 크기
    - min_count = 단어 최소 빈도 수 제한 (빈도가 적은 단어들은 학습하지 않는다.)
    - workers = 학습을 위한 프로세스 수
    - sg = 0 은 CBOW, 1 은 Skip‑gram
  - `print(model.wv.most_similar("어벤져스"))`: 어벤져스와 유사어들 추출
    - 결과:
    ```text
    [('트랜스포머', 0.8490170240402222), ('분노의질주', 0.808656632900238), ('고사', 0.8060718178749084), ('아이언맨', 0.8060380220413208), ('다이하드', 0.8043357133865356), ('쥬라기', 0.7975572347640991), ('무간도', 0.797261118888855), ('엽문', 0.7933233976364136), ('넘버', 0.7916000485420227), ('탄도', 0.7907267212867737)]
    ```
    
