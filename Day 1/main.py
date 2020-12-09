filepath = 'text.txt'

with open(filepath) as fp:
   line1 = fp.readline()
   while line1:
       with open(filepath) as fp2:
           line2 = fp2.readline()
           while line2:
               if int(line1) + int(line2) == 2020:
                   print('Answer is '+str(int(line1)*int(line2)))
               line2 = fp2.readline()

       line1 = fp.readline()
