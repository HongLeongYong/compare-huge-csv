# CSV 大文件比較工具

這是一個專為比較大小可達 50GB 的 CSV 文件而設計的 Python 工具。

## 目標 🎯
- 對比兩個大型 CSV 文件
- 根據指定的 key 進行對比

## 開始之前
在使用本工具之前，請確保您已安裝 pandas 套件。如果尚未安裝，可以使用以下指令進行安裝：

```bash
pip install pandas
```

在使用本工具之前，請先設定 `src/global_variable.py` 中的以下變數：
1. `before_huge_csv_file` - 原始 CSV 文件的路徑
2. `after_huge_csv_file` - 後續 CSV 文件的路徑
3. `header` - CSV 文件的表頭

## 使用步驟

所有源碼都放置在 src/ 目錄下。

### 拆分 CSV
如果需要，您可以使用 `src/split_csv.py` 將大型 CSV 文件拆分為多個較小的 CSV 文件。每個拆分的文件將包含原始文件的表頭。

```bash
python src/split_csv.py
```

### 計算行數
執行 `src/count_row.py` 以計算 "before" 和 "after" 的 CSV 文件的行數。

```bash
python src/count_row.py
```

### 比較 CSV
執行 `src/compare.py` 以進行兩個 CSV 文件的比較。

```bash
python src/compare.py
```

## 許可證
本項目使用 MIT 許可證，詳情請參見 [LICENSE](LICENSE) 文件。
