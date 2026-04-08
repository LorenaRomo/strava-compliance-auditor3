import streamlit as st

# 1. BASE DE DATOS BILINGÜE CON RECOMENDACIONES TÉCNICAS
audit_content = {
    "Español": {
        "title": "⚖️ Strava Compliance Auditor Pro 2026",
        "tabs": ["📚 Marco Legal", "🔍 Auditoría de Cláusulas", "📱 Evaluación de Funcionalidades", "🚀 Recomendaciones Senior"],
        "sidebar_info": "Auditora: Lorena (Nala)\n\nEspecialidad: LegalTech & Compliance",
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
        "clauses_data": {
            "1. Estructura Contractual": {
                "hallazgo": "Doble entidad contratante y arbitraje obligatorio fuera de UE.",
                "fundamento": "Directivas Consumo UE / Ley California.",
                "analisis": "La renuncia a acciones colectivas es nula en la UE, pero efectiva en el resto. Riesgo de indefensión.",
                "recomendacion": "Utilizar el Art. 80 para blindar la acción colectiva mediante mandatos a organizaciones. Aplicar el Art. 3 para someter a la empresa a jurisdicción europea si trata datos en la UE.",
                "score": 55
            },
            "2. Propiedad Intelectual": {
                "hallazgo": "Licencia perpetua incluso tras borrar la cuenta.",
                "fundamento": "Art. 17 RGPD (Derecho al Olvido).",
                "analisis": "Vulnera el espíritu del Art. 17. Strava se apropia de IP con fines comerciales perpetuos.",
                "recomendacion": "El Derecho al Olvido (Art. 17) prevalece sobre propiedad perpetua. El consentimiento no debe contener 'cláusulas abusivas' (Considerando 42).",
                "score": 95
            },
            "3. Datos de Salud": {
                "hallazgo": "Procesamiento de VFC y ritmo cardíaco mediante integraciones.",
                "fundamento": "Art. 9 RGPD (Categorías Especiales).",
                "analisis": "Uso de consentimiento explícito viciado por falta de granularidad.",
                "recomendacion": "Datos de salud son 'categorías especiales' (Art. 9). Según Art. 7(4), no se puede supeditar el contrato (GPS) a la cesión de biometría.",
                "score": 92
            },
            "4. IA & ML": {
                "hallazgo": "Entrenamiento de modelos con datos de usuario.",
                "fundamento": "Art. 22 RGPD / AI Act.",
                "analisis": "Requiere consentimiento independiente que la cláusula genérica no satisface.",
                "recomendacion": "Entrenar modelos sin aviso viola el Art. 5.1.b. Se requiere consentimiento diferenciado para cada fin, incluyendo biometría (Considerando 32).",
                "score": 88
            },
            "5. Geolocalización (Opt-out)": {
                "hallazgo": "Configuración pública por defecto (Opt-out).",
                "fundamento": "Art. 25.2 RGPD (Privacidad por Defecto).",
                "analisis": "Incumple el mandato de privacidad desde el diseño al publicar rutas por defecto.",
                "recomendacion": "Implementar Art. 25.2: la configuración debe ser Opt-in (privado por defecto). El modelo público por defecto es ilegal.",
                "score": 85
            },
            "6. Responsabilidad & IA": {
                "hallazgo": "Límite de indemnización de 50 USD.",
                "fundamento": "Derecho de Daños / Responsabilidad Civil.",
                "analisis": "Cláusula leonina inoponible ante daños personales causados por errores de IA.",
                "recomendacion": "Cláusulas que limiten responsabilidad económica son inválidas frente al Art. 82, que garantiza indemnización total por daños.",
                "score": 70
            },
            "7. Cumplimiento DSA": {
                "hallazgo": "Obligaciones de moderación de contenidos activas.",
                "fundamento": "Digital Services Act (2026).",
                "analisis": "Cumplimiento formal, pero Strava debe mejorar la transparencia algorítmica.",
                "recomendacion": "Obligatorio designar un DPO (Art. 37) y realizar una EIPD (Art. 35) para mitigar riesgos antes del tratamiento a gran escala.",
                "score": 30
            }
        }
    },
    "English": {
        "title": "⚖️ Strava Compliance Auditor Pro 2026",
        "tabs": ["📚 Legal Framework", "🔍 Clause Audit", "📱 Feature Evaluation", "🚀 Senior Recommendations"],
        "sidebar_info": "Auditor: Lorena (Nala)\n\nSpecialty: LegalTech & Compliance",
        "risk_label": "Numerical Risk Score",
        "analysis_label": "👁️ In-depth Legal Analysis",
        "remedy_label": "✅ Technical and Legal Recommendation (GDPR)",
        "legal_header": "Regulatory Framework (GDPR)",
        "legal_main_warning": "**GDPR Art. 83.5:** Critical violations carry fines up to **20M EUR** or **4% turnover**.",
        "legal_sections": {"Principles (Art. 5)": "Focus on Minimization, Purpose, Storage and Transparency.", "Consent (Art. 6/7)": "Must be withdrawable.", "Special (Art. 9)": "Health data prohibited by default.", "Transparency": "Concise info.", "Privacy (Art. 25/32)": "Privacy by default.", "Rights": "Access, Erasure, Portability."},
        "clauses_data": {
            "1. Contractual Structure": {
                "hallazgo": "Dual entity (Ireland/USA). Mandatory arbitration.",
                "fundamento": "EU Consumer Law / California Law.",
                "analisis": "Class action waiver is void in EU but effective elsewhere. Risk for Latam users.",
                "recomendacion": "Leverage Article 80 for collective actions. Apply Article 3 for EU jurisdiction if processing EU data.",
                "score": 55
            },
            "2. Intellectual Property": {
                "hallazgo": "Perpetual license even after deletion.",
                "fundamento": "Art. 17 GDPR (Right to Olvido).",
                "analisis": "Violates Art. 17. Strava appropriates IP for commercial use permanently.",
                "recomendacion": "Right to Erasure (Art. 17) overrides perpetual ownership. Consent must not contain unfair terms (Recital 42).",
                "score": 95
            },
            "3. Health Data": {
                "hallazgo": "HRV and sleep processing via integrations.",
                "fundamento": "Art. 9 GDPR (Special Categories).",
                "analisis": "Explicit consent use lacking granularity for health features.",
                "recomendacion": "Health data (Art. 9) processing is prohibited unless explicit consent. Art. 7(4) prevents conditional biometrics.",
                "score": 92
            },
            "4. AI & ML": {
                "hallazgo": "Model training with user data.",
                "fundamento": "Art. 22 GDPR / AI Act.",
                "analisis": "Requires independent consent that generic terms do not satisfy.",
                "recomendacion": "Training without notice violates Art. 5.1.b. Separate consent required for biometrics (Recital 32).",
                "score": 88
            },
            "5. Geolocation": {
                "hallazgo": "Public by default settings (Opt-out).",
                "fundamento": "Art. 25.2 GDPR (Privacy by Default).",
                "analisis": "Breaches privacy-by-design mandate by publishing routes by default.",
                "recomendacion": "Implement Art. 25.2: settings must be Opt-in. Public by default model is illegal.",
                "score": 85
            },
            "6. Liability & AI": {
                "hallazgo": "50 USD liability limit.",
                "fundamento": "Tort Law / Civil Liability.",
                "analisis": "Unconscionable clause, unenforceable for personal injury caused by AI errors.",
                "recomendacion": "Liability limits are invalid under Art. 82, which guarantees full compensation for material/non-material damages.",
                "score": 70
            },
            "7. DSA Compliance": {
                "hallazgo": "Content moderation obligations active.",
                "fundamento": "Digital Services Act (2026).",
                "analisis": "Formal compliance, but lacks algorithmic transparency.",
                "recomendacion": "Mandatory DPO (Art. 37) and DPIA (Art. 35) to mitigate risks before large-scale tracking.",
                "score": 30
            }
        }
    }
}

