# onest-scholarships-com

a platform to curate and discover scholarship and grants via beckn protocol ONEST

# dev setup

1. docker-compose up -d
1. start ngrok tunnels using ngrok.yml as configuration
1. bash node-install.sh
1. create configs/default.yml for each gateway service

3000 - seeker application
5000 - BAP client PS
7000 - BAP network PS

4000 - provider application
6000 - BPP client PS
8000 - BPP network PS
