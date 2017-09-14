#!/bin/bash
env=$1
domain=$2

if [[ -d "/apps/oracle_$env" ]]; then
  domain_home="/apps/oracle_$env/Middleware/user_projects/domains/domain_$domain"
  echo "found directory /apps/oracle_$env"

  if [[ -d "$domain_home" ]]; then
    echo "Directory $domain_home exists."
    echo "Changing directory to  to pack.sh location..."

    cd "/apps/oracle_$env/Middleware/oracle_common/common/bin"
  #pwd
    ./pack.sh -domain=$domain_home -template="/tmp/$domain.jar" -managed=true -template_name="domain_$domain"
  else
    echo "Could not find directory $domain_home"
    echo "Exiting..."
    exit
  fi
else
  echo "Did not find directory /apps/oracle_$env"
  echo "Exiting..."
  exit
fi
