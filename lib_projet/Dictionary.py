Dictionary = {                      # Definition du dictionnaire 
        T1  :  [],                  # La tache T1 n'est precedée par aucune tache
        T2  :  T1,                  # La tache T2 est precedée par la tache 1
        somme  :  [T1,T2]           # La tache somme n'est prècedée par les taches 1 et 2
            }