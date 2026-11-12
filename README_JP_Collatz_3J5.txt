# **Algebraic Formulation of the 3n+5 Collatz Operator in Jacobsthal Space: The 3J + 5J(0,1) Transformation**

**Hiroshi Harada - November 12, 2026**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

## **概要 (Overview)**
本リポジトリは、Collatz予想の拡張モデルである「3n+5 問題」の軌道遷移を、Jacobsthal（J）空間におけるアフィン変換として代数的に定式化した研究レポート、およびその理論を実証するPythonシミュレータを公開するものです。

標準的なCollatz操作をJ空間の2成分列ベクトル（J-Spinor）上で定義し、加法ノイズ `+5` を隔離することで、軌道計算の乗法的成分を明示的に記述する手法を提案しています。

**$$3\boldsymbol{J}(a,b) + 5\boldsymbol{J}(0,1)$$**

このアルゴリズムにより、3n+5空間に存在するすべての既知のループ（1, 5, 19, 23, 187, 347）を、途中で分数を発生させることなく、共通の力学系の枠組みで統一的に記述することが可能となりました。

## **収録ファイル (Files)**
*   `REPORT_EN.md` : 英語版 研究レポート
*   `REPORT_JP.md` : 日本語版 研究レポート
*   `code_01_collatz_3j5.py` : J-Spinor軌道を生成・検証するPythonスクリプト

## **理論的背景 (Theoretical Background)**
本研究のPythonスクリプトは、以下の2つの代数的手法を実装しています。
1.  **J-Reduction（J空間2-adic縮約）**: 軌道の枝を根本まで遡り、分数を生じさせない代表元（Reduced Spinor）を抽出する。
2.  **J-Normalization（J正規化）**: アフィン変換後のベクトルに対し、J数列上の展開（Sequence Expansion）と定数倍（Geometric Scaling）を適用し、次ノードの標準スピノルへ正確に着地させる。

これらの代数的手法により、旧来の「k回の2除算（$1/2^k$）」というスカラー操作の背後にある、位相シフトとスカラー倍の分離構造が明らかになります。

## **実行要件 (Requirements)**
*   Python 3.8 以上
*   `pandas` ライブラリ

## **使用方法 (Usage)**
スクリプトを実行すると、指定した初期奇数ノード（デフォルトは `347`）からのJ-Spinor軌道を計算し、ループを検知するまで自動追跡します。

```bash
# 依存ライブラリのインストール
pip install pandas

# シミュレータの実行
python code_01_collatz_3j5.py

```

実行後、コンソールにMarkdown形式の軌道遷移テーブル（**Table 1**）が出力され、同時に同階層へCSVファイル（例：`collatz_3J5_347.csv`）が保存されます。スクリプト内の `start_node` 変数を変更することで、任意の奇数ノードの軌道を解析可能です。

## **ライセンス (License)**

* **Python Source Code:** MIT License
* **Research Documents:** CC BY 4.0

Copyright (c) 2026 Hiroshi Harada
