Eduardo Camozzato Fonte - 00326194
Bernardo Boeira - 00303704

Hiper-parâmetros iniciais:

B = 2
W = 1
Alpha = 0.004
Num_iterations = 10000

EQM Final: 8.527708190984436
Função: 1.1606251498976714*x + -3.4500303192966237

Síntese:
O modelo de regressão linear, inicializado com hiper parâmetros pseudo-aleatórios (baseado em uma observação básico dos dados), conseguiu ajustar os dados para que uma função de saída fosse formalizada. A estratégia se deu pelo uso do Gradiente Descendente na qual escolhemos uma taxa de aprendizado pequena para garantir a estabilidade da "descida" no tratamento da função de custo, sendo assim, o modelo final está ajustado, pois os resultados com 10000 iterações foram  próximos dos resultados com 1000000 de iterações (na casa de 10^-9 de precisão).

