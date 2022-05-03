from rocrate.rocrate import ROCrate
from rocrate.model.person import Person
from rocrate.model.file import File 
from rocrate.model.dataset import Dataset 

import time
import sys

def main(argv):
    times = argv[0]
    start = time.time()
    crate = ROCrate()
    for i in range(int(times)):
    # Person entity
        #file = crate.add_file('example'+str(i))
        person = Person(crate, 'id'+str(i), {'name': 'Joe Bloggs'})
        file = crate.add_file('./data/file'+str(i), 'file'+str(i), fetch_remote = True)
        file['author'] = person
        crate.add(file)
        crate.add(person)
    
    end = time.time();
    print(times + " " + str(end-start))
    
    with open('mix_py.txt', 'a') as the_file:
        the_file.write(str(end-start)+'\n')

   # out_path = "./test"
   # crate.write(out_path)

if __name__ == "__main__":
   main(sys.argv[1:])


