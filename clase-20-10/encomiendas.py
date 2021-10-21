import persona
import datos_encomun

persona_envia= persona.ingreso()
encomienda=datos_encomun
persona_recibe=persona.ingreso()

#print("la persona %s con DNI %s esta enviando %s a %s con DNI%s"
    #%(persona_envia["nombre"], persona_envia["dni"],encomienda,persona_recibe["dni"] ))


print("%s esta enviando %s a"
    %(persona.ver_datos(persona_envia["nombre"], persona_envia["dni"]),
    encomienda,
    persona.ver_datos(persona_recibe["nombre"], persona_recibe["dni"])))