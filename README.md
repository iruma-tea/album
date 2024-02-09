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
   
## 管理者画面の設定
   ・ python manage.py createsuperuser
      ・ ユーザー名： admin
      ・ パスワード: 0
   ・ http://127.0.0.1:8000/admin
   ・ アプリ(album)/admin.pyの編集
     → 管理画面からテーブル(model)のデータの参照、登録、更新、削除が可能となる。

## フリー画像の掲載サイト
   ・ O-DAN https://o-dan.net/ja/
            https://unsplash.com/photos/73pyV0JJOmE
            
## フォーム要素にclassを追加するライブラリ
   ・ pip install django-widget-tweaks