import chardet

# Определяем кодировку
with open("cats.json", "rb") as f:
    raw = f.read()
    result = chardet.detect(raw)
    encoding = result["encoding"]

# Перекодируем
text = raw.decode(encoding)

# Сохраняем в новой UTF-8 версии
with open("cats_utf.json", "w", encoding="utf-8") as f:
    f.write(text)