# sales.py の total 関数の単体テスト
# 実行方法: py -m unittest -v test_sales

import unittest

from sales import total


class TestTotal(unittest.TestCase):
    # total 関数は「売り上げのリスト」を受け取り、各要素の "金額" を合計して返す

    def test_empty_list_returns_zero(self):
        # 売り上げが1件もない（空のリスト）場合、合計は初期値の 0 になる
        self.assertEqual(total([]), 0)

    def test_single_sale_returns_its_amount(self):
        # 要素が1件だけの場合、その金額がそのまま合計になる
        sales = [{"金額": 1500}]
        self.assertEqual(total(sales), 1500)

    def test_multiple_sales_are_summed(self):
        # 複数件の場合、すべての「金額」を足し合わせた値になる（1000+2000+3000=6000）
        sales = [
            {"金額": 1000},
            {"金額": 2000},
            {"金額": 3000},
        ]
        self.assertEqual(total(sales), 6000)

    def test_zero_amounts_do_not_change_total(self):
        # 金額が 0 の売り上げは合計に影響しないことを確認する（0+500+0=500）
        sales = [{"金額": 0}, {"金額": 500}, {"金額": 0}]
        self.assertEqual(total(sales), 500)

    def test_negative_amount_is_subtracted(self):
        # 負の金額（返品など）を含む場合は、その分が差し引かれることを確認する（1000-300=700）
        sales = [{"金額": 1000}, {"金額": -300}]
        self.assertEqual(total(sales), 700)

    def test_float_amounts_are_summed(self):
        # 小数の金額も合計できることを確認する
        # 浮動小数点の誤差があるため assertEqual ではなく assertAlmostEqual で比較する
        sales = [{"金額": 100.5}, {"金額": 200.25}]
        self.assertAlmostEqual(total(sales), 300.75)

    def test_missing_amount_key_raises_key_error(self):
        # 「金額」キーを持たない要素が含まれる場合は KeyError が発生することを確認する
        # （不正なデータを黙って無視せず、エラーとして知らせる仕様）
        sales = [{"金額": 1000}, {"数量": 2}]
        with self.assertRaises(KeyError):
            total(sales)


if __name__ == "__main__":
    # このファイルを直接実行したときにテストを走らせる
    unittest.main()
