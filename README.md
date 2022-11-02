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

### 2. Which files on a local machine contain OpenSSL code of vulnerable versions

Applications running OpenSSL are easy to miss if the library is statically linked into an application binary. 
Running the following command
```
python scan_vulnerable_openssl_code.py ROOT_DIR
```
Will recursively scan ROOT_DIR for ELF files, and report the files which include the pattern `ossl_punycode_decode` (indicative of versions >=3.0.0), while files which in addition include the pattern `ripemd160_newctx` indicative of the updated version (3.0.7) are reported as such.

