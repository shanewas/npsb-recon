# BangladeshBankNPSB
#beta 1.1.2

# For Windows users# Note: <> denotes changes to be made

#Create a conda environment
conda create --name <environment-name> python=<version:3.8.0>

#To create a requirements.txt file:
conda list #Gives you list of packages used for the environment

conda list -e > requirements.txt #Save all the info about packages to your folder

#To export environment file
activate <environment-name>
conda env export > <environment-name>.yml

#For other person to use the environment
conda env create -f <environment-name>.yml