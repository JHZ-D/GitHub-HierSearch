import pandas as pd
import numpy as np
import torch
import torch.optim as optim
from keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, hamming_loss
import json
def get_top_k(y_pred,k):
    idx = np.argpartition(y_pred, -k)
    new_arr = y_pred[idx]
    max_k = new_arr[-k]
    return max_k
def Success_rate(y_test,y_pred):
    count = 0
    for i in range(len(y_test)):
        for j in range(len(y_test[i])):
            if(y_test[i][j]==1 and y_pred[i][j]==1):
                count += 1
                break
    return count/len(y_test)

with open('llist.json', 'r') as f:
    llist = json.load(f)
# 加载数据
df = pd.read_csv('train.csv')
df1 = pd.read_csv('test.csv')
df2 = pd.read_csv('test_labels.csv')
# 分割输入和标签
X_train = df.iloc[:, 1].values
y_train = df.iloc[:, 2:].values
X_test = df1.iloc[:,1].values
y_test = df2.iloc[:,1:].values
# 数据预处理
# MAX_WORDS = 5000  # 设置最大词汇量
# MAX_LEN = 100  # 设置每个输入序列的最大长度

# 将X转换为字符串列表
X_train = [str(x) for x in X_train]
X_test = [str(x) for x in X_test]
# 使用Tokenizer将文本转换为数字序列
# tokenizer = Tokenizer(num_words=MAX_WORDS)
# tokenizer.fit_on_texts(X_train)

# X_train_seq = tokenizer.texts_to_sequences(X_train)
# X_test_seq = tokenizer.texts_to_sequences(X_test)
# # 使用pad_sequences对输入序列进行填充，使得长度一致
# X_train = pad_sequences(X_train_seq, maxlen=MAX_LEN)
# X_test = pad_sequences(X_test_seq, maxlen=MAX_LEN)
# 划分训练集和测试集

y_train = y_train.astype(float)
y_test = y_test.astype(float)
# 构建LSTM多标签分类模型
# model = Sequential()
# model.add(Embedding(MAX_WORDS, 128, input_length=MAX_LEN))
# model.add(LSTM(128))
# model.add(Dense(y_train.shape[1], activation='sigmoid'))

# # 编译模型
# model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# # 训练模型
# model.fit(X_train, y_train, epochs=71, batch_size=64, validation_split=0.1)
# model.save('lstm.h5')
# # 模型评估
# y_pred = model.predict(X_test)
# y_pred_total = y_pred.copy()
# y_pred_total[y_pred_total >= 0.5] = 1
# y_pred_total[y_pred_total < 0.5] = 0

# with open('prediction.txt','w') as f:
#     for i in range(len(y_pred)):
#         for j in range(len(y_pred[i])):
#             f.write(str((y_pred[i][j])))
#             if(j!=len(y_pred[i])-1):
#                 f.write(',')
#         f.write('\n')

for 
y_pred = 
# 将预测结果转换为整数型数组
y_pred_total = y_pred_total.astype(int)
# 计算各种评估指标
accuracy_total = accuracy_score(y_test, y_pred_total)
precision_total = precision_score(y_test, y_pred_total, average='weighted')
recall_total = recall_score(y_test, y_pred_total, average='weighted')
f1 = f1_score(y_test, y_pred_total, average='weighted')
hamming_loss_total = hamming_loss(y_test, y_pred_total)

# 打印评估指标
print("Total Accuracy: {:.4f}".format(accuracy_total))
print("Total Precision: {:.4f}".format(precision_total))
print("Total Recall: {:.4f}".format(recall_total))
print("Total F1-score: {:.4f}".format(f1))
print("Total Hamming Loss: {:.4f}".format(hamming_loss_total))
with open('result.txt','a') as f:
    f.write(f"Total Accuracy: {accuracy_total:.4f}\n")
    f.write(f"Total Precision: {precision_total:.4f}\n")
    f.write(f"Total Recall: {recall_total:.4f}\n")
    f.write(f"Total F1-score: {f1:.4f}\n")
    f.write(f"Total Hamming Loss: {hamming_loss_total:.4f}\n")
