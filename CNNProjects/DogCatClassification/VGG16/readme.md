- `DogCatClassifier_SimpleLayers`: chỉ dùng phần CNN của VGG16 rồi bổ sung thêm các lớp Fully Connected đơn giản ở sau

- `DogCatClassifier_Full`: dùng phần trích xuất đặc trưng của VGG16 sau đó thêm các lớp Fully Connected phức tạp hơn ở sau

- `build_vgg16`: Thử xây dựng model VGG16 bằng những lớp cơ bản nhất của Keras, xây dựng bằng 3 cách

- `DogCatClassifier_Manual`: xây dựng model VGG16 bằng cách tự định nghĩa các lớp Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization và tự kết nối chúng với nhau. Rồi lấy model đó để train trên tập dữ liệu DogCat.