from GetImages import extractor as Extractor
from push_extractor_to_xampp import preparator as Preparator
import time


# Filters:
brand = "-sargento -pringles"
package = "-brand -package -container -can"
food = "-burguer -meat -potato -sausage"
additional = "-city -church -house -pearson -airplane -switzerland -country -ball -car -tree"

filters = additional+" "+brand+" "+food+" "+package

cheese_types = [["mozzarella cheese", filters],
                ["parmesan cheese", filters],
                ["cheddar cheese", filters],
                ["gouda cheese", filters],
                ["swiss cheese", filters],
                ["camembert cheese", filters],
                ["feta cheese", filters],
                ["provolone cheese", filters],
                ["edam cheese", filters],
                ["emmental cheese", filters],
                ["gorgonzola cheese", filters],
                ["ricotta cheese", filters],
                ["cottage cheese", filters]]

minimum_number_of_images =  400 # It will save not more than 20 images plus minimum.

# Clean the database/cheese_photos folder before running it.
proceed = str(input("\nDo you wish to execute this script?[yes/no]\n"))

#preparator = Preparator()
#preparator.make()

if proceed == "yes":
    # Close all your chrome tabs. Open just one new tab.
    extractor = Extractor("C:/xampp", cheese_types, minimum_number_of_images)
    extractor.start()

    time.sleep(10)

    extractor.stop_apache()
