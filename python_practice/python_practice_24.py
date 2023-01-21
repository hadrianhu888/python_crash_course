import Restaurant
from Restaurant import Restaurant as rest
flavors = ['chocolate', 'vanilla']
class IceCreamStand(rest):    
    def __self__(self, flavors):
        self.flavor = flavors 
    def displayFlavours(self,flavors):
        for f in flavors: 
            self.flavors = f
            print ('Ice cream shop flavors: \n\n')
            print(self.flavors)
        
def main(): 
    flavor = 'chocolate'
    TestIceCreamStand = IceCreamStand('TestIceCreamStand', flavor)    
    TestIceCreamStand.displayFlavours(flavors)
    
if __name__ == "__main__":
    main()
    

    
        
