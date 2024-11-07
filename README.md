## pyxel 日本語ドキュメント

https://github.com/kitao/pyxel/blob/main/docs/README.ja.md

## pyxel 公式リポジトリ

https://github.com/kitao/pyxel

## pyxel のインストール

```bash
brew install pipx
pipx ensurepath
pipx install pyxel
```

## サンプルの生成

```bash
pyxel copy_examples
```

## 初回起動

```bash
cd pyxel_examples
pyxel run 01_hello_pyxel.py
# => bash: pyxel: command not found

pip install pyxel
# => 'pyxel' already seems to be installed. Not modifying existing installation in '/Users/username/.local/pipx/venvs/pyxel'. Pass

/Users/username/.local/pipx/venvs/pyxel/bin/pyxel run 01_hello_pyxel.py
# => 実行OK

echo 'export PATH=/Users/username/.local/pipx/venvs/pyxel/bin:$PATH' >> ~/.bash_profile
source ~/.bash_profile
# => 見つけた実行ファイルにpyxelコマンドでpathを通す

pyxel run 01_hello_pyxel.py
# => 実行OK

pyxel play 30sec_of_daylight.pyxapp
# => 実行OK
```
