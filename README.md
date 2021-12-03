# Python Integration Test Example

This is simple example of a integration test suite built in pytest. 



## Target Service
An example target serice has been created to exerice the pytest framework. There are intentional errors/issue within the code.

### Operations

GET
```
curl -X GET  http://127.0.0.1:5000/
```


POST
```
curl -X POST http://127.0.0.1:5000 -d '{"model": "aaa", "year": "99", "miles": 123}'
```


DELETE
```
curl -X DELETE  http://127.0.0.1:5000/NJKBKLSNKJJ
```


