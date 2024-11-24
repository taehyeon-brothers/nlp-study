from gensim.models import Word2Vec
from gensim.models import KeyedVectors

model = Word2Vec(sentences=result, vector_size=100, window=5, min_count=5, workers=4, sg=0)
model_result = model.wv.most_similar("man")
print(model_result)

model.wv.save_word2vec_format('eng_w2v') # 모 델 저 장
loaded_model = KeyedVectors.load_word2vec_format("eng_w2v") # 모 델 로 드

model_result = loaded_model.most_similar("man")
print(model_result)