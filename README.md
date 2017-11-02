# sebastien-tutorial-python-heroku

sebastienのエキスパートエージェント作成向けのサンプルAPIサーバーです。
使用言語はpythonでflaskアプリをHeroku上でデプロイします。
今回のAPIサーバーはdefault intent以外のintentでサーバーにpostされる全てに対して
"こんにちは" と返すものです。

localのOSはmacです。  
今回はPython3.6を使用します。Pythonのバージョンを変更する場合はruntime.txtを変更してください。

----------------------

## 事前準備
Herokuの[公式ドキュメント](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)を参考してください。
- Herokuのアカウントの作成
- Heroku CLIのインストール  
`$brew install heroku`
- gitのインストール  
`$brew install git`

上記に加えて, sampleを編集してlocal上で変更を行う場合はlocalにpython環境を用意してください。

## directoryを作成, コピー
- 今回はsebastienというdirectoryで作業をします。  
`$ mkdir {path}/sebastien`  
`$ cd {path}/sebastien `  

- git clone してください。  
`$ git clone https://github.com/DinoKGH/sebastien-tutorial-python-heroku.git`  
`$ cd sebastien-tutorial-python-heroku `  

## herokuにアプリをdeploy　　
- gitのバージョン情報登録  
`$ git init`  
`$ git add . `  
`$ git commit -m "first commit" `  

- アプリの作成  
`$ heroku create`    
 または、アプリの名前を指定する場合は   
`$ heroku create hogehoge `  
  
- push  
`$ git push heroku master `  
`$ heroku ps:scale web=1 `  
`$ heroku open `  
 hello world が表示されればdeploy完了




--------------------------------

## DDBでの設定

以上でherokuへのAPIサーバーのデプロイが終了します。     
DDSのボット作成時のendpointに    
`{上記のアプりのURL}/test`  
と入力して保存するとdefault以外のintentの場合, "こんにちは" と答えます。





