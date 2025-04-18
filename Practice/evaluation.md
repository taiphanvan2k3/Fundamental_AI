### Tiền xử lý dữ liệu
- Xoá các hàng chứa giá trị null và các hàng bị trùng lặp
- Vơi các tên cột mà bắt đầu bởi khoảng trắng thì sẽ bỏ khoảng trắng đó đi
- Với các tên cột có khoảng trắng ở giữa thì sẽ thay thế bằng dấu gạch dưới
- Đổi tên một số giá trị của cột Label để dễ dàng hơn trong việc phân tích như `Dos Hulk` thành `Dos`,...
- Thực hiện cân bằng dữ liệu giữa các lớp trong cột Label. Vì các sample có label là "BENIGN" có số lượng rất lớn so với các label khác nên sẽ thực hiện giảm số lượng sample của lớp này xuống bằng với lớp có số lượng nhỏ nhất. Việc này sẽ giúp cho việc phân tích dữ liệu dễ dàng hơn và không bị thiên lệch về một lớp nào đó.
- Thực hiện quá trình encode và chuẩn hoá dữ liệu:
    + Vì ban đầu các cột có giá trị là các giá trị thuộc các không gian khác nhau nên sẽ thực hiện chuẩn hoá dữ liệu về cùng một không gian. Việc này sẽ giúp cho việc phân tích dữ liệu dễ dàng hơn và không bị thiên lệch về một không gian nào đó.
    + Sử dụng hàm `LabelEncoder` để chuyển đổi các giá trị của cột Label thành các giá trị số nguyên.
- Với mỗi record có `78` column nên để chuyển đổi từng record thành từng ảnh vuông nên ta sẽ sử dụng hàm `reshape` để chuyển đổi các giá trị của từng record thành một ảnh vuông có kích thước `9x9`.


### Đánh giá hiệu suất của mô hình
#### 1. Mô hình CNN
- Sau khi training với 10 epoch và ưu tiên chọn epoch có val_accuracy cao nhất thì ta được:
    + loss: 0.0520 - accuracy: 0.9844 - val_loss: 0.0510 - val_accuracy: 0.9875
- Dựa vào đồ thị loss và accuracy ta thấy rằng model học rất tốt và không có hiện tượng overfitting.

#### 2. Mô hình ResNet50
- Gồm 2 giai đoạn:
    + Giai đoạn 1: freeze các layer của model ResNet50 và chỉ train các layer classification được thêm vào. Sau khi training với 10 epoch và ưu tiên chọn epoch có val_accuracy cao nhất thì ta được:
    `loss: 0.1651 - accuracy: 0.9509 - val_loss: 0.1416 - val_accuracy: 0.9679`
    Lúc này hiệu suất của model đã tốt nhưng chưa bằng với model CNN cơ bản.
    + Giai đoạn 2: tiếp tục fine-tune các layer của model ResNet50 bằng cách unfreeze 30 layer cuối cùng của model ResNet50 và train tiếp với 10 epoch. Sau khi training với 10 epoch và ưu tiên chọn epoch có val_accuracy cao nhất thì ta được:
    `loss: 0.0303 - accuracy: 0.9911 - val_loss: 0.0497 - val_accuracy: 0.9884`
    Lúc này hiệu suất của model đã tốt hơn rất nhiều so với giai đoạn 1 và cũng tốt hơn so với model CNN cơ bản.
- Dựa vào đồ thị loss và accuracy ta thấy rằng model học rất tốt và không có hiện tượng overfitting.