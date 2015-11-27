def search(s, p):                  
    matches = []
    p_length = len(p)               
    p_end    = len(p) - 1           

    i = j = p_end                   
                                   
    k = 0  

    while i < len(s):
        if s[i].lower() == p[j].lower():
            k = i                   
            while j > 0:           
                i -= 1
                j -= 1

                if s[i].lower() != p[j].lower():
                    i = k + p_end
                    j = p_end
                    break

            if j == 0:              
                matches.append(i)
                i = k + p_end
                j = p_end
        else:
            try:
                mpos = p.rindex(s[i]) 
                shift = p_end - mpos   
                i += shift
                continue
            except ValueError:        
                i += p_length          
                continue

    return matches

def radixsort( aList ):
  RADIX = 10
  maxLength = False
  tmp , placement = -1, 1

  while not maxLength:
    maxLength = True
    # declare and initialize buckets
    buckets = [list() for _ in range( RADIX )]

 
    for  i in aList:
      tmp = i // placement
##      print ("i is " , i)
##      print ("placement is " , placement)
##      print ("tmp is ", tmp)
##      print ("tmp % RADIX is ", tmp % RADIX)
      buckets[tmp % RADIX].append( i )
      if maxLength and tmp > 0:
        maxLength = False

    
    a = 0
    for b in range( RADIX ):
      buck = buckets[b]
      for i in buck:
        aList[a] = i
        a += 1

    # move to next digit
    placement *= RADIX
  return aList


if __name__ == "__main__":

 #flag=0  
##    s = 'here is a simple example'
##    p = 'jump'

    with open('product.txt') as f:
        ArrayList = f.readlines()
    s= [ x[:-1] for x in ArrayList ]
flag=0
p=raw_input("Product Search - Input your keyword : ")
while(flag==0):
    

    key=p.split()

    line=0
    sort=['']*len(s)
    bit1=[0]*len(s)
    bit2=[0]*len(s)
    bit3=[0]*len(s)
    print ('%-4s %-35s %10s %10s %10s') % ("ID","Name of product","Matching Keyword","Position","Distance")
    for i in range(0,len(s)):
    
        y=search(s[i],key[1])
        x=search(s[i],key[0])
    
        if(x!=[] or y!=[]):
            line=i
            num=1
            xx=0
            yy=0

        
            if(x!=[]):
                xx=int(x[0])
                posi=x
                bit1[i]='2'
                bit2[i]+=x[0]
            
            
            else:
                xx=0
                posi=y

            
            if(y!=[]):
                yy=int(y[0])
                bit1[i]='3'
                bit2[i]+=y[0]
            
     
            else:
                yy=0

            
            if(x!=[] and y!=[]):
                num=2
                distance=abs(xx-yy)
                bit1[i]='1'
                bit2[i]+=x[0]
                bit3[i]=distance
       
                #print s[i],x,y,num,posi,distance
                sort[i]=str(bit1[i])+str(bit2[i]).zfill(3)+str(bit3[i]).zfill(3)+str(line).zfill(4)
                print ('%-4d %-35s %10d %10s %10d') % (i,s[i], num,posi[0],distance)
            #   print sort[i]
            else:
                bit3[i]=999
                sort[i]=str(bit1[i])+str(bit2[i]).zfill(3)+str(bit3[i]).zfill(3)+str(line).zfill(4)
                print ('%-4d %-35s %10d %10s          - ') % (i,s[i], num,posi[0])
           #    print sort[i]
            #   print s[i],num,posi,'-'



    sort = [x for x in sort if x != '']
    sort = map(int,sort)
    radixsort(sort)
    lenn=len(radixsort(sort))

    conf=raw_input('Do you want to set Command-line Argument Y / N :')
    if(conf=='Y'):
        Argument=input(('\nEnter line Argument [1-%d]  : ')%(lenn))
        while(Argument>lenn or Argument<0):
            Argument=input(('\nEnter line Argument again[1-%d]  : ')%(lenn))
            
    else:
        Argument=10
        print '\nnot in range ..  \nDEFAULT is 10 \n'
    

    for i in range(0,Argument):
           
            index = sort[i] % 10000
            print i+1,'-',s[index]

    p=raw_input("\nProduct Search - Input your keyword [Q to exit]: ")
    if(p=='Q'):
        flag=1


    
        
    
