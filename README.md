# TEFAS Price API

Minimal FastAPI service that returns daily TEFAS fund prices. Also serves as an MCP tool via SSE.

TEFAS fonlarının günlük fiyatını döndüren minimal FastAPI servisi. SSE üzerinden MCP tool olarak da kullanılabilir.

## REST API

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

## MCP (Model Context Protocol)

The server exposes an MCP SSE endpoint at `/mcp/sse` with the `get_fund_price` tool.

Sunucu `/mcp/sse` adresinde `get_fund_price` tool'unu sunar.

### Claude Desktop / Claude Code Configuration

Add to your MCP config (`claude_desktop_config.json` or `.claude/settings.json`):

Claude Desktop veya Claude Code MCP ayarlarınıza ekleyin:

```json
{
  "mcpServers": {
    "tefas": {
      "url": "http://localhost:8000/mcp/sse"
    }
  }
}
```

### Available Tools / Mevcut Araçlar

| Tool | Parameters | Description |
|------|-----------|-------------|
| `get_fund_price` | `symbol` (string) | Get today's price for a TEFAS fund / Bir TEFAS fonunun günlük fiyatını getirir |

Example symbols / Örnek semboller: `TLE`, `YAC`, `IPB`

## Running / Çalıştırma

### Local / Lokal

```bash
pip install fastapi uvicorn tefas-crawler "mcp[cli]"
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Docker

```bash
docker build -t tefas-api .
docker run -p 8000:8000 tefas-api
```

## Disclaimer

This project is not affiliated with, endorsed by, or connected to TEFAS or any official institution. Fund data is fetched from publicly available sources and provided "as is" without any warranty. Do not use this data for financial decisions without independent verification.

Bu proje TEFAS veya herhangi bir resmi kurumla bağlantılı değildir. Fon verileri kamuya açık kaynaklardan çekilmekte olup herhangi bir garanti verilmemektedir. Bu verileri bağımsız doğrulama yapmadan finansal kararlar için kullanmayınız.

## License / Lisans

[MIT](LICENSE)