# LÓGICA DE INTERFAZ
st.set_page_config(page_title="Nala Compliance Pro", layout="wide")
idioma = st.sidebar.selectbox("🌐 Language / Idioma", ["Español", "English"])
txt = audit_content[idioma]
st.sidebar.markdown("---")
st.sidebar.info(txt["sidebar_info"])

st.title(txt["title"])
tab1, tab2, tab3, tab4 = st.tabs(txt["tabs"])

with tab1:
    st.header(txt["legal_header"])
    st.error(txt["legal_main_warning"])
    st.markdown("---")
    for section_title, section_body in txt["legal_sections"].items():
        with st.expander(section_title):
            st.markdown(section_body)

with tab2:
    col_list, col_view = st.columns([1, 2])
    with col_list:
        st.subheader("Cláusulas / Clauses")
        seleccion = st.radio("Puntos de fricción:", list(txt["clauses_data"].keys()))
    with col_view:
        datos = txt["clauses_data"][seleccion]
        st.subheader(seleccion)
        st.error(f"**Hallazgo / Finding:** {datos['hallazgo']}")
        st.warning(f"**Fundamento / Basis:** {datos['fundamento']}")
        with st.expander(txt["analysis_label"], expanded=True):
            st.write(datos['analisis'])
        # NUEVA SECCIÓN DE RECOMENDACIÓN DINÁMICA
        st.success(f"**{txt['remedy_label']}:**\n\n{datos['recomendacion']}")
        st.subheader(txt["risk_label"])
        st.metric(label="Score", value=f"{datos['score']}%")
        st.progress(datos['score'] / 100)

with tab3:
    st.header("📱 Evaluación de Funcionalidades vs RGPD")
    # (Textos OCR previos conservados)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 🏥 Biometría (Art. 9)\n* **Esfuerzo Relativo:** Algoritmo predictivo.\n* **Análisis:** Consentimiento 'Explícito'.")
    with col2:
        st.markdown("### 📍 Geolocalización (Art. 25)\n* **Beacon:** Seguimiento.\n* **Análisis:** Traslado de riesgo.")
    with col3:
        st.markdown("### 🤖 IA Contextual (AI Act)\n* **Sugerencia de Rutas:** Entrenamiento.\n* **Análisis:** Riesgo reputacional.")

with tab4:
    st.header("🚀 Dictamen Final para Contratación")
    st.success("Conclusión Senior: Strava 2026 presenta un modelo basado en la expropiación de datos biométricos. Valor agregado: mitiga sanciones del 4% del facturación global.")
