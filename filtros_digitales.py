# =================================================
# PROYECTO: IMPLEMENTACIÓN Y EVALUACIÓN
# DE FILTROS DIGITALES
# =================================================

# LIBRERIAS
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# =================================================
# 1. DEFINICIÓN DE PARAMETROS
# =================================================

frecuencia_muestreo = 1000
duracion = 2
t = np.arange(0, duracion, 1 / frecuencia_muestreo)

# ==================================================
# 2. CREACION DE LA SEÑAL ORIGINAL
# ==================================================

senal = (
    np.sin(2 * np.pi * 5 * t) +
    0.7 * np.sin(2 * np.pi * 50 * t) +
    0.5 * np.sin(2 * np.pi * 150 * t)
)

# AGREGAR RUIDO
ruido = 0.5 * np.random.randn(len(t))
senal_ruidosa = senal + ruido

# ===================================================
# 3. GRAFICAR SEÑAL ORIGINAL
# ===================================================

plt.figure(figsize=(12, 5))
plt.plot(t, senal_ruidosa)
plt.title("Señal original con ruido")
plt.xlabel("Tiempo (segundos)")
plt.ylabel("Amplitud")
plt.grid()
plt.show()

# ==================================================
# 4. DISEÑO DE FILTROS DIGITALES
# ==================================================

# FILTRO PASA BAJOS
sos_bajos = signal.butter(
    4, 20, btype="lowpass",
    fs=frecuencia_muestreo, output="sos"
)

# FILTRO PASA ALTOS
sos_altos = signal.butter(
    4, 80, btype="highpass",
    fs=frecuencia_muestreo, output="sos"
)

# FILTRO PASA BANDAS
sos_bandas = signal.butter(
    4, [40, 70], btype="bandpass",
    fs=frecuencia_muestreo, output="sos"
)

# =================================================
# 5. APLICACION DE LOS FILTROS
# =================================================

# APLICAR FILTRO PASA BAJOS 
senal_pasa_bajos = signal.sosfiltfilt(
    sos_bajos, senal_ruidosa
)

# APLICAR FILTRO PASA ALTOS
senal_pasa_altos = signal.sosfiltfilt(
    sos_altos, senal_ruidosa
)

# APLICAR FILTRO PASA BANDAS
senal_pasa_bandas = signal.sosfiltfilt(
    sos_bandas, senal_ruidosa
)

# =================================================
# 6. VISUALIZACION DE LOS RESULTADOS
# =================================================

plt.figure(figsize=(12, 10))

# SEÑAL ORIGINAL
plt.subplot(4, 1, 1)
plt.plot(t, senal_ruidosa)
plt.title("Señal original con ruido")
plt.ylabel("Ampltud")
plt.grid()

# FILTRO PASA ALTOS
plt.subplot(4, 1, 2)
plt.plot(t, senal_pasa_bajos)
plt.title("Filtro pasada bajos")
plt.ylabel("Amplitud")
plt.grid()

# FILTRO PASA ALTOS
plt.subplot(4, 1, 3)
plt.plot(t, senal_pasa_altos)
plt.title("Filtro pasada altos")
plt.ylabel("Amplitud")
plt.grid()

# FILTRO PASA BANDAS
plt.subplot(4, 1, 4)
plt.plot(t, senal_pasa_bandas)
plt.title("Filtro pasada bandas")
plt.xlabel("Tiempo (segundos)")
plt.ylabel("Amplitud")
plt.grid()

plt.tight_layout()
plt.show()

# ================================================
# 7. RESPUESTA EN FRECUENCIA 
# ================================================

plt.figure(figsize=(12, 8))

# RESPUESTA DEL FILTRO PASA BAJOS
frecuencias, respuesta = signal.sosfreqz(
    sos_bajos, worN=2048, fs=frecuencia_muestreo
)

