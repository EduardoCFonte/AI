#   LAB 1 IA

## Alunos

Eduardo Camozzato Fonte - 00326194
Bernardo Boeira - 00303704

#   Regressão Linear

## Hiper-parâmetros iniciais

B = 2
W = 1
Alpha = 0.004
Num_iterations = 10000

##  Valores Finais

EQM Final: 8.527708190984436
Função: 1.1606251498976714*x + -3.4500303192966237

##  Síntese:
O modelo de regressão linear, inicializado com hiper parâmetros pseudo-aleatórios (baseado em uma observação básico dos dados), conseguiu ajustar os dados para que uma função de saída fosse formalizada. A estratégia se deu pelo uso do Gradiente Descendente na qual escolhemos uma taxa de aprendizado pequena para garantir a estabilidade da "descida" no tratamento da função de custo, sendo assim, o modelo final está ajustado, pois os resultados com 10000 iterações foram  próximos dos resultados com 1000000 de iterações (na casa de 10^-9 de precisão).

#   Redes Neurais

Datasets
- CIFAR-10  Classes: 10 Amostras: 60.000  Tamanho: 32x32 pixels  Canais de cor: 3
- CIFAR-100 Classes: 100  Amostras: 60.000  Tamanho: 32x32 pixels  Canais de cor: 3
- MNIST-> Classes: 10  Amostras: 70.000  Tamanho: 28x28 pixels  Canais de cor: 1
- Fashion MNIST-> Classes: 10  Amostras: 70.000 Tamanho: 28x28 pixels  Canais de cor: 1

##  Complexidade 

- MNIST:
Uma vez que as imagens que tem menor resolução e só variações de cinza, é o mais fácil.       
- FASHION MNIST: 
Um pouco mais complexo que o MNIST pois seus conjunto de calsses consta com diferentes tipos de roupas.
- CIFAR-10:
Mais difícil pois possui maior resolução (32 x 32) contra (28x28) das classes anteriores, possui cor em RGB, e suas classes tem alguns aspectos comuns tipo passáro e avião que tem um fundo em comum.
- CIFAR-100:  
O mais complexo pois possui 100 classes, resolução alta, cores em RGB e consequentemente classes parecidas como tipos de animais parecidos.




## Conclusao:      

Para os datasets, os melhores resultados foram:

- MNIST: 98.17% de acurácia em 35.05 segundos. A rede com três camadas convolucionais, Dropout de 0.5 e Adam otimizou o desempenho.
- Fashion MNIST: 90.28% em 117.4 segundos, usando camadas mais profundas e Batch Normalization para estabilidade.
- CIFAR-10: 10% em 64.05 segundos, indicando a necessidade de ajustes mais avançados para essa tarefa.
- CIFAR-100: 35.36% em 84.97 segundos, com uma rede profunda (64 a 512 filtros) e taxa de aprendizado reduzida para melhorar o ajuste.
A normalização entre [0, 1] e o uso de Dropout ajudaram a regularizar e estabilizar o treinamento em todos os conjuntos.


