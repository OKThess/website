#!/usr/bin/env bash

if [ $TRAVIS_BRANCH == "staging" ]; then
    echo "Deployment for staging starting..."
    ssh-keyscan -H staging.okthess.gr >> ~/.ssh/known_hosts
    git push dokku@138.68.74.50:staging staging
else
    echo "Not on staging, deployment canceled."
fi
