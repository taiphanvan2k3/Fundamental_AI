## Đánh giá giữa Logistic Regression và AdaBoost cho bài toán heart disease prediction

### 1. Mô hình Logistic Regression
- Mô hình này cần chuẩn hoá dữ liệu trước khi train, vì dữ liệu không đồng nhất về đơn vị đo lường, hơn nữa sẽ bị tràn số trong hàm sigmoid nếu không chuẩn hoá.
- Mô hình hội tụ từ `epoch = 10000` trở đi, với `learning rate = 0.01`
- Với `epoch = 10000` ta thu được weights và độ chính xác khoảng tương ứng là `86.7%`

### 2. Mô hình AdaBoost
- Mô hình này không cần chuẩn hoá dữ liệu trước khi train, vì nó sử dụng các mô hình weak learner, nên không cần chuẩn hoá dữ liệu.
- Độ chính xác của mô hình phụ thuộc nhiều vào số lượng weak learner
- Thông qua quá trình thử nghiệm với số lượng weak learner `[10, 50, 100, 500, 1000, 5000, 6000, 7000, 8000, 9000, 10000]` thì thấy mô hình hội tụ với `số lượng weak learner >= 5000`, độ chính xác khoảng `97.5%`