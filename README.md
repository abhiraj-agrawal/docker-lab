#!/bin/bash

SEARCH_VALUE="test to search"

for REGION in $(aws ec2 describe-regions \
  --all-regions \
  --query 'Regions[].RegionName' \
  --output text); do

  echo "Checking region: $REGION"

  for SECRET in $(aws secretsmanager list-secrets \
    --region "$REGION" \
    --query 'SecretList[].Name' \
    --output text 2>/dev/null); do

    VALUE=$(aws secretsmanager get-secret-value \
      --region "$REGION" \
      --secret-id "$SECRET" \
      --query 'SecretString' \
      --output text 2>/dev/null)

    if echo "$VALUE" | grep -qi "$SEARCH_VALUE"; then
      echo "✅ Match found | Region: $REGION | Secret: $SECRET"
    fi

  done
done
