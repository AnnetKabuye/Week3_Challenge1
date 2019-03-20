lista=[]
def list_sort(lista): 
    even_nos=[]
    odd_nos =[]
    characters=[] 
    pass
    sorted_dict={"evens":[],"odds":[],"chars":[]}
    for n in lista:
        if isinstance(n,int):
            if n%2==0:    
                even_nos.append(n)
            elif n%2==1:   
                odd_nos.append(n)
        elif isinstance(n,str):     
            characters.append(n)
        sorted_dict["evens"]=sorted(even_nos)
        sorted_dict["odds"]=sorted(odd_nos)
        sorted_dict["chars"]=sorted(characters)
            
    print (sorted_dict)
list_sort([2,6,7,9,10,'a', 'z','r'])    
    
    

