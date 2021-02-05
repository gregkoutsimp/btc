## Bitcoin Price Chart

#### Introduction 

This repositiry contains the complete definition to builld a Docker Image for Bitcoin Price Chart, available on Docker Hub as `gregkoutsimp/btc`

This images does not run as stand alone. It is a part of a mulit-conatiner docker application.
The requires `YAML` file can be found in this repository.  
The Docker Compose tool is used to run the application.

#### Instructions

Download the `YAML` file and run the `docker-compose up` command. 


#### Development Workflow 

In case changes needed to be made in the code, download the repository. 
Apply changes and then build the new image. The new image must to have the same tag as the previews one. Afterwards, we need to apply the new image name to the `YAML` file.
Otherwise, you can change the *image* command with *build*, in the app section and assign as value the path where the app code is stored. The new image can be created by running the `docker-compose build` command.



