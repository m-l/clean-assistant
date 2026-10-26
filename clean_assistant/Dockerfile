# App (add-on) de Clean Assistant para Home Assistant.
# La imagen se PRECOMPILA en GitHub Actions con docker buildx (multi-arquitectura) y se publica
# en GHCR (ver .github/workflows/build.yml). Home Assistant la DESCARGA en vez de compilarla en
# el dispositivo -> actualizaciones rápidas y con barra de progreso real.
FROM alpine:3.20

ENV PYTHONUNBUFFERED=1
# tzdata es imprescindible: sin la base de zonas horarias, poner TZ + time.tzset() no surte
# efecto en Alpine y los horarios se disparan con desfase. Ver backend/app.py _apply_host_timezone.
RUN apk add --no-cache python3 py3-pip openssl jq git curl tzdata

# Código a instalar: el tag vX.Y.Z de esta versión (lo pasa el workflow como APP_REF; por defecto
# 'main' para un build manual suelto).
#
# NOTA LOCAL (no subir al PR a upstream): APP_REPO apunta temporalmente a mi fork para poder
# compilar y probar estos cambios en mi propio Home Assistant antes de que se publique una
# imagen oficial. Revertir a miguelsg29/clean-assistant antes de preparar el PR.
ARG APP_REPO=https://github.com/m-l/clean-assistant
ARG APP_REF=main
RUN git clone --depth 1 --branch "${APP_REF}" "${APP_REPO}" /app \
    && pip3 install --no-cache-dir --break-system-packages -r /app/requirements.txt

COPY run.sh /run.sh
RUN chmod a+x /run.sh
CMD [ "/run.sh" ]