plt.subplot(3, 1, 1)
plt.plot(frecuencias, 20 * np.log10(np.maximum(np.abs(respuesta), 1e-10)))
plt.title("Respuesta en frecuencia - pasa bajos")
plt.ylabel("Ganancia (dB)")
plt.grid()

# RESPUESTA DE FILTRO PASA ALTOS
frecuencias, respuesta = signal.sosfreqz(
    sos_altos, worN=2048, fs=frecuencia_muestreo
)

plt.subplot(3, 1, 2)
plt.plot(frecuencias, 20 * np.log10(np.maximum(np.abs(respuesta), 1e-10)))
plt.title("Respuesta en frecuencia - pasa altos")
plt.ylabel("Ganancia (dB)")
plt.grid()

# RESPUESTA DEL FILTRO PASA BANDAS
frecuencias, respuesta = signal.sosfreqz(
    sos_bandas, worN=2048, fs=frecuencia_muestreo
)

plt.subplot(3, 1, 3)
plt.plot(frecuencias, 20 * np.log10(np.maximum(np.abs(respuesta), 1e-10)))
plt.title("Respuesta en frecuencia - pasa bandas")
plt.xlabel("Fracuencia (Hz)")
plt.ylabel("Ganancia (dB)")
plt.grid()

plt.tight_layout()
plt.show()

# ================================================
# 8. EVALUACION DE LOS FILTROS
# ================================================

# CALCULAR LA POTENCIA DE CADA SEÑAL 
potencia_original = np.mean(senal_ruidosa ** 2)
potencia_bajos = np.mean(senal_pasa_bajos ** 2)
potencia_altos = np.mean(senal_pasa_altos ** 2)
potencia_bandas = np.mean(senal_pasa_bandas ** 2)

# MOSTRAR RESULTADOS
print("\n===== EVALUACION DE FILTROS DIGITALES =====")

print("Pontencia de la señal original:", potencia_original)
print("Potencia después del pasa bajos:", potencia_bajos)
print("Potencia después del pasa altos:", potencia_altos)
print("Potencia después del pasa bandas:", potencia_bandas)

# CALCULAR REDUCCION DE POTENCIA
reduccion_bajos = (1 - potencia_bajos / potencia_original) * 100
reduccion_altos = (1 - potencia_altos / potencia_original) * 100
reduccion_bandas = (1 - potencia_bandas / potencia_original) * 100

print("\n===== REDUCCION DE POTENCIA =====")

print("Pasa bajos:", reduccion_bajos, "%")
print("Pasa altos:", reduccion_altos, "%")
print("Pasa bandas:", reduccion_bandas, "%")

# ===============================================
# 9. DISEÑO DE FILTROS FIR
# ===============================================


# FILTRO FIR PASA BAJOS 
fir_bajos = signal.firwin(
    101, 20, fs=frecuencia_muestreo,
    pass_zero="lowpass"
)

# FILTRO FIR PASA ALTOS 
fir_altos = signal.firwin(
    101, 80, fs=frecuencia_muestreo,
    pass_zero="highpass"
)

# FILTRO FIR PASA BANDAS 
fir_bandas = signal.firwin(
    101, [40, 70], fs=frecuencia_muestreo,
    pass_zero="bandpass"
)

# ===============================================
# 10. APLICACIÓN DE FILTROS FIR
# ===============================================

# APLICAR FILTRO FIR PASA BAJOS
senal_fir_bajos = signal.filtfilt(
    fir_bajos, [1.0], senal_ruidosa
)

# APLICAR FILTRO FIR PASA ALTOS
senal_fir_altos = signal.filtfilt(
    fir_altos, [1.0], senal_ruidosa
)

# APLICAR FILTRO FIR PASA BANDAS
senal_fir_bandas = signal.filtfilt(
    fir_bandas, [1.0], senal_ruidosa
)

# ===============================================
# 11. COMPARACION DE FILTROS FIR 
# ===============================================

plt.figure(figsize=(12, 9))