#top1
y_pred_top_1 = []
for i in range(len(y_pred)):
    y_pred_temp = []
    max_1 = get_top_k(y_pred[i],1)
    for j in range(len(y_pred[i])):
        if y_pred[i][j] >= max_1 and y_pred[i][j] != 0:
            y_pred_temp.append(1)
        else:
            y_pred_temp.append(0)
    y_pred_top_1.append(y_pred_temp)
y_pred_top_1 = np.array(y_pred_top_1)
# 将预测结果转换为整数型数组
y_pred_top_1 = y_pred_top_1.astype(int)
# 计算各种评估指标
success_rate = Success_rate(y_test,y_pred_top_1)
accuracy_total = accuracy_score(y_test, y_pred_top_1)
precision_total = precision_score(y_test, y_pred_top_1, average='weighted')
recall_total = recall_score(y_test, y_pred_top_1, average='weighted')
f1 = f1_score(y_test, y_pred_top_1, average='weighted')
hamming_loss_total = hamming_loss(y_test, y_pred_top_1)

# 打印评估指标
print("Top1 SuccessRate: {:.4f}".format(success_rate))
print("Top1 Accuracy: {:.4f}".format(accuracy_total))
print("Top1 Precision: {:.4f}".format(precision_total))
print("Top1 Recall: {:.4f}".format(recall_total))
print("Top1 F1-score: {:.4f}".format(f1))
print("Top1 Hamming Loss: {:.4f}".format(hamming_loss_total))
with open('result.txt','a') as f:
    f.write(f"Top1 SuccessRate: {success_rate:.4f}\n")
    f.write(f"Top1 Accuracy: {accuracy_total:.4f}\n")
    f.write(f"Top1 Precision: {precision_total:.4f}\n")
    f.write(f"Top1 Recall: {recall_total:.4f}\n")
    f.write(f"Top1 F1-score: {f1:.4f}\n")
    f.write(f"Top1 Hamming Loss: {hamming_loss_total:.4f}\n")
#top2
y_pred_top_2 = []
for i in range(len(y_pred)):
    y_pred_temp = []
    max_2 = get_top_k(y_pred[i],2)
    for j in range(len(y_pred[i])):
        if y_pred[i][j] >= max_2 and y_pred[i][j] != 0:
            y_pred_temp.append(1)
        else:
            y_pred_temp.append(0)
    y_pred_top_2.append(y_pred_temp)
y_pred_top_2 = np.array(y_pred_top_2)
# 将预测结果转换为整数型数组
y_pred_top_2 = y_pred_top_2.astype(int)

# 计算各种评估指标
success_rate = Success_rate(y_test,y_pred_top_2)
accuracy_total = accuracy_score(y_test, y_pred_top_2)
precision_total = precision_score(y_test, y_pred_top_2, average='weighted')
recall_total = recall_score(y_test, y_pred_top_2, average='weighted')
f1 = f1_score(y_test, y_pred_top_2, average='weighted')
hamming_loss_total = hamming_loss(y_test, y_pred_top_2)

# 打印评估指标
print("Top2 SuccessRate: {:.4f}".format(success_rate))
print("Top2 Accuracy: {:.4f}".format(accuracy_total))
print("Top2 Precision: {:.4f}".format(precision_total))
print("Top2 Recall: {:.4f}".format(recall_total))
print("Top2 F1-score: {:.4f}".format(f1))
print("Top2 Hamming Loss: {:.4f}".format(hamming_loss_total))

with open('result.txt','a') as f:
    f.write(f"Top2 SuccessRate: {success_rate:.4f}\n")
    f.write(f"Top2 Accuracy: {accuracy_total:.4f}\n")
    f.write(f"Top2 Precision: {precision_total:.4f}\n")
    f.write(f"Top2 Recall: {recall_total:.4f}\n")
    f.write(f"Top2 F1-score: {f1:.4f}\n")
    f.write(f"Top2 Hamming Loss: {hamming_loss_total:.4f}\n")
