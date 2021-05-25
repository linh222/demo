#!/usr/bin/env sh

cd $HELM_CHART_PATH

helm secrets upgrade --install lead_scoring_api ./lead_scoring_api --wait \
  --timeout 600s \
  --set-string lead_scoring_api.image.tag=$CI_COMMIT_SHORT_SHA \
  --namespace=lead_scoring_api \
  --create-namespace \
  -f $environment/$environment-values.yaml \
  -f $environment/secrets.yaml \
