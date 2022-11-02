# openssl-tools

### Overview
This is a collection of simple utilities in the context of recently discovered CVE-2022-3602, CVE-2022-3786, allowing to answer the following questions:

### 1. Does my server require client authentication

Running the following command
```
python openssl_req_client_cert.py HOST_NAME PORT
```
Will determine whether client authentication is required by the SSL server, in which case servers based on OpenSSL 3.0.0..3.0.6 will be vulnerable to CVEs above [https://jfrog.com/knowledge-base/upcoming-openssl-3-x-critical-vulnerability/]

For example:
```
|ψ> python openssl_req_client_cert.py 127.0.0.1 12345
127.0.0.1:12345 -> Client certificate not required
```



