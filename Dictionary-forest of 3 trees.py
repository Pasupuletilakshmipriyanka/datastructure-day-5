#Dictionary(forest of 3 trees:)
families={
    'charley':
    {'sam':{'boxy','rosy'},
     'nila':{'pepsi'}},
    'devi':
    {'tommy':{'tonny'},
     'timmy':{'hamster'},
     'tammy':{'hamster'}},
    'carlos':
    {'diego':'cat','ferret':'fox'}
    }
for parent,children in families.items():
    print(f"{parent} has {len(children)}kids(s):")
    print(f"{' , and '.join([str(child) for child in [*children]])}")
    
         
