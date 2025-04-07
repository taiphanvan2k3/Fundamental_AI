## Đánh giá mô hình và so sánh kết quả giữa VGG16 và MobileNetV2 trên tập dữ liệu DogCatClassification

### `1. Đánh giá mô hình VGG16`
- Số lượng tham số trên tập dữ liệu này là `134,264,641` tham số.
- Sau khi chạy trên 10 epoch thu được checkpoint tốt nhất với các thông số sau:
```python
accuracy: 0.8675 - loss: 0.2948 - val_accuracy: 0.9117 - val_loss: 0.2106
```

- Xét về F1 score:
```text
Classification Report:
              precision    recall  f1-score   support

        cats       0.95      0.81      0.87       504
        dogs       0.83      0.96      0.89       504

    accuracy                           0.88      1008
   macro avg       0.89      0.88      0.88      1008
weighted avg       0.89      0.88      0.88      1008
```

### `2. Đánh giá mô hình MobileNetV2`
- Số lượng tham số trên tập dữ liệu này là `2,259,265` tham số.
- Cũng tiến hành chạy trên 10 epoch và thu được checkpoint tốt nhất với các thông số sau:
```python
accuracy: 0.9052 - loss: 0.2498 - val_accuracy: 0.9593 - val_loss: 0.1356
```


- Xét về F1 score:
```text
Classification Report:
              precision    recall  f1-score   support

        cats       0.95      0.97      0.96       504
        dogs       0.97      0.95      0.96       504

    accuracy                           0.96      1008
   macro avg       0.96      0.96      0.96      1008
weighted avg       0.96      0.96      0.96      1008
```

### `3. So sánh kết quả giữa VGG16 và MobileNetV2`
- Số lượng tham số của VGG16 là `134,264,641` trong khi MobileNetV2 chỉ có `2,259,265` tham số. Do đó thời gian huấn luyện và inference của MobileNetV2 sẽ nhanh hơn rất nhiều so với VGG16.
- Dựa trên kết quả ở trên có thể nhận thấy rằng MobileNetV2 có độ chính xác cao hơn VGG16 trên tập dữ liệu này.
- Accuracy của MobileNetV2 là `0.96` và cao hơn so với VGG16 là `0.88`.
- Về precision, recall:
    + MobileNetV2: Precision và Recall đều tốt hơn, đặc biệt là ở Cats (precision 0.95, recall 0.97) và Dogs (precision 0.97, recall 0.95).

    + VGG16: Mặc dù precision cao ở Cats (0.95), nhưng recall thấp (0.81), nghĩa là nó bỏ sót nhiều Cats. Còn với Dogs, precision thấp (0.83) nhưng recall cao (0.96), cho thấy nó nhận diện tốt nhưng không chính xác hoàn toàn.
- Về mặt F1 score, MobileNetV2 cũng cho kết quả tốt hơn với `0.96` so với `0.88` của VGG16.
