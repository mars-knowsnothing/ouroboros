rm -rf ../build/runtime
cd ../build && virtualenv -p /usr/local/bin/python3.9 runtime
cd runtime && source ./bin/activate
mkdir -p temp/python && cd temp/python
pip install -r ../../../$1 -t .
pip freeze > requirements.txt
cd .. && zip -r9 ../$2.zip .
