Um bot para fazer uma limpeza de dados (acho bom deixar claro que o bot pode apresentar alguma falha, não só isso como se for uma base de dados muito importante para você 
recomendo fazer uma análise melhor), tirando isso basicamente o bot vai remover valores nulos, tirar os outlier e em um nível mais elevado vai deixar os dados pronto para 
fazer um treinamento de machine learning 

--------------------------------------------

A função para tirar os valores nulos vai ser o seguinte, o robô vai mostrar a quantidade de linhas presente no seu data frame ou banco de dados e você vai ter que escolher 
algum número então vamos supor que no seu arquivo tenha mais de 100 linhas, e existem colunas com 99 números nulos e outras com 80 e assim por diante o que o número vai fazer
é pagar o número que você passou e então somar a quantidade de valores nulos em uma coluna e a coluna que estiver com os valores acima d número passado pelo usuário vai ser
deletada 
