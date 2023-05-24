import tensorflow as tf
from keras.preprocessing.text import Tokenizer

# Пример текстовых данных
texts = ['Пример текста про автомобили', 'Пример текста про компьютеры', 'Пример текста про лошадей']
labels = [0, 1, 0]  # Пример меток для классификации

# Преобразование текста в векторное представление
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)

# Формирование входных данных для LSTM
max_sequence_length = max([len(seq) for seq in sequences])
vocab_size = len(tokenizer.word_index) + 1  # +1 для учета паддинга

X = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=max_sequence_length)
y = tf.keras.utils.to_categorical(labels)

# Формирование LSTM
model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(vocab_size, 100, input_length=max_sequence_length),
    tf.keras.layers.LSTM(64),
    tf.keras.layers.Dense(2, activation='softmax')
])

# Определение функции потерь и метода оптимизации для обновления весов LSTM в процессе обучения
loss_fn = tf.keras.losses.CategoricalCrossentropy()
optimizer = tf.keras.optimizers.Adam()

# Компиляция модели
model.compile(loss=loss_fn, optimizer=optimizer, metrics=['accuracy'])

# Обучение модели
model.fit(X, y, epochs=60, batch_size=32)

# Применение обученной нейросети на новых данных
new_texts = new_texts = ['Новый текст лошади', 'Новый текст машины']
new_sequences = tokenizer.texts_to_sequences(new_texts)
new_X = tf.keras.preprocessing.sequence.pad_sequences(new_sequences, maxlen=max_sequence_length)

predictions = model.predict(new_X)

print(predictions)