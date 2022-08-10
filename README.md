# IP-cyberattack-visualization

**disclaimer** 
Most of the code of this project is taken from https://github.com/MatthewClarkMay/geoip-attack-map which is made by MatthewClarkMay 

What I have changed are some debugging due to upgrades and using my own data set that is stored in an elasticsearch server rather than generating dummy traffic

### Ubuntu 
This project requires an Ubuntu 20.04.


### to set up: the code is mostly taken from MatthewClarkMay's github

### Deploy example
Tested on Ubuntu 20.04 LTS.

* Download the files of this github:

* Install system dependencies:

  ```sh
  sudo apt install python3-pip redis-server

  ```

* Install python requirements:

  ```sh
  cd geoip-attack-map
  sudo pip3 install -U -r requirements.txt

  ```
  
* Start Redis Server:

  ```sh
  redis-server
  ```
* Configure the Data Server DB:
  
    ```sh
  cd DataServerDB
  ./db-dl.sh
  cd ..

  ```
* Start the Data Server:

    ```sh
  cd DataServer
  sudo python3 DataServer.py

  ```
  
* Start the Syslog Gen Script, inside DataServer directory:

  * Open a new terminal tab (Ctrl+Shift+T, on Ubuntu).
  
    ```sh
    python3 gen_data.py
    ```

* Configure the Attack Map Server, extract the flags to the right place:

  * Open a new terminal tab (Ctrl+Shift+T, on Ubuntu).
  
    ```sh
    cd AttackMapServer/
    unzip static/flags.zip
    ``` 
 
* Start the Attack Map Server:
  
    ```sh
    sudo python3 AttackMapServer.py
    ```
 
* Access the Attack Map Server from browser:

    * [http://localhost:8888/](http://localhost:8888/) or [http://127.0.0.1:8888/](http://127.0.0.1:8888/)
  
 
