# TEFAS Price API

Minimal FastAPI service that returns daily prices of TEFAS funds.

TEFAS fonlarının günlük fiyatını döndüren minimal FastAPI servisi.

## Usage / Kullanım

```
GET /price?symbol=TLE
```

Response / Yanıt:

```json
{
  "symbol": "TLE",
  "title": "AURA PORTFÖY YABANCI BORÇLANMA ARAÇLARI FONU",
  "price": 26.51,
  "date": "2026-05-04"
}
```

## Running / Çalıştırma

### Local / Lokal

```bash
pip install fastapi uvicorn tefas-crawler
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Docker

```bash
docker build -t tefas-api .
docker run -p 8000:8000 tefas-api
```
