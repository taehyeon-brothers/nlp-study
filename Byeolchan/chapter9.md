## Word Embedding

희소 표현(Sparse Representation)

- Sparse Representation: 백터 대부분이 0으로 표현
- 단어 개수에 따라 백터 차원 급상승

밀집 표현

- 사용자가 정의한 차원으로 백터 표현을 맞춘다.

워드 임베딩

- 단어를 밀집 백터로 표현
- 임베딩 백터: 워드 임배딩을 통해 나온 밀집 백터

## Word2Vec

- 원핫인코딩 백터간 유사성 표현 불가
- 단어의 의미를 다차원 공간에 백터화 => 분산 표현

분산 표현

분포 가설

- 비슷한 문맥에 등장하는 단어들은 비슷한 의미를 가진다
- 저차원에 단어 의미를 1 하나 대신 여러 차원에다가 분산

## CBOW

- Word2Vec의 학습 방식 중 하나(다른 하나: Skip Gram)
- 중간 단어들을 입력으로 주변 단어 예측
- 예측해야 하는 단어: 중심 단어
- 예측에 사용되는 단어: 주변 단어
- 윈도우: 중심 단어 기준으로 앞 뒤 주변단어의 개수
- 슬라이딩 윈도우: 중심 단어 선택을 변경하며 데이터 셋 생성

문제: Skipgram과 CBOW 차이를 이해하기가 힘들다.

문제: NNLM VS. WORD2VEC

## Glove

- 카운트 기반과 예측 기반 모두 사용
- 실무에서는 Word2Vec, Glove 모두 사용하여 성능이 좋은 것 선택
- LSA: 왕:남자, 여왕:(여자) 같이 단어 유추에 약하다. (카운드 기반) Word2Vec: 주변 단어만 고려.(예측 기반)
- Window based co occurence matrix
  잘 모르겠다..
- 손실 함수
  잘 모르겠다...

- 에포크란??

## FastText

- 페이스북에서 개발한 Word2Vec의 확장판
- FastText에서는 subword(단어 안 단어,내부단어) 고려
- 모르는 단어 (oov)에 대한 대응 ex) birthplace
- 등장 빈도수가 적었던 단어에 대한 대응(오타, 맞춤법 틀림 대응)

한국어에서 fast text

1. 음절 단위
2. 자모 단위

## Pre-trained word embedding

- 위키피딩 같은 방대한 코퍼스로 word2vec, fasttest, glove 훈련을 하는 방법도 있다.
- keras의 embedding layer는 현재 갖고 있는 데이터로 처음부터 학습
- 임베팅 층은 룩업 테이블?

## 엘모(Embeddings from Language Model) ELMo

- 사전 훈련된 언어 모델 사용
- 문맥을 반영한 워드 임베딩

## biLM??

## 임베딩 시각화 도구

- embedding projector

## 문서 백터 이용한 추천 시스템

책의 문서 백터와 유사한 문서 백터값 추천

## 임베딩 평균??

## Doc2VEc으로 공시 사업보고서 유사도 계산
