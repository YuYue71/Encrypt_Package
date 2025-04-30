
# ord() 將字串轉換為 Unicode 編碼
# chr() 將 Unicode 編碼轉換為字串

# 凱薩加密（Caesar）
def Caesar(text: str, shift: int) -> str :
    encrypted_text = ""
    for char in text:                               # 逐字元加密 (我真的不太喜歡用for..)
        if char.isupper():
            ascii_offset = 65                               # 大寫字母的 ASCII 編碼範圍是 65-90 
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)    # 26 是字母表的大小
            encrypted_text += encrypted_char
        elif char.islower():
            ascii_offset = 97                               # 小寫字母的 ASCII 編碼範圍是 97-122
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)    # 26 是字母表的大小
            encrypted_text += encrypted_char
        elif char.isdigit():
            ascii_offset = 48                               # 數字的 ASCII 編碼範圍是 48-57
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 10 + ascii_offset)    # 10 是數字十進位的大小
            encrypted_text += encrypted_char
        else:                                               # 其他字元加密
                code_point = ord(char)                      # 轉換字串為 Unicode 編碼 
                new_code = (code_point + shift) % 0x110000  # Unicode 最大值 0x10FFFF（即 1114111 十進制）
                encrypted_text += chr(new_code)             # 將 Unicode 編碼轉換為字串
    return encrypted_text

    # 解密則使用負值的移位量




# ROT13
def ROT13(text: str) -> str:
    return Caesar(text, 13)                                 # ROT13 是凱薩加密的特例，移位量為 13

    # 解密則使用相同的函數，因為 ROT13 是對稱加密算法




# Atbash 加密
def Atbash(text: str) -> str:
    encrypted_text = ""
    for char in text:
        if char.isupper():
            ascii_offset = 65                               # 大寫字母的 ASCII 編碼範圍是 65-90
            encrypted_char = chr(155 - ord(char))           # 155 = 65 + 90
            encrypted_text += encrypted_char
        elif char.islower():
            ascii_offset = 97                               # 小寫字母的 ASCII 編碼範圍是 97-122
            encrypted_char = chr(219 - ord(char))           # 219 = 97 + 122
            encrypted_text += encrypted_char
        elif char.isdigit():
            ascii_offset = 48                               # 數字的 ASCII 編碼範圍是 48-57
            encrypted_char = chr(105 - ord(char))           # 105 = 48 + 57
            encrypted_text += encrypted_char
        else:
            code_point = ord(char)                          # 轉換字串為 Unicode 編碼
            new_code = (0x10FFFF - code_point) % 0x110000   # Unicode 最大值 0x10FFFF（即 1114111 十進制）
            encrypted_text += chr(new_code)                 # 將 Unicode 編碼轉換為字串
    return encrypted_text

    # 解密則使用相同的函數，因為 Atbash 是對稱加密算法




# Affine 線性加密
def Affine(text: str, a: int, b: int) -> str:
    encrypted_text = ""
    for char in text:
        if char.isupper():
            ascii_offset = 65                               # 大寫字母的 ASCII 編碼範圍是 65-90
            encrypted_char = chr((a * (ord(char) - ascii_offset) + b) % 26 + ascii_offset)  # 26 是字母表的大小
            encrypted_text += encrypted_char
        elif char.islower():
            ascii_offset = 97                               # 小寫字母的 ASCII 編碼範圍是 97-122
            encrypted_char = chr((a * (ord(char) - ascii_offset) + b) % 26 + ascii_offset)  # 26 是字母表的大小
            encrypted_text += encrypted_char
        elif char.isdigit():
            ascii_offset = 48                               # 數字的 ASCII 編碼範圍是 48-57
            encrypted_char = chr((a * (ord(char) - ascii_offset) + b) % 10 + ascii_offset)  # 10 是數字十進位的大小
            encrypted_text += encrypted_char
        else:
            code_point = ord(char)                          # 轉換字串為 Unicode 編碼
            new_code = (a * code_point + b) % 0x110000      # Unicode 最大值 0x10FFFF（即 1114111 十進制）
            encrypted_text += chr(new_code)                 # 將 Unicode 編碼轉換為字串
    return encrypted_text

    # 解密則使用負值的移位量
    # 需要注意的是，a 必須與字母表的大小互質，否則無法解密
    # 例如，對於字母表大小為 26 的情況，a 必須是奇數且不等於 13



