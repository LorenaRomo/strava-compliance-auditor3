import streamlit as st

# 1. BASE DE DATOS CON TEXTO LITERAL COMPLETO
audit_content = {
    "Español": {
        "title": "⚖️ Strava Compliance Auditor Pro 2026",
        "tabs": ["📚 Marco Legal", "🔍 Auditoría de Cláusulas", "📱 Evaluación de Funcionalidades", "🚀 Conclusiones"],
        "sidebar_info": "Auditor: ROMO Sandra\n\nEspecialidad: LegalTech & Compliance",
        "risk_label": "Puntuación de Riesgo Numérica",
        "analysis_label": "👁️ Análisis Técnico-Jurídico Profundo",
        "remedy_label": "✅ Recomendación Técnica y Jurídica (RGPD)",
        "legal_header": "Fundamentación Normativa Máxima (RGPD)",
        "legal_main_warning": "**Art. 83.5 RGPD:** Infracciones críticas conllevan multas de hasta **20M EUR** o el **4% de la facturación global anual**.",
        "legal_sections": {
            "Principios Fundamentales (Art. 5)": "Estructura en torno a: Minimización, Limitación de Finalidad, Conservación y Licitud/Transparencia.",
            "El Consentimiento (Art. 6 y 7)": "Debe ser demostrable y tan fácil de retirar como de dar.",
            "Categorías Especiales (Art. 9)": "Datos de salud prohibidos por defecto; requieren consentimiento explícito.",
            "Transparencia (Art. 12 y 13)": "Información concisa y clara sobre el responsable y perfiles.",
            "Privacidad y Seguridad (Art. 25 y 32)": "Privacidad por defecto y medidas de seguridad (cifrado) según el riesgo.",
            "Derechos de los Usuarios (Art. 15, 17 y 20)": "Acceso, Supresión (Olvido) y Portabilidad en formato mecánico."
        },
        "final_verdict": "Conclusión Senior: Strava 2026 presenta un modelo basado en la expropiación de datos biométricos. Valor agregado: mitiga sanciones del 4% del facturación global.",
        "conclusion_completa": """
(Artículo 5) Principios fundamentales del tratamiento de datos La aplicación debe estructurar su funcionamiento en torno a los principios básicos del tratamiento:
Minimización de datos: Los datos solicitados deben ser adecuados, pertinentes y limitados a lo necesario en relación con los fines para los que son tratados.
Limitación de la finalidad: Los datos (como rutas o ritmo cardíaco) deben recogerse con fines determinados, explícitos y legítimos, y no ser tratados de manera incompatible con dichos fines.
Limitación del plazo de conservación: Los datos deben conservarse de forma que se permita identificar al usuario durante no más tiempo del necesario para los fines del tratamiento.
Licitud, lealtad y transparencia: Los datos personales deben tratarse de manera lícita, leal y transparente en relación con el usuario.
(Artículos 6 y 7) El consentimiento como base legitimadora
Licitud y demostración: Para que el tratamiento sea lícito, generalmente dependerá de que el usuario dé su consentimiento para fines específicos. El responsable de la aplicación debe ser capaz de demostrar que el usuario consintió el tratamiento.
Facilidad para retirarlo: El reglamento exige explícitamente que el interesado tiene derecho a retirar su consentimiento en cualquier momento y que "será tan fácil retirar el consentimiento como darlo".
(Artículo 9) Tratamiento de categorías especiales de datos personales
Al tratarse de una aplicación deportiva que puede registrar información relativa a la salud o datos biométricos, entra en el tratamiento de "categorías especiales", el cual está prohibido por defecto.
Para que la aplicación pueda tratar estos datos sensibles, el usuario debe dar su consentimiento explícito para dichos fines.
(Artículos 12 y 13) Transparencia y el deber de informar (Políticas de Privacidad)
La aplicación debe tomar medidas para que toda información dirigida al usuario sea concisa, transparente, inteligible y de fácil acceso, utilizando un lenguaje claro y sencillo.
En el momento de recopilar los datos, se debe informar al usuario sobre la identidad del responsable, los fines y la base jurídica del tratamiento, los destinatarios a los que se comunicarán los datos, el plazo de conservación previsto, y la existencia de elaboración de perfiles automatizados.
(Artículos 25 y 32) Privacidad desde el diseño, por defecto y Seguridad
Privacidad por defecto (Artículo 25): El responsable de la app debe aplicar medidas técnicas y organizativas para garantizar que, por defecto, solo se traten los datos personales necesarios y que estos no sean accesibles, sin la intervención de la persona, a un número indeterminado de individuos (vital en redes sociales deportivas).
Seguridad del tratamiento (Artículo 32): Se debe garantizar un nivel de seguridad adecuado al riesgo, incluyendo medidas como la seudonimización y el cifrado de los datos personales.
(Artículos 15, 17 y 20) Garantía de los Derechos de los Usuarios El responsable del tratamiento tiene la obligación de facilitar al usuario el ejercicio de sus derechos:
Derecho de acceso (Artículo 15): El derecho del usuario a obtener confirmación de si se están tratando sus datos y acceder a detalles como los fines, categorías de datos, plazos y destinatarios,.
Derecho de supresión o "derecho al olvido" (Artículo 17): La capacidad de que el usuario exija la eliminación de sus datos sin dilación indebida cuando retire el consentimiento o ya no sean necesarios para los fines originales,.
Derecho a la portabilidad (Artículo 20): El derecho a recibir sus datos personales (rutas, tiempos, etc.) en un formato estructurado, de uso común y lectura mecánica, para poder transmitirlos a otra aplicación o responsable sin impedimentos
        """
    },
    "English": {
        "title": "⚖️ Strava Compliance Auditor Pro 2026",
        "tabs": ["📚 Legal Framework", "🔍 Clause Audit", "📱 Feature Evaluation", "🚀 Conclusions"],
        "sidebar_info": "Auditor: ROMO Sandra\n\nSpecialty: LegalTech & Compliance",
        "final_verdict": "Senior Conclusion: Strava 2026 presents a model based on the expropriation of biometric data. Added value: mitigates penalties of 4% of global turnover.",
        "conclusion_completa": "Senior Conclusion: Strava 2026 presents a model based on the expropriation of biometric data. Added value: mitigates penalties of 4% of global turnover.\n\n(Full GDPR analysis based on Art. 5, 6, 7, 9, 12, 13, 15, 17, 20, 25, 32)."
    }
}

# LÓGICA DE INTERFAZ
st.set_page_config(page_title="Romo Compliance Pro", layout="wide")
idioma = st.sidebar.selectbox("🌐 Language / Idioma", ["Español", "English"])
txt = audit_content[idioma]

st.sidebar.markdown("---")
st.sidebar.info(txt["sidebar_info"])
st.sidebar.markdown("### 🛠️ Código Fuente")
st.sidebar.markdown("[View on GitHub](https://github.com/tu-usuario/tu-repositorio)")

st.title(txt["title"])
tab1, tab2, tab3, tab4 = st.tabs(txt["tabs"])

# --- TAB 1, 2 y 3 (Se mantienen según el código original) ---
with tab1:
    st.header(txt["legal_header"])
    st.error(txt["legal_main_warning"])
    for title, body in txt["legal_sections"].items():
        with st.expander(title): st.markdown(body)

# (Aquí iría el código de Tab 2 y 3 que ya tienes)

# --- TAB 4: CONCLUSIONES ---
with tab4:
    st.header(f"🚀 {txt['tabs'][3]}")
    st.success(txt["final_verdict"])
    st.markdown("---")
    # Uso de st.text o st.markdown para el texto literal
    st.markdown(txt["conclusion_completa"])