plt.subplot(3, 1, 1)
plt.plot(t, senal_fir_bajos)
plt.title("Filtro FIR pasa bajos")
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(t, senal_fir_altos)
plt.title("Filtro FIR pasa altos")
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(t, senal_fir_bandas)
plt.title("Filtro FIR pasa bandas")
plt.xlabel("Tiempo (segundos)")
plt.grid()

plt.tight_layout()
plt.show()

# ===============================================
# 12. EVALUACION DE FILTROS FIR 
# ===============================================

potencia_fir_bajos = np.mean(senal_fir_bajos ** 2)
potencia_fir_altos = np.mean(senal_fir_altos ** 2)
potencia_fir_bandas = np.mean(senal_fir_bandas ** 2)

print("\n===== EVALUACION DE FILTROS FIR =====")
print("Potencia FIR pasa bajos:", potencia_fir_bajos)
print("Potencia FIR pasa altos:", potencia_fir_altos)
print("Potencia FIR pasa bandas:", potencia_fir_bandas)

# ===============================================
# 13. COMPARACION DE RESPUESTA EN FRECUENCIA
# ===============================================

plt.figure(figsize=(12, 9))

# Comparacion pasa bajos
f_fir, h_fir = signal.freqz(fir_bajos, worN=2048, fs=frecuencia_muestreo)
f_iir, h_iir = signal.sosfreqz(sos_bajos, worN=2048, fs=frecuencia_muestreo)

plt.subplot(3, 1, 1)
plt.plot(f_fir, 20 * np.log10(np.maximum(np.abs(h_fir), 1e-10)), label="FIR")
plt.plot(f_iir, 20 * np.log10(np.maximum(np.abs(h_iir), 1e-10)), label="IIR")
plt.title("Comparacion pasa bajos")
plt.ylabel("Magnitud (dB)")
plt.legend()
plt.grid()

# Comparacion pasa altos
f_fir, h_fir = signal.freqz(fir_altos, worN=2048, fs=frecuencia_muestreo)
f_iir, h_iir = signal.sosfreqz(sos_altos, worN=2048, fs=frecuencia_muestreo)

plt.subplot(3, 1, 2)
plt.plot(f_fir, 20 * np.log10(np.maximum(np.abs(h_fir), 1e-10)), label="FIR")
plt.plot(f_iir, 20 * np.log10(np.maximum(np.abs(h_iir), 1e-10)), label="IIR")
plt.title("Comparacion pasa altos")
plt.ylabel("Magnitud (dB)")
plt.legend()
plt.grid()

# Comparacion pasa bandas
f_fir, h_fir = signal.freqz(fir_bandas, worN=2048, fs=frecuencia_muestreo)
f_iir, h_iir = signal.sosfreqz(sos_bandas, worN=2048, fs=frecuencia_muestreo)

plt.subplot(3, 1, 3)
plt.plot(f_fir, 20 * np.log10(np.maximum(np.abs(h_fir), 1e-10)), label="FIR")
plt.plot(f_iir, 20 * np.log10(np.maximum(np.abs(h_iir), 1e-10)), label="IIR")
plt.title("Comparacion pasa bandas")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud (dB)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

# ===============================================
# 14. CONCLUSIION DE ANALISIS 
# ===============================================

print("\n===== CONCLUSION DE ANALISIS =====")
print("Se diseñaron y aplicaron filtros digitales FIR e IIR.")
print("Los filtros pasa bajos conservaron principalmente las frecuencias bajas.")
print("Los filtros pasa altas conservaron principlamente las frecuencias altas.")
print("Los filtros pasa bandas permitieron conservar un rango específico de frecuencias.")
print("Las graficas permitieron comparar el comprtamiento de ambos metodos.")
print("Los resultados muestran que FIR e IIR pueden reducir el ruido de una señal,")
print("aunque su comportamiento depende del diseño y de las frecuencias de corte.")