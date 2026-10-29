def total(sales):
    """売り上げの合計金額を返す"""
    result = 0
    for sale in sales: # 中身を繰り返し取り出す
        result += sale["金額"] # sale["金額"]の値をresultにプラスしていく
    return result


sales = [
    {"金額": 1000},
    {"金額": 2000},
]

# result = total(sales) # totalの実行結果をresultに保存 
# print(result) # resultの中身を表示する