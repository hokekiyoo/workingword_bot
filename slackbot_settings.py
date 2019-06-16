# coding: utf-8

with open("TOKEN.text") as f:
    TOKEN = f.read()

# botアカウントのトークンを指定
API_TOKEN = TOKEN

# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = "HELLO, SOMETHING WRONG"

# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']

