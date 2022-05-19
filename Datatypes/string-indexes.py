selfish = 'me me me'
          #01234567-indexes
          print(selfish[0]) #m
       #(start:stop:stepover)
       selfish = '01234567'
       print(selfish[0:2]) #01
       print(selfish[0:8]) #01234567
       print(selfish[1:]) # 1234567
       print(selfish[:5]) #01234
       print(selfish::1) #01234567
       print(selfish[-1]) #76543210-negatrive index means start at the end of the string
       print(selfish[::-1]) # 76543210 - negative two will skip by two in reverse eg(7531)
       