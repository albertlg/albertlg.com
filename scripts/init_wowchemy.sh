#!/usr/bin/env bash

# Initialize Wowchemy exampleSite files for Hugo Modules-based theme

# Ensure modules are downloaded and vendored locally
hugo mod tidy
hugo mod vendor

# Sync exampleSite configuration and static assets
rsync -av vendor/modules/github.com/wowchemy/wowchemy/v5/exampleSite/config/_default/ config/_default/
rsync -av vendor/modules/github.com/wowchemy/wowchemy/v5/exampleSite/data/ data/
rsync -av vendor/modules/github.com/wowchemy/wowchemy/v5/exampleSite/i18n/ i18n/
rsync -av vendor/modules/github.com/wowchemy/wowchemy/v5/exampleSite/layouts/ layouts/
rsync -av vendor/modules/github.com/wowchemy/wowchemy/v5/exampleSite/static/ static/
rsync -av vendor/modules/github.com/wowchemy/wowchemy/v5/exampleSite/content/ content/