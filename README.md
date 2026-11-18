Implementación y evaluación de filtros digitales

Descripción del proyecto
Este proyecto tiene como objetivo diseñar, implementar y evaluar filtros digitales utilizando Python. Se trabaja con una señal compuesta por diferentes frecuencias y ruido aleatorio para observar cómo los filtros permiten modificar y mejorar una señal.

Se implementaron filtros digitales FIR e IIR para analizar su comportamiento y comparar sus resultados.

Objetivos
  Diseñar filtros digitales pasa bajos, pasa
  altos y pasa bandas.
  Implementar filtros FIR e IIR.
  Aplicar los filtros con una señal con ruido.
  Analizar las señales antes y después del filtrado.
  Comprar las respuestas en frecuencias de ambos métodos.
  Evaluar los resultados mediante gráficas y cálculos de potencias.

Herramientas utilizadas
  Python 3.
  NumPy.
  SciPy.
  Matplotlib.
  Visual Studio aCode.

Tipos de filtros implementados
Filtros IIR
Se utilizaron fltros Butterworth de cuatro orden para implementar.
  Pasa bajos.
  Pasa altos.
  Pasa bandas.

Filtros FIR
Se utilzaron filtros basados en la función firwin, con una ventana de diseño de 101 coeficientes, para implementar:
  Pasa bajos.
  Pasa altos.
  Pasa bandas.

Señal utilizada
Se generó una señal compuesta por tres componentes sinusoidales de 5 Hz, 50 HZ y 150 HZ. Posteriormente, se agregó ruido aleatorio pasa simular una señal.

Evaluación de resultados 
Se analizaron las señales filtradas gráficas en el dominio del tiempo y respuestas en frecuencia.
También de calcularon las potencias de las señales para evaluar la reducción obtenida después de aplicar los filtros.
Los resultados permitieron observar diferencias entre los métodos FIR e IIR y comprobar que cada filtro conserva diferentes rangos de frecuencia según su diseño.

Cómo ejecutar el proyecto
 1. Instalar Python.
 2. Instalar las bibliotecas necesarias.

 Python -m pip install numpy scipy matplotlib

3. Abrir la carpeta del proyecto en Visual Studio Code.
4. Ejecutar el siguiente comando en la terminal:

python filtros_digitales.py

Conclusión
La implementación permitió comprender el funcionamiento de los filtros digitales y su utilidad para procesar señales con ruido. Mediante los métodos FIR e IIR fue posible diseñar filtros pasa bajos, pasa altos y pasa bandas, observar su respuestas en frecuencia y comparar sus resultados.
El proyecto permitió aplicar conseptos de procesamiento digital de señales y comprobar cómo las herramientas de Python facilitan el análisis y la evaluación de diferentes técnicas de filtrado. 