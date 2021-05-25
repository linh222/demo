#!/usr/bin/env sh

echo "Logging to GitLab Container Registry with CI credentials..."
docker login -u "$CI_REGISTRY_USER" -p "$CI_REGISTRY_PASSWORD" "$CI_REGISTRY"
echo ""

docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA -f $DOCKERFILE .

echo "Pushing to GitLab Container Registry..."
docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA
echo ""


