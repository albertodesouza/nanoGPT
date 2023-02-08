= Como tunar a gpt2 para falar portugues (Machado de Assis, na verdade, 
  tirado daqui: https://www.kaggle.com/datasets/rtatman/brazilian-portuguese-literature-corpus?resource=download
  ver livros disponíveis no arquico guideToDocuments.csv neste diretório)

 cd Brazilian_Portugese_Corpus
 cat > A\ Mao\ e\ a\ Luva.txt Casa\ Velha.txt Contos\ Fluminenses.txt Dom\ Casmurro.txt Esau\ e\ Jaco.txt Helena.txt Historias\ da\ Meia-Noite.txt Historias\ Sem\ Data.txt Iaia\ Garcia.txt Memorial\ de\ Aires.txt Memorias\ Postumas\ de\ Bras\ Cubas.txt Paginas\ Recolhidas.txt Papeis\ Avulsos.txt Quincas\ Borba.txt Reliquias\ de\ Casa\ Velha.txt Ressurreicao.txt > ../input.txt
 cd ..
 iconv -f ISO_8859-1 -t UTF-8 < input.txt > output.txt
 mv output.txt input.txt
 python3 prepare.py
 cd ../..
 python3 train.py config/finetune_portugues.py # está configurado para fazer overfitting

Altere sample.py para fazer out_dir = 'out-portugues'
 python3 sample.py

