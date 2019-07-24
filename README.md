# Rasa chatbot exemplo
Um simple chatbot de exemplo utilizando o Rasa

## Como usar

### Instalando o Rasa
```
pip install rasa
```

### Trainamento da NLU
```
rasa train
```

### Rodando chatbot via terminal
```
rasa shell
```
*Você pode ativar o debug utilizando o camando ```rasa shell --debug```*


### Permitindo que as actions funcione
Para utilizar as actions personalizadas como o exemplo da idade do bot, é necessário rodar o endpoint. Para isso rode em um terminal separado, ou em background o comando
```
rasa run actions
```
