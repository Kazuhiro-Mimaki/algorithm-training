# Algorithm

## アルゴリズム役立ち資料
- [実践・最強最速のアルゴリズム勉強会　第一回　講義資料(ワークスアプリケーションズ & AtCoder)](https://www.slideshare.net/chokudai/wap-atcoder1)
- [実践・最強最速のアルゴリズム勉強会　第二回　講義資料(ワークスアプリケーションズ & AtCoder](https://www.slideshare.net/chokudai/wap-atcoder2)
- [AtCoder に登録したら次にやること ～ これだけ解けば十分闘える！過去問精選 10 問 ～](https://qiita.com/drken/items/fd4e5e3630d0f5859067)
- [アルゴリズムとデータ構造](https://www.codereading.com/algo_and_ds/)
- [10 Algorithms To Solve Before your Python Coding Interview](https://towardsdatascience.com/10-algorithms-to-solve-before-your-python-coding-interview-feb74fb9bc27)
- [leetcode](https://leetcode.com/problemset/all/)

## python役立ち資料
- [Python3の標準入力やり方まとめ](https://qiita.com/yasu_teco/items/e8db933ac4f647166996)
- [競プロ等におけるpython3の標準入力](https://qiita.com/zenrshon/items/c4f3849552348b3dbe67)

## python 標準入力テクニック

### 1行に1つの文字列
```python
str = input()
```

### １行に１つの数値（整数もしくは浮動小数点数）の場合
```python
int = int(input())
```

### １行に複数の数値（整数もしくは浮動小数点数）の場合
```python
a,b = map(int, input().split())　# "A B"と空白区切りで数値が入力されるのを受け取る
```