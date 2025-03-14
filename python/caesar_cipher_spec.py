# Rewrite this in Unit Test

from caesar_cipher import caesar_cipher

# # caesar_cipher("aA", 2)
# caesar_cipher("B", -5)
print(caesar_cipher("Boy! What a string!", -5) == "Wjt! Rcvo v nomdib!")
print(caesar_cipher("Hello zach168! Yes here.", 5) == "Mjqqt efhm168! Djx mjwj.")
print(caesar_cipher("Hello Zach168! Yes here.", -5) == "Czggj Uvxc168! Tzn czmz.")
