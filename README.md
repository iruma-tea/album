# album

## プロジェクトの作成
   ・ django-admin startproject config .

## アプリの作成
   ・ python manage.py startapp <アプリ名>

## 開発サーバの起動
   ・ python manage.py runserver

## モデル作成のステップ
   ・ models.pyでモデルの定義をする
   ・ マイグレーションファイルを作成する
     ・ python manage.py makemigrations
   ・ マイグレーションファイルを元にテーブルを作成する
     ・ python manage.py migrate

## ImageFieldを扱う
   ・ Pillowをインストールする
   　→ pip install pillow
   