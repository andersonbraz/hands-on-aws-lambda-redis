# Hands-on - AWS Lambda + Redis


## Introdução


## Problema


## Solução

### Step 1

```shell
mkdir my-sample-lambda
```
### Step 2

```shell
touch my-sample-lambda/app.py
```
### Step 3

```python
import boto3
s3 = boto3.resource('s3')
my_bucket = s3.Bucket('braz-bucket-storage')

for my_bucket_object in my_bucket.objects.all():
    print(my_bucket_object)
```

### Step 4

```shell
pip install --target ./my-sample-lambda/package boto3
```

### Step 5

```shell
cd ./my-sample-lambda/package && zip -r ../my-sample-package.zip . && cd ..
```

### Step 6

```shell
zip -g my-sample-package.zip app.py
```

### Step 7

```shell
aws lambda update-function-code --function-name MySample_001 --zip-file fileb://my-sample-package.zip
```

### Step 8

```shell
```

### Criar Função Lambda


```shell
aws lambda create-function --function-name MyRedisFunction --timeout 30 --memory-size 1024 --zip-file fileb://my-deployment-package.zip --handler app.handler --runtime python3.8 --role arn:aws:iam:::role/lambda-vpc-role
```

### Atualizar Código Função Lambda

```shell
cd my-math-function
aws lambda update-function-code --function-name MyMathFunction --zip-file fileb://my-deployment-package.zip
```

aws lambda invoke --function-name MyRedisFunction output.txt

## Referência

[Implantar funções do Lambda em Python com arquivos .zip](https://docs.aws.amazon.com/pt_br/lambda/latest/dg/python-package.html)

[Tutorial: configurar uma função do Lambda para acessar o Amazon ElastiCache em uma Amazon VPC](https://docs.aws.amazon.com/pt_br/lambda/latest/dg/services-elasticache-tutorial.html)