# 維吉尼亞加密（Vigenère）
def Vigenere(text: str, key: str) -> str:
    encrypted_text = ""
    key_length = len(key)
    key_index = 0
    for char in text:
        if char.isupper():
            ascii_offset = 65                               # 大寫字母的 ASCII 編碼範圍是 65-90
            shift = ord(key[key_index % key_length].upper()) - 65  # 將密鑰字元轉換為移位量
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)  # 26 是字母表的大小
            encrypted_text += encrypted_char
            key_index += 1
        elif char.islower():
            ascii_offset = 97                               # 小寫字母的 ASCII 編碼範圍是 97-122
            shift = ord(key[key_index % key_length].lower()) - 97  # 將密鑰字元轉換為移位量
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)  # 26 是字母表的大小
            encrypted_text += encrypted_char
            key_index += 1
        elif char.isdigit():
            ascii_offset = 48                               # 數字的 ASCII 編碼範圍是 48-57
            shift = ord(key[key_index % key_length]) - 48   # 將密鑰字元轉換為移位量
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 10 + ascii_offset)  # 10 是數字十進位的大小
            encrypted_text += encrypted_char
            key_index += 1
        else:
            encrypted_text += char                          # 不加密其他字元，直接添加到結果中

    return encrypted_text

    # 解密則使用相同的函數，因為 Vigenère 是對稱加密算法
    # 需要注意的是，Vigenère 加密算法的安全性取決於密鑰的長度和隨機性




# 自定替換加密
def Substitution(text: str, substitution_table: dict) -> str:
    encrypted_text = ""
    for char in text:
        if char in substitution_table:
            encrypted_text += substitution_table[char]      # 使用替換表進行加密
        else:
            encrypted_text += char                          # 不加密其他字元，直接添加到結果中

    return encrypted_text

    # 解密則需要提供相反的替換表
    # 需要注意的是，替換表必須是雙射，即每個字元只能對應一個唯一的字元，否則無法解密




# 柵欄加密（Rail Fence）

def RailFence(text: str, key: int) -> str:
    rail = [['\n' for i in range(len(text))] for j in range(key)]  # 創建一個空的柵欄
    dir_down = None
    row, col = 0, 0

    for char in text:
        if row == 0:                                               # 如果在第一行，則開始向下移動
            dir_down = True
        if row == key - 1:                                        # 如果在最後一行，則開始向上移動
            dir_down = False

        rail[row][col] = char                                      # 將字元放入柵欄中
        col += 1

        if dir_down:                                              # 根據方向移動到下一行
            row += 1
        else:
            row -= 1

    encrypted_text = ""
    for i in range(key):                                         # 按行讀取柵欄中的字元
        for j in range(len(text)):
            if rail[i][j] != '\n':
                encrypted_text += rail[i][j]

    return encrypted_text


    #柵欄解密
def DERailFence(cipher: str, key: int) -> str:
    rail = [['\n' for i in range(len(cipher))] for j in range(key)]  # 創建一個空的柵欄
    dir_down = None
    row, col = 0, 0

    for char in cipher:
        if row == 0:                                               # 如果在第一行，則開始向下移動
            dir_down = True
        if row == key - 1:                                        # 如果在最後一行，則開始向上移動
            dir_down = False

        rail[row][col] = '*'
        col += 1

        if dir_down:                                              # 根據方向移動到下一行
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(key):                                         # 按行讀取柵欄中的字元
        for j in range(len(cipher)):
            if (rail[i][j] == '*' and index < len(cipher)):
                rail[i][j] = cipher[index]
                index += 1

    result = []
    row, col = 0, 0

    for i in range(len(cipher)):
        result.append(rail[row][col])                            # 將字元放入結果中
        col += 1

        if row == 0:                                             # 如果在第一行，則開始向下移動
            dir_down = True
        if row == key - 1:                                      # 如果在最後一行，則開始向上移動
            dir_down = False

        if dir_down:
            row += 1
        else:
            row -= 1

    return "".join(result)                                       # 返回解密後的字串