#top5
y_pred_top_5 = []
for i in range(len(y_pred)):
    y_pred_temp = []
    max_5 = get_top_k(y_pred[i],5)
    for j in range(len(y_pred[i])):
        if y_pred[i][j] >= max_5 and y_pred[i][j] != 0:
            y_pred_temp.append(1)
        else:
            y_pred_temp.append(0)
    y_pred_top_5.append(y_pred_temp)
y_pred_top_5 = np.array(y_pred_top_5)
# 将预测结果转换为整数型数组
y_pred_top_5 = y_pred_top_5.astype(int)

# 计算各种评估指标
success_rate = Success_rate(y_test,y_pred_top_5)
accuracy_total = accuracy_score(y_test, y_pred_top_5)
precision_total = precision_score(y_test, y_pred_top_5, average='weighted')
recall_total = recall_score(y_test, y_pred_top_5, average='weighted')
f1 = f1_score(y_test, y_pred_top_5, average='weighted')
hamming_loss_total = hamming_loss(y_test, y_pred_top_5)

# 打印评估指标
print("Top5 SuccessRate: {:.4f}".format(success_rate))
print("Top5 Accuracy: {:.4f}".format(accuracy_total))
print("Top5 Precision: {:.4f}".format(precision_total))
print("Top5 Recall: {:.4f}".format(recall_total))
print("Top5 F1-score: {:.4f}".format(f1))
print("Top5 Hamming Loss: {:.4f}".format(hamming_loss_total))

with open('result.txt','a') as f:
    f.write(f"Top5 SuccessRate: {success_rate:.4f}\n")
    f.write(f"Top5 Accuracy: {accuracy_total:.4f}\n")
    f.write(f"Top5 Precision: {precision_total:.4f}\n")
    f.write(f"Top5 Recall: {recall_total:.4f}\n")
    f.write(f"Top5 F1-score: {f1:.4f}\n")
    f.write(f"Top5 Hamming Loss: {hamming_loss_total:.4f}\n")
#top8
y_pred_top_8 = []
for i in range(len(y_pred)):
    y_pred_temp = []
    max_8 = get_top_k(y_pred[i],8)
    for j in range(len(y_pred[i])):
        if y_pred[i][j] >= max_8 and y_pred[i][j] != 0:
            y_pred_temp.append(1)
        else:
            y_pred_temp.append(0)
    y_pred_top_8.append(y_pred_temp)
y_pred_top_8 = np.array(y_pred_top_8)
# 将预测结果转换为整数型数组
y_pred_top_8 = y_pred_top_8.astype(int)

# 计算各种评估指标
success_rate = Success_rate(y_test,y_pred_top_8)
accuracy_total = accuracy_score(y_test, y_pred_top_8)
precision_total = precision_score(y_test, y_pred_top_8, average='weighted')
recall_total = recall_score(y_test, y_pred_top_8, average='weighted')
f1 = f1_score(y_test, y_pred_top_8, average='weighted')
hamming_loss_total = hamming_loss(y_test, y_pred_top_8)

# 打印评估指标
print("Top8 SuccessRate: {:.4f}".format(success_rate))
print("Top8 Accuracy: {:.4f}".format(accuracy_total))
print("Top8 Precision: {:.4f}".format(precision_total))
print("Top8 Recall: {:.4f}".format(recall_total))
print("Top8 F1-score: {:.4f}".format(f1))
print("Top8 Hamming Loss: {:.4f}".format(hamming_loss_total))
with open('result.txt','a') as f:
    f.write(f"Top8 SuccessRate: {success_rate:.4f}\n")
    f.write(f"Top8 Accuracy: {accuracy_total:.4f}\n")
    f.write(f"Top8 Precision: {precision_total:.4f}\n")
    f.write(f"Top8 Recall: {recall_total:.4f}\n")
    f.write(f"Top8 F1-score: {f1:.4f}\n")
    f.write(f"Top8 Hamming Loss: {hamming_loss_total:.4f}\n")