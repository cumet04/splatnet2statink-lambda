# splatnet2statink-lambda

Run [splatnet2statink](https://github.com/frozenpandaman/splatnet2statink) on AWS Lambda every 2 hours

## Requirements
* Node.js: for serverless-framework
  - See `.node-version` for version
* Python3: for build service's packages on local
* AWS account & API key

## Deploy
### 1. Generate `config.txt`
Generate `config.txt` with running splatnet2statink on local.

### 2. Put config.txt on AWS
Make a SSM ParameterStore's parameter with name:`/splatnet2statink/config` and type:SecureString,
and set content of `config.txt` to parameter's value.

### 3. Run deploy
```
npm ci
npm run deploy
```
