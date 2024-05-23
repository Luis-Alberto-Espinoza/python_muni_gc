# ACTIVIDAD

### **Tamagotchi**

Crea una clase llamada **`Tamagotchi`** que tenga los siguientes atributos:

* **`nombre`**
* **`nivel_energia`** (inicializado en 100)
* **`nivel_hambre`** (inicializado en 0)
* **`nivel_felicidad`** (inicializado en 50)
* `**humor`** (enojado, triste, indiferente, feliz, eufórico) *depende de `**nivel_felicidad**`
* **`esta_vivo`** (inicializado en True)

> Pueden agregar más atributos si lo consideran necesario.

La clase Tamagotchi debe tener los siguientes métodos:

1. **`mostrar_estado`** : Muestra en consola el nombre del Tamagotchi y sus niveles actuales de energía, hambre y estado de humor.
2. **`alimentar`** : Disminuye el nivel de hambre en 10 y disminuye el nivel de energía en 15.
3. **`jugar`** : Aumenta el nivel de felicidad en 20, disminuye el nivel de energía en 18 y aumenta el nivel de hambre en 10.
4. **`dormir`** : Aumenta el nivel de energía en 40 y aumenta el nivel de hambre en 5.

Además, implementa un método llamado **`verificar_estado`** que revise si el Tamagotchi está vivo. Un Tamagotchi está vivo mientras su nivel de energía sea mayor que cero. Si el nivel de hambre llega a 20, cada vez que se realice una acción que no sea `**alimentar**` deberá reducir los puntos de energía en 20 puntos y la felicidad perderá 30 puntos. Si el nivel de energía llega a cero, el Tamagotchi muere y el atributo **`esta_vivo`** debe ser False.

> Pueden agregar otros métodos si desean.
>
> ---
