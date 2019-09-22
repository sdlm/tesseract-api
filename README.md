# tesseract-api
Web server with tesseract engine for OCR

# request for test api
```
http -f POST http://localhost:8000/extract file@data/test-european.jpg
```

# run image by
```
docker run -p 80:80 sdlmer/tesseract-api
```
