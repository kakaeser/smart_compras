from supermercado import *

#Classes dentro de Setores: Limpeza, Hortifruti, Lacticinios, HigienePessoal, Açougue, Bebidas, Padaria, Biscoitos

limpeza_1 = Limpeza (["Detergente", "Sabão em pó"])
hortifruti_1 = Hortifruti (["Banana", "Melão", "Maçã", "Uva"])
lacticinios_1 = Lacticinios (["Queijo", "Yogurte"])
higienepessoal_1 = HigienePessoal (["Escova de dente", "Pasta de dente"])
açougue_1 = Açougue (["Filé de peito", "Picanha"])
bebidas_1 = Bebidas ([])
padaria_1 = Padaria ([])
biscoitos_1 = Biscoitos ([])

setor_1 = Setores (limpeza_1, hortifruti_1, lacticinios_1, higienepessoal_1, açougue_1, bebidas_1, padaria_1, biscoitos_1)

endereço_1 = Endereço ("Brasil", "Minas Gerais", "Belo Horizonte", "Minaslândia", "Rua Dourados", 122)

supermercado_1 = Supermercado ("Supermercados BH", setor_1, endereço_1)

publicar_dados(supermercado_1)

