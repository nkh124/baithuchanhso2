def count_words_in_file(file_path):
    # Khởi tạo một dictionary để lưu trữ số lần xuất hiện của các từ
    word_count = {}

    try:
        # Mở file để đọc
        with open(file_path, 'r') as file:
            # Đọc từng dòng trong file
            for line in file:
                # Tách các từ trong dòng và duyệt qua từng từ
                words = line.lower().split()
                for word in words:
                    # Nếu từ đã tồn tại trong từ điển, tăng giá trị lên 1
                    if word in word_count:
                        word_count[word] += 1
                    # Nếu không, thêm từ vào từ điển và gán giá trị là 1
                    else:
                        word_count[word] = 1
    except FileNotFoundError:
        print("File không tồn tại!")
    
    return word_count

# Test với một đường dẫn file txt
file_path = "sample.txt"
word_counts = count_words_in_file(file_path)
print(word_counts)