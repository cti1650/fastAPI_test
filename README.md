# fastAPI_test

## fastAPI

### fastAPI導入
```bash
pip install fastapi
pip install "uvicorn[standard]"
```

### サンプル
```python
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
```

### サーバー立ち上げ
```
uvicorn main:app --reload
```

### requirements.txt作成
```plane:requirements.txt
fastapi
```

### Deta 登録
[Deta Cloud](https://www.deta.sh/?ref=fastapi)

### Deta CLIインストール
```
curl -fsSL https://get.deta.dev/cli.sh | sh
```
動作確認
```
deta --help
```

### CLI Login
```
deta login
```

### Deta デプロイ
```
deta new
```

## 参考にしたサイト

- [tiangolo/fastapi: FastAPI framework, high performance, easy to learn, fast to code, ready for production](https://github.com/tiangolo/fastapi)
- [Deta にデプロイ - FastAPI](https://fastapi.tiangolo.com/ja/deployment/deta/)
- [Python Tutorial | Deta Docs](https://docs.deta.sh/docs/base/py_tutorial/?ref=fastapi)
- [DETA](https://web.deta.sh/home/cti1650/default/micros)

