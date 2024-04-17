def count_chars(string):
    # Khởi tạo một dictionary để lưu trữ số lần xuất hiện của các ký tự
    char_count = {}

    # Duyệt qua từng ký tự trong chuỗi
    for char in string:
        # Nếu ký tự là một chữ cái
        if char.isalpha():
            # Chuyển đổi ký tự thành chữ cái in thường để loại bỏ sự phân biệt chữ hoa chữ thường
            char = char.lower()
            # Nếu ký tự đã tồn tại trong từ điển, tăng giá trị lên 1
            if char in char_count:
                char_count[char] += 1
            # Nếu không, thêm ký tự vào từ điển và gán giá trị là 1
            else:
                char_count[char] = 1
    
    return char_count

# Test với các ví dụ
string1 = 'Happiness'
print(count_chars(string1))  # {'h': 1, 'a': 1, 'p': 2, 'i': 1, 'n': 1, 'e': 1, 's': 2}

string2 = 'smiles'
print(count_chars(string2))  # {'s': 2, 'm': 1, 'i': 1, 'l': 1, 'e': 1}
