# Merchant's Guide To The Galaxy
This project has been assigned in completion of an assessment to ascertain technical ability.
The language chosen is *Python*. The version of Python tested against is version 3.6.4 but the code should be backwards compatible to all versions of Python 3.
Other than **sys** (in order to extract argument parameters) no packages have been used.

## Assumptions
* It is assumed that L = 50 (the instructions contended L = 250)
* Relationship between the intergalactic currency and roman numerals is first in the file.
* The relationship between intergalactic currency and roman numeral is defined by a sentence of the structure 

          <int_curr> is <rom_num>
          eg: glob is I
* The currency per commodity sentence is defined by a sentence of the structure 

          <value_in_int_curr> <commodity> is <number> Credits
          eg: glob glob Silver is 34 Credits
* The questions are defined by a sentence of the structure

          how many/much Credits is <int_curr> <commodity>?
          eg: how many Credits is glob prok Silver?
or

          how much/many is <int_curr>
          eg: how much is pish tegj glob glob?
