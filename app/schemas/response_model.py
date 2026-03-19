ACTA_SCHEMAS = {
    "nacimiento": {
        "datos_del_registro": {
            "fecha_registro": "string", "entidad_federativa": "string", "distrito": "string",
            "municipio": "string", "localidad": "string", "oficialia": "string", "responsable": "string"
        },
        "datos_de_la_acta": {"num_acta": "number", "num_de_control": "number", "libro": "string"},
        "datos_del_ciudadano": {
            "nombre": "string", "primer_apellido": "string", "segundo_apellido": "string",
            "fecha_nacimiento": "string", "clave_registro_identidad_personal": "string", "sexo": "string"
        }
    },
    "matrimonio": {
        "datos_del_registro": {
            "fecha_registro": "string", "entidad_federativa": "string", "distrito": "string",
            "municipio": "string", "localidad": "string", "oficialia": "string", "responsable": "string"
        },
        "datos_de_la_acta": {"num_acta": "number", "num_de_control": "number", "libro": "string"},
        "datos_del_contrayente_1": {
            "nombre": "string", "primer_apellido": "string", "segundo_apellido": "string", "sexo": "string",
            "clave_registro_identidad_personal": "string", "curp": "string", "edad": "number"
        },
        "datos_del_contrayente_2": {
            "nombre": "string", "primer_apellido": "string", "segundo_apellido": "string", "sexo": "string",
            "clave_registro_identidad_personal": "string", "curp": "string", "edad": "number"
        }
    },
    "defuncion": {
        "datos_del_registro": {
            "fecha_registro": "string", "entidad_federativa": "string", "distrito": "string",
            "municipio": "string", "localidad": "string", "oficialia": "string", "responsable": "string"
        },
        "datos_de_la_acta": {"num_acta": "number", "num_de_control": "number", "libro": "string"},
        "datos_del_finado": {
            "nombre": "string", "primer_apellido": "string", "segundo_apellido": "string",
            "edad_fallecimiento": "number", "sexo": "string", "nacionalidad": "string"
        }
    }
}