# 培根加密（Bacon）
def Bacon(text: str) -> str:
    bacon_dict = {
        'A': 'AAAAA', 'B': 'AAAAB', 'C': 'AAABA', 'D': 'AAABB',
        'E': 'AABAA', 'F': 'AABAB', 'G': 'AABBA', 'H': 'AABBB',
        'I': 'ABAAA', 'J': 'ABAAA', 'K': 'ABAAB', 'L': 'ABABA',
        'M': 'ABABB', 'N': 'ABBAA', 'O': 'ABBAB', 'P': 'ABBBA',
        'Q': 'ABBBB', 'R': 'BAAAA', 'S': 'BAAAB', 'T': 'BAABA',
        'U': 'BAABB', 'V': 'BABAA', 'W': 'BABAB', 'X': 'BABBA',
        'Y': 'BABBB',  # Z: BAAAA
    }

    encrypted_text = ""
    for char in text:
        if char.upper() in bacon_dict:
            encrypted_text += bacon_dict[char.upper()]         # 使用培根密碼進行加密
        else:
            encrypted_text += char                             # 不加密其他字元，直接添加到結果中

    return encrypted_text


    # 培根解密
def DEBacon(text: str) -> str:
    bacon_dict = {
        'AAAAA': 'A', 'AAAAB': 'B', 'AAABA': 'C', 'AAABB': 'D',
        'AABAA': 'E', 'AABAB': 'F', 'AABBA': 'G', 'AABBB': 'H',
        'ABAAA': 'I', 'ABAAB': 'K', 'ABABA': 'L', 'ABABB': 'M',
        'ABBAA': 'N', 'ABBAB': 'O', 'ABBBA': 'P', 'ABBBB': 'Q',
        'BAAAA': 'R', 'BAAAB': 'S', 'BAABA': 'T', 'BAABB': 'U',
        # 省略其他字母的映射
    }

    decrypted_text = ""
    for i in range(0, len(text), 5):                          # 每 5 個字元為一組
        group = text[i:i + 5]
        if group in bacon_dict:
            decrypted_text += bacon_dict[group]               # 使用培根密碼進行解密
        else:
            decrypted_text += group                           # 不加密其他字元，直接添加到結果中

    return decrypted_text




# Base64 編碼
import base64
def Base64(text: str) -> str:
    text_bytes = text.encode('utf-8')                          # 將字串轉換為位元組
    base64_bytes = base64.b64encode(text_bytes)                # 使用 Base64 編碼
    base64_text = base64_bytes.decode('utf-8')                 # 將位元組轉換回字串
    return base64_text

    # Base64 解碼
def DEBase64(text: str) -> str:
    base64_bytes = text.encode('utf-8')                        # 將字串轉換為位元組
    text_bytes = base64.b64decode(base64_bytes)                # 使用 Base64 解碼
    text = text_bytes.decode('utf-8')                          # 將位元組轉換回字串
    return text




# Base32 編碼
def Base32(text: str) -> str:
    text_bytes = text.encode('utf-8')                          # 將字串轉換為位元組
    base32_bytes = base64.b32encode(text_bytes)                # 使用 Base32 編碼
    base32_text = base32_bytes.decode('utf-8')                 # 將位元組轉換回字串
    return base32_text

    # Base32 解碼
def DEBase32(text: str) -> str:
    base32_bytes = text.encode('utf-8')                        # 將字串轉換為位元組
    text_bytes = base64.b32decode(base32_bytes)                # 使用 Base32 解碼
    text = text_bytes.decode('utf-8')                          # 將位元組轉換回字串
    return text








# 幽月保有所有權利
# 2025/04/30