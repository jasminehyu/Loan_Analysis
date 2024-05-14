import zipfile
import json
from io import TextIOWrapper
import csv

race_lookup = {
    "1": "American Indian or Alaska Native",
    "2": "Asian",
    "3": "Black or African American",
    "4": "Native Hawaiian or Other Pacific Islander",
    "5": "White",
    "21": "Asian Indian",
    "22": "Chinese",
    "23": "Filipino",
    "24": "Japanese",
    "25": "Korean",
    "26": "Vietnamese",
    "27": "Other Asian",
    "41": "Native Hawaiian",
    "42": "Guamanian or Chamorro",
    "43": "Samoan",
    "44": "Other Pacific Islander"
}


    
class Applicant:
    def __init__(self, age, race):
        self.age = age
        self.race = set()
        for r in race:
            if r in race_lookup:
                self.race.add(race_lookup[r])  #set() is mutable like list.append()-update automatically
            else:
                continue
      
    def __repr__(self):
        return f"Applicant('{self.age}', {sorted(list(self.race))})"

    def lower_age(self):
        new_string= self.age.replace(">","").replace("<","")
        return int(new_string.split('-')[0])
    
    def __lt__(self, other):
        return self.lower_age() < other.lower_age()

class Loan:
    def __convert_to_float(self,values):
        if values in ['NA','Exempt']:
            return -1
        else:
            return float(values)
            
    def __find_race(self,values):
        empty=list()
        for keyword in values:
            if keyword.startswith("applicant_race") and keyword != "applicant_race_observed" :
                if values[keyword]=="":
                    continue
                empty.append(values[keyword])
        return empty
        
    def __find_co_race(self,values):
        empty=list()
        for keyword in values:
            if keyword.startswith("co-applicant_race") and keyword !="coapplicant_race_observed":
                if values[keyword]=="":
                    continue
                empty.append(values[keyword])
        return empty
        
    def __init__(self, values):
        self.loan_amount = self.__convert_to_float(values["loan_amount"])
        self.property_value=self.__convert_to_float(values['property_value'])
        self.interest_rate=self.__convert_to_float(values['interest_rate'])
        list_of_race=self.__find_race(values)
        self.applicants=[Applicant(values["applicant_age"],list_of_race)]
        if values["co-applicant_age"] != "9999":
            list_of_co_race=self.__find_co_race(values)
            self.applicants.append(Applicant(values["co-applicant_age"],list_of_co_race))
        self.applicant_num=len(self.applicants)
            
    def __str__(self):
        return f"<Loan: {self.interest_rate}% on ${self.property_value} with {self.applicant_num} applicant(s)>"
         
    def __repr__(self):
        return f"<Loan: {self.interest_rate}% on ${self.property_value} with {self.applicant_num} applicant(s)>"
        
    def yearly_amounts(self, yearly_payment):    #公开方法（Public Methods），意味着它们是供类的外部使用的。
        # TODO: assert interest and amount are positive
        assert (self.interest_rate)/100>=0 and self.loan_amount>=0
        amt = self.loan_amount
        interest=(self.interest_rate)/100

        while amt > 0:
            yield(amt)
        # TODO: add interest rate multiplied by amt to amt
            with_multiply_interest=amt+amt*interest
        # TODO: subtract yearly payment from amt
            amt=with_multiply_interest-yearly_payment
            
    
class Bank:
            
    def __init__(self,bank_name):
        with open('banks.json','r') as file:
            trans_to_dict= json.load(file)
                
        found=False
        for item in trans_to_dict:
            name=item['name']
                
            if bank_name==name:
                print('find it')
                self.name=name
                self.lei=item['lei']
                found=True
                break    
                    
        if not found:                
            raise ValueError(f"{bank_name} does not exist in banks.json")
            
                   
    def load_from_zip(self,path):
        with zipfile.ZipFile(path, 'r') as zf:
            with zf.open("wi.csv") as f:
                reader = csv.DictReader(TextIOWrapper(f))
                self.list=[]
                for dic in reader:
                     if dic['lei'] == self.lei:
                            information = Loan(dic) 
                            self.list.append(information) 
                            
    def average_interest_rate(self):
        interest_rate=0
        num=0
        for item in self.list:
            each_inrate= item.interest_rate
            interest_rate+=each_inrate
            num+=1
            
        return interest_rate / num
        
                
        avg_interest_rate= interest_rate/num
    
    def num_applicants(self):
        num_of_applicant=0
        for item in self.list:
            num_of_applicant+=item.applicant_num
        return num_of_applicant/ len(self.list)
            
                       
    def __len__(self):
            return len(self.list)
        
    def __getitem__(self,position):  #uwcu[position],Python internally calls uwcu.__getitem__(position) 
            return self.list[position]                    
                    
    def ages_dict(self):
        empty_dict={}
        for item in self.list:
            for item in item.applicants:
                age=item.age
                if age in ['8888','9999']:
                    continue
                if not str(age) in  empty_dict:
                    empty_dict[str(age)]=0
                empty_dict[str(age)]+=1
        return empty_dict
    
class Node:
    def __init__(self, key):
        self.key = key
        self.values = []
        self.left = None
        self.right=None
        
    def lookup(self,key):
        if key == self.key:
            return len(self.values)
        elif key < self.key:
            if self.left !=None:
                return self.left.lookup(key)
        elif key>self.key:
            if self.right !=None:
                 return self.right.lookup(key)
        return []
    
    def get_height(self):
        if self.left==None:
            l=0
        else:
            l=self.left.get_height()
        if self.right==None:
            m=0
        else:
            m=self.right.get_height()
        return max(l,m)+1
    
    def num_nonleaf_nodes(self):
        num=0
        if self.left!=None or self.right!=None:
            num+=1
        if self.left!= None:
            num+=self.left.num_nonleaf_nodes()
        if self.right!=None:
            num+=self.right.num_nonleaf_nodes()
        return num
            
                   
class BST:
    
    def __init__(self):
        self.root = None
    
    def add(self, key, val):
        if self.root==None:
            self.root= Node(key)
        current=self.root
        while True:
            if key < current.key:
                # go left
                if current.left == None:
                    current.left = Node(key)
                current = current.left
            elif key > current.key:
                 # go right
                if current.right==None:
                    current.right=Node(key)
                current=current.right
            else:
                # found it!
                assert current.key == key
                break

        current.values.append(val)
        
    def __getitem__(self, key):
        return self.root.lookup(key)
    
    def find_top_n(self, node, n, result):
        if node is not None and len(result) < n:
            self.find_top_n(node.right, n, result)
            if len(result) < n:
                result.append(node.key)
            self.find_top_n(node.left, n, result)

    def top_n_interest_rates(self,n):
        result = []
        self.find_top_n(self.root, n, result)
        if len(result) == n:
            return result[-1] 
        