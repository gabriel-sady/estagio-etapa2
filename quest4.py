'''4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente.
Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser.
Seu objetivo é descobrir qual interruptor controla qual lâmpada.

Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

Resposta:
    Vou aos interruptores e ligo o interrup1 e interrup2 e vou até a sala1:
        
        SE sala1 == escura ENTÃO {
            sala1 = interrup3
            Volto aos interruptores e desligo interrup1 e vou na sala2:
            SE sala2 == escura ENTÃO {sala2 = interrup1, sala3 = interrup2} 
            SENÃO, SE sala2 == iluminada ENTÃO {sala2 = interrup2, sala3 = interrup1}
            }
                        
        SENÃO, SE sala1 == iluminada ENTÃO {
            sala1 != interrup3
            Volto aos interruptores e desligo interrup1 e vou a sala2:
            SE sala2 == iluminada ENTÃO {sala2 = Interruptor 2, sala3 = interrup3, sala1 = interrup1}
            SENÃO, SE sala2 == escura ENTÃO {sala2 = interrup3, sala3 = interrup2, sala1 = interrup1}
 
'''