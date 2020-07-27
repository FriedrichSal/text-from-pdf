# Test-from-pdf

This projects if for fetching text from a url. Content type can be html or pdf.

## Getting started

Build the docker image by

```
docker build -t url2text:latest .
```

Then start the service by

```
docker run -p 8080:80 url2text:latest
```

Now test the service by querying

```
http://localhost:8080/textforurl?url=<your url to html or pdf content>
```

for example

```
http://localhost:8080/textforurl?url=https://arxiv.org/pdf/2003.03384.pdf```
