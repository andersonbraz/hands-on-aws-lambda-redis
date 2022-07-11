# Hands-on - AWS Lambda + Redis


## Introdução


## Problema


## Solução


### Criar Função Lambda


### Create Function Lambda - 

```shell
aws lambda create-function --function-name MyRedisFunction --timeout 30 --memory-size 1024 \
--zip-file fileb://my-deployment-package.zip --handler app.handler --runtime python3.8 \
--role arn:aws:iam::921154759462:role/lambda-vpc-role \
--vpc-config SubnetIds=subnet-0c50caa13f8b3c617,subnet-019127b26e52b7750,subnet-0fbe8c49114d82025,subnet-0b6fcad83e264535f,subnet-05485c1177bb237fa,subnet-02112d7a91f0e77cd,SecurityGroupIds=sg-0ef09623128a3f72e
```

### Update Function Lambda - Upload Código Lambda

```shell
cd my-math-function
aws lambda update-function-code --function-name MyMathFunction --zip-file fileb://my-deployment-package.zip
```

aws lambda invoke --function-name MyRedisFunction output.txt

## Referência

[Implantar funções do Lambda em Python com arquivos .zip](https://docs.aws.amazon.com/pt_br/lambda/latest/dg/python-package.html)

[Tutorial: configurar uma função do Lambda para acessar o Amazon ElastiCache em uma Amazon VPC](https://docs.aws.amazon.com/pt_br/lambda/latest/dg/services-elasticache-tutorial.html)