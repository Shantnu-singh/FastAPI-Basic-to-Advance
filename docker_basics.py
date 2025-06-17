# Docker --> contanisation
# for consistancy across env
# Isolation --> on same server mutiple server
# Sacalabilty --> deplyemnet across mutiple server
# How does this works?
# docker (demon core -> Rest APi Core -> CLI )
# Docker image 1) Base image 2) application code 3 ) dependecis 4) metadata

# Lifecycle of docker image 1) creation 2) stroage 3) distribution 4) execustion
# Docker file -> set of instrction to build docker image layer by layer
# docker container -> instace of docker image that run in the host system
# docker registry -> servicve that store and distibutre doker images 
# docker hub -> most known public repo for docker images
# docker regitsry -> 1) tag 2) repos -> collection of docker imges
# types of docker registry -> public ( docker hub) , private (org) , 3rd pary (ecr -> amazon)
# why-> version control , colloboation , seccuty , 

# lifecyle -> dockerfile ->built -> image created -> run -> container ( if okay) -> push in repo - > registry -> someone pull ( from registrty) - > run -> container
# use of docker -> microservices articheture -> each feature has diff code 2) cicd 3)cloud migration 4) scable web application 5) testing and QA 6) ML and Ai 6) API dev and deployamnet

# docker desktop -> docker engine (demoan , CLI , docker API) , GUI(saw images and containers , other stuff , uses docker API)