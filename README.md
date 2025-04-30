# Encrypt_Package

#### 由 **幽月YuYue** 所設計，`EncryptLib` 是一套輕量級的 Python 函式庫，提供多種**字串加密、解密、雜湊與編碼功能**，適用於學習、開發與安全驗證等場景



# 套用 :
### 將此.py檔案放到專案跟目錄資料夾中
### 在專案中輸入 :
    import EncryptLib as el
### 以引用套件


## 以下為本套件包提供之加密方法
  - **凱薩加密（Caesar）**
  ```bash
    - 加密: el.Caesar(str, int)
    - 解密: el.Caesar(str, -int)
  ```
  - **ROT13**
  ```bash
    - 加密: el.ROT13(str)
    - 解密: el.ROT13(str)
  ```
  - **Atbash 加密**
  ```bash
    - 加密: el.Atbash(str)
    - 解密: el.Atbash(str)
  ```
  - **Affine 線性加密**
  ```bash
    - 加密: el.Affine(str, a, b)
    - 解密: el.Affine(str, a, b)
  ```
  - **維吉尼亞加密（Vigenère）**
  ```bash
    - 加密: el.Vigenere(str, key)
    - 解密: el.Vigenere(str, key)
  ```
  - **自定替換加密**
  ```bash
    - 加密: el.Substitution(str, dict)
    - 解密: el.Substitution(str, dict)
  ```
  - **柵欄加密（Rail Fence）**
  ```bash
    - 加密: el.RailFence(str, int)
    - 解密: el.EDRailFence(str, int)
  ```
  - **培根密碼（Bacon）**
  ```bash
    - 加密: el.Bacon(str)
    - 解密: el.DEBacon(str)
  ```
  - **Base64 編碼**
  ```bash
    - 加密: el.Base64(str)
    - 解密: el.DEBase64(str)
  ```
  - **Base32 編碼**
  ```bash
    - 加密: el.Base32(str)
    - 解密: el.DEBase32(str)
  ```
