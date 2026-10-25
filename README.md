# Lumbalgia en Arabia Saudí y dosificación de carga

Sitio estático de Víctor Andrés Gómez López (fisioterapia deportiva y ciencia de datos, Riad).

## Contenido

- `index.html`: Portada con enlaces a las tres versiones y al plan
- `lumbar-saudi-es.html`: Lumbalgia crónica en Arabia Saudí, en español
- `lumbar-saudi-en.html`: La misma página en inglés
- `lumbar-saudi-ar.html`: La misma página en árabe (RTL; pendiente de revisión nativa)
- `plan.html`: Plan del proyecto de dosificación de carga: objetivo, tres módulos (tendinopatía aquílea, isquiosurales, lumbalgia crónica), hoja de ruta de unas 12 semanas, requisitos para un estudio en Riad, riesgos y referencias

Las páginas son HTML autónomo con CSS y JavaScript en línea (animaciones al hacer scroll, barra de progreso, contadores). Respetan `prefers-reduced-motion`. Solo dependen de Google Fonts.

## Cómo reconstruir

Requiere Python 3, sin dependencias externas.

```bash
cd src
python3 build.py
```

`build.py` rellena las plantillas y escribe los cinco HTML en la carpeta raíz:

- `src/common.py`: paleta, CSS y JS compartidos.
- `src/template.html` con `src/es.py`, `src/en.py` y `src/ar.py`: textos de cada idioma de la página de lumbalgia.
- `src/plan_template.html`: plan del proyecto (solo español).
- `src/index_template.html`: portada.

Si falta alguna clave en una plantilla, el script se detiene y la indica.

## Despliegue

Sitio estático sin paso de compilación en Vercel: se sirven los archivos de la raíz tal cual.

## Aviso

Información educativa basada en fuentes publicadas. Las cifras marcadas como sin verificar o tomadas solo del resumen están señaladas en cada página. No es consejo médico